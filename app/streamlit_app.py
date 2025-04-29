import streamlit as st
import requests
import json
import os
from PIL import Image
import io
import base64
import time

# Constants
API_URL = "http://localhost:8888/execution"
GENERATED_IMAGES_DIR = "../generated_images"
GENERATED_MODELS_DIR = "../generated_models"

# Ensure directories exist
os.makedirs(GENERATED_IMAGES_DIR, exist_ok=True)
os.makedirs(GENERATED_MODELS_DIR, exist_ok=True)

# Page config
st.set_page_config(
    page_title="AI Creative Partner",
    page_icon="🎨",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🎨 AI Creative Partner")
st.markdown("""
    Transform your ideas into stunning visuals and 3D models. 
    Just describe what you want to create, and let the AI do the magic!
""")

# Sidebar for history and settings
with st.sidebar:
    st.header("History & Settings")
    
    # Memory section
    st.subheader("Recent Creations")
    if os.path.exists(GENERATED_IMAGES_DIR):
        recent_files = sorted(os.listdir(GENERATED_IMAGES_DIR), 
                            key=lambda x: os.path.getctime(os.path.join(GENERATED_IMAGES_DIR, x)),
                            reverse=True)[:5]
        for file in recent_files:
            if file.endswith(('.png', '.jpg', '.jpeg')):
                st.image(os.path.join(GENERATED_IMAGES_DIR, file), width=100)
                st.caption(file)

# Main content area
col1, col2 = st.columns(2)

with col1:
    # Input section
    st.subheader("Describe Your Creation")
    prompt = st.text_area(
        "What would you like to create?",
        placeholder="e.g., A glowing dragon standing on a cliff at sunset",
        height=100
    )
    
    # Advanced options
    with st.expander("Advanced Options"):
        style = st.selectbox(
            "Art Style",
            ["Realistic", "Cartoon", "Cyberpunk", "Fantasy", "Minimalist"]
        )
        quality = st.slider("Quality", 1, 10, 7)
    
    if st.button("Generate", key="generate"):
        if prompt:
            with st.spinner("Creating your masterpiece..."):
                # Prepare the request
                payload = {
                    "prompt": prompt,
                    "style": style,
                    "quality": quality
                }
                
                try:
                    # Call the API
                    response = requests.post(API_URL, json=payload)
                    response.raise_for_status()
                    
                    # Process the response
                    result = response.json()
                    
                    # Save and display the generated image
                    if "image" in result:
                        image_data = base64.b64decode(result["image"])
                        image = Image.open(io.BytesIO(image_data))
                        
                        # Save the image
                        timestamp = int(time.time())
                        image_path = os.path.join(GENERATED_IMAGES_DIR, f"generated_{timestamp}.png")
                        image.save(image_path)
                        
                        # Display the image
                        st.image(image, caption="Generated Image", use_column_width=True)
                        
                        # Show 3D model if available
                        if "model" in result:
                            st.success("3D Model generated successfully!")
                            model_path = os.path.join(GENERATED_MODELS_DIR, f"model_{timestamp}.glb")
                            with open(model_path, "wb") as f:
                                f.write(base64.b64decode(result["model"]))
                            
                            # Display 3D model viewer
                            st.markdown(f"""
                                <iframe src="https://modelviewer.dev/shadowed" 
                                        width="100%" 
                                        height="400" 
                                        frameborder="0" 
                                        allowfullscreen>
                                </iframe>
                            """, unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a description for your creation")

with col2:
    # Preview section
    st.subheader("Preview")
    st.info("Your creation will appear here once generated")
    
    # Placeholder for the generated content
    if "last_generated" in st.session_state:
        st.image(st.session_state.last_generated, caption="Last Generated Image", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Powered by Openfabric AI</p>
    </div>
""", unsafe_allow_html=True) 