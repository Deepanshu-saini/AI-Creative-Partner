# 🚀 AI Creative Partner

A powerful AI-powered application that transforms text descriptions into stunning visuals and 3D models using Openfabric and local LLMs.

## 🌟 Features

- **Text-to-Image Generation**: Convert your creative ideas into beautiful images
- **Image-to-3D Conversion**: Transform generated images into interactive 3D models
- **Local LLM Integration**: Powered by DeepSeek or Llama for intelligent prompt understanding
- **Modern Web Interface**: Beautiful Streamlit UI for easy interaction
- **Memory System**: Track and recall your previous creations
- **Advanced Options**: Control style and quality of generations

## 🛠️ Technical Stack

- **Backend**:
  - Python 3.8+
  - Openfabric SDK
  - Local LLM (DeepSeek/Llama)
  - Poetry for dependency management

- **Frontend**:
  - Streamlit
  - Pillow for image processing
  - Model-viewer for 3D visualization

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
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

2. Create and activate a virtual environment:
```bash
python -m venv venv
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

1. Create a `models` directory in the project root:
```bash
mkdir models
```

2. Download the required model:
   - llama-2-7b-chat.Q4_K_M.gguf

3. Place the downloaded model file in the `models` directory:
   - The model file should be in `.gguf` format

4. Verify the model setup:
   - The `models` directory should contain:
     ```
     models/
     ├── model            # Your downloaded model file
     └── README.md        # Model information
     ```

## 🚀 Running the Application

The application can be run in two ways:

### 1. API Mode (Backend)

Run the main application that provides the API endpoints:

```bash
# On Windows
start.sh

# On Linux/Mac
./start.sh
```

The API will be available at `http://localhost:8888`

### 2. Web Interface (Frontend)

Run the Streamlit interface:

```bash
# On Windows
run_streamlit.bat

# On Linux/Mac
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
   - Generated images are saved in `generated_images/`
   - 3D models are saved in `generated_models/`

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
AI-test/
├── app/
│   ├── main.py              # Main application logic
│   ├── streamlit_app.py     # Web interface
│   ├── pyproject.toml       # Dependencies
│   └── run_streamlit.sh     # Run script
├── models/                  # Local LLM models
│   ├── model               # Downloaded model file
│   └── README.md           # Model information
├── generated_images/        # Generated image storage
├── generated_models/        # Generated 3D model storage
└── readme.md               # This documentation
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