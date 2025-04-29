# 🚀 AI Creative Partner

A powerful AI-powered application that transforms text descriptions into stunning visuals and 3D models using Openfabric and local LLMs.

## 🌟 Features

- **Text-to-Image Generation**: Convert your creative ideas into beautiful images
- **Image-to-3D Conversion**: Transform generated images into interactive 3D models
- **Local LLM Integration**: Powered by Llama for intelligent prompt understanding
- **Modern Web Interface**: Beautiful Streamlit UI for easy interaction
- **Memory System**: Track and recall your previous creations
- **Advanced Options**: Control style and quality of generations

## 🛠️ Technical Stack

- **Backend**:
  - Python 3.9+ (excluding 3.9.7) or Python 3.12
  - Openfabric SDK
  - Local LLM (Llama)
  - Poetry for dependency management

- **Frontend**:
  - Streamlit
  - Pillow for image processing
  - Web-based 3D model viewer

## 📦 Installation

### Prerequisites

- Python 3.9+ (excluding 3.9.7) or Python 3.12
- Poetry package manager
- Git
- At least 8GB RAM (16GB recommended)
- 10GB free disk space for models

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-test
```

2. Create and activate a virtual environment in the project root:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
cd app
poetry install
```

### Model Setup

1. The `models` directory is located inside the `app` directory:
```bash
cd app
mkdir models
```

2. Download the required model:
   - Download `llama-2-7b-chat.Q4_K_M.gguf` from the official source

3. Place the downloaded model file in the `app/models` directory:
   - The model file should be in `.gguf` format
   - Rename it to `model` for consistency

4. Verify the model setup:
   - The `app/models` directory should contain:
     ```
     app/models/
     ├── model           # Your downloaded model file
     └── README.md       # Model information
     ```

## 🚀 Running the Application

The application can be run in two ways:

### 1. API Mode (Backend)

Run the main application that provides the API endpoints:

```bash
# On Windows
cd app
start.bat

# On Linux/Mac
cd app
./start.sh
```

The API will be available at `http://localhost:8888`

### 2. Web Interface (Frontend)

Run the Streamlit interface:

```bash
# On Windows
cd app
run_streamlit.bat

# On Linux/Mac
cd app
chmod +x run_streamlit.sh
./run_streamlit.sh
```

The web interface will be available at `http://localhost:8501`

## 📝 Usage

1. **Access the Web Interface**:
   - Open your browser and navigate to `http://localhost:8501`
   - You'll see the AI Creative Partner interface

2. **Create Your Masterpiece**:
   - Enter your creative prompt in the text area
   - (Optional) Adjust advanced options like style and quality
   - Click "Generate" to create your artwork

3. **View Results**:
   - Generated images will appear in the preview section
   - 3D models will be displayed when available
   - Recent creations are stored in the sidebar

4. **File Storage**:
   - Generated images are saved in `app/generated_images/`
   - 3D models are saved in `app/generated_models/`

## 🧠 How It Works

1. **User Input**:
   - User provides a text description
   - Local LLM processes and enhances the prompt

2. **Image Generation**:
   - Enhanced prompt is sent to Openfabric's Text-to-Image app
   - High-quality image is generated and saved

3. **3D Conversion**:
   - Generated image is processed by Openfabric's Image-to-3D app
   - Interactive 3D model is created and saved

4. **Memory System**:
   - All creations are stored locally
   - Users can reference previous works
   - System maintains context for future generations

## 📁 Project Structure

```
AI-test/                  # Project root
├── venv/                 # Virtual environment
├── app/                  # Application code
│   ├── main.py          # Main application logic
│   ├── streamlit_app.py # Web interface
│   ├── pyproject.toml   # Dependencies
│   ├── start.bat        # Windows startup script
│   ├── start.sh         # Linux/Mac startup script
│   ├── models/          # Local LLM models
│   │   ├── model       # Downloaded model file
│   │   └── README.md   # Model information
│   ├── generated_images/ # Generated image storage
│   └── generated_models/ # Generated 3D model storage
└── readme.md           # This documentation
```

## 🔧 Configuration

The application can be configured through environment variables:

- `OPENFABRIC_API_KEY`: Your Openfabric API key
- `LLM_MODEL_PATH`: Path to your local LLM model (default: models/model)
- `PORT`: API server port (default: 8888)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Openfabric for their powerful AI tools
- Streamlit for the beautiful web interface
- The open-source community for their contributions

---

Made with ❤️ by Deepanshu Saini