import logging
import os
import sqlite3
from datetime import datetime
from typing import Dict
from llama_cpp import Llama

from ontology_dc8f06af066e4a7880a5938933236037.config import ConfigClass
from ontology_dc8f06af066e4a7880a5938933236037.input import InputClass
from ontology_dc8f06af066e4a7880a5938933236037.output import OutputClass
from openfabric_pysdk.context import AppModel, State
from core.stub import Stub

# Configurations for the app
configurations: Dict[str, ConfigClass] = dict()

# Initialize LLaMA model
def init_llm():
    model_path = "models/llama-2-7b-chat.Q4_K_M.gguf"  # Path to your local model
    if not os.path.exists(model_path):
        logging.error(f"Model file not found at {model_path}")
        return None
    
    try:
        llm = Llama(
            model_path=model_path,
            n_ctx=2048,  # Context window
            n_threads=4,  # Number of CPU threads to use
            n_gpu_layers=0  # Number of layers to offload to GPU (0 for CPU only)
        )
        logging.info("LLaMA model loaded successfully")
        return llm
    except Exception as e:
        logging.error(f"Failed to load LLaMA model: {str(e)}")
        return None

# Initialize LLM on module load
llm_model = init_llm()

# Initialize SQLite database for memory
def init_db():
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS generations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  prompt TEXT,
                  expanded_prompt TEXT,
                  image_path TEXT,
                  model_path TEXT,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

# Initialize database on module load
init_db()

############################################################
# Config callback function
############################################################
def config(configuration: Dict[str, ConfigClass], state: State) -> None:
    """
    Stores user-specific configuration data.

    Args:
        configuration (Dict[str, ConfigClass]): A mapping of user IDs to configuration objects.
        state (State): The current state of the application (not used in this implementation).
    """
    for uid, conf in configuration.items():
        logging.info(f"Saving new config for user with id:'{uid}'")
        configurations[uid] = conf

def expand_prompt(prompt: str) -> str:
    """
    Expands the user's prompt using local LLaMA to create a more detailed description.

    Args:
        prompt (str): The original user prompt

    Returns:
        str: An expanded, detailed prompt suitable for image generation
    """
    if llm_model is None:
        logging.warning("LLaMA model not loaded, using fallback prompt expansion")
        return f"A highly detailed, photorealistic image of {prompt} with dramatic lighting and rich textures"

    try:
        # Construct the prompt for LLaMA
        system_prompt = """You are an expert at creating detailed, vivid descriptions for image generation. 
        Expand the given prompt into a rich, detailed description that would help create a stunning image.
        Focus on visual details, lighting, atmosphere, and artistic style."""
        
        full_prompt = f"""<s>[INST] <<SYS>>
        {system_prompt}
        <</SYS>>
        
        Original prompt: {prompt}
        
        Please expand this into a detailed description for image generation. [/INST]"""

        # Generate response
        output = llm_model(
            full_prompt,
            max_tokens=200,
            temperature=0.7,
            top_p=0.9,
            stop=["</s>", "[/INST]"],
            echo=False
        )
        
        # Extract the response
        expanded_prompt = output['choices'][0]['text'].strip()
        
        logging.info(f"Original prompt: {prompt}")
        logging.info(f"Expanded prompt: {expanded_prompt}")
        
        return expanded_prompt

    except Exception as e:
        logging.error(f"Error in prompt expansion: {str(e)}")
        return f"A highly detailed, photorealistic image of {prompt} with dramatic lighting and rich textures"

def save_to_memory(prompt: str, expanded_prompt: str, image_path: str, model_path: str):
    """
    Saves the generation details to the SQLite database.
    """
    conn = sqlite3.connect('memory.db')
    c = conn.cursor()
    c.execute('''INSERT INTO generations (prompt, expanded_prompt, image_path, model_path, timestamp)
                 VALUES (?, ?, ?, ?, ?)''',
              (prompt, expanded_prompt, image_path, model_path, datetime.now()))
    conn.commit()
    conn.close()

############################################################
# Execution callback function
############################################################
def execute(model: AppModel) -> None:
    """
    Main execution entry point for handling a model pass.

    Args:
        model (AppModel): The model object containing request and response structures.
    """
    # Retrieve input
    request: InputClass = model.request
    prompt = request.prompt

    # Retrieve user config
    user_config: ConfigClass = configurations.get('super-user', None)
    logging.info(f"{configurations}")

    # Initialize the Stub with app IDs
    app_ids = user_config.app_ids if user_config else []
    stub = Stub(app_ids)

    try:
        # Step 1: Expand the prompt using local LLM
        expanded_prompt = expand_prompt(prompt)
        logging.info(f"Expanded prompt: {expanded_prompt}")

        # Step 2: Generate image using Text-to-Image app
        text_to_image_app_id = 'f0997a01-d6d3-a5fe-53d8-561300318557'
        image_result = stub.call(text_to_image_app_id, {'prompt': expanded_prompt}, 'super-user')
        
        # Save the image
        image_path = f"generated_images/{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        os.makedirs('generated_images', exist_ok=True)
        with open(image_path, 'wb') as f:
            f.write(image_result.get('result'))

        # Step 3: Convert image to 3D using Image-to-3D app
        image_to_3d_app_id = '69543f29-4d41-4afc-7f29-3d51591f11eb'
        model_result = stub.call(image_to_3d_app_id, {'image': image_path}, 'super-user')
        
        # Save the 3D model
        model_path = f"generated_models/{datetime.now().strftime('%Y%m%d_%H%M%S')}.glb"
        os.makedirs('generated_models', exist_ok=True)
        with open(model_path, 'wb') as f:
            f.write(model_result.get('result'))

        # Step 4: Save to memory
        save_to_memory(prompt, expanded_prompt, image_path, model_path)

        # Prepare response
        response: OutputClass = model.response
        response.message = f"Successfully generated 3D model from prompt: {prompt}\nImage saved at: {image_path}\n3D model saved at: {model_path}"

    except Exception as e:
        logging.error(f"Error in execution: {str(e)}")
        response: OutputClass = model.response
        response.message = f"Error processing request: {str(e)}"