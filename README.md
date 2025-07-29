# 🎨 AI Text-to-Image Generator

A fully functional text-to-image generator built with Python, showcasing AI-powered image generation capabilities. This project uses state-of-the-art diffusion models to transform text descriptions into stunning visual artwork.

## ✨ Features

- **AI-Powered Generation**: Uses Stable Diffusion models for high-quality image generation
- **User-Friendly Interface**: Both command-line and web-based interfaces
- **Customizable Parameters**: Control generation steps, guidance scale, and image dimensions
- **Multiple Output Formats**: Generate single images or multiple variations
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Easy Setup**: Simple installation process with clear instructions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Internet connection (for downloading models)
- At least 4GB RAM (8GB recommended)
- Optional: NVIDIA GPU with CUDA support for faster generation

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd text-to-img
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   **Option A: Web Interface (Recommended)**
   ```bash
   streamlit run app.py
   ```
   Then open your browser to `http://localhost:8501`

   **Option B: Command Line Interface**
   ```bash
   python text_to_image.py
   ```

   **Option C: Demo Mode**
   ```bash
   python demo.py
   ```

## 📖 Usage Guide

### Web Interface (Streamlit)

1. **Launch the app**: Run `streamlit run app.py`
2. **Wait for model loading**: The AI model will download automatically on first run
3. **Enter your prompt**: Describe the image you want to generate
4. **Adjust settings**: Use the sidebar to customize generation parameters
5. **Generate**: Click the "Generate Image" button
6. **Download**: Save your generated image

### Command Line Interface

1. **Run the script**: `python text_to_image.py`
2. **Wait for model loading**: The model will download on first run
3. **Enter prompts**: Type your image descriptions when prompted
4. **View results**: Generated images are saved in the current directory

### Example Prompts

- "A beautiful sunset over mountains, digital art style"
- "A cute cat sitting on a windowsill, watercolor painting"
- "A futuristic city with flying cars, sci-fi style"
- "A peaceful forest with sunlight filtering through trees"
- "A magical castle floating in the clouds, fantasy art"

## ⚙️ Configuration

### Generation Parameters

- **Number of Steps**: Controls generation quality (10-50, default: 20)
  - More steps = better quality but slower generation
  - 10-15: Fast generation, basic quality
  - 20-25: Balanced quality and speed (recommended)
  - 30-50: High quality, slower generation

- **Guidance Scale**: How closely to follow the prompt (1.0-20.0, default: 7.5)
  - Higher values = more closely follow the prompt
  - 1.0-3.0: Very creative, may ignore parts of prompt
  - 3.0-7.0: Balanced creativity and prompt following
  - 7.0-10.0: Closely follows prompt (recommended)
  - 10.0-20.0: Strictly follows prompt, may look artificial

- **Image Dimensions**: Width and height in pixels (512, 768, or 1024)

### Model Selection

The application automatically selects the best model based on your hardware:
- **GPU**: Uses Stable Diffusion v1.5 for better quality
- **CPU**: Uses Stable Diffusion v1.4 for faster loading

## 🛠️ Technical Details

### Architecture

- **Backend**: Python with PyTorch and Hugging Face Diffusers
- **Frontend**: Streamlit for web interface
- **Models**: Stable Diffusion (CompVis/stable-diffusion-v1-4, runwayml/stable-diffusion-v1-5)
- **Scheduler**: DPM++ 2M for optimized generation

### File Structure

```
text-to-img/
├── app.py                 # Streamlit web application
├── text_to_image.py       # Command-line interface
├── demo.py               # Demo script with predefined examples
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── venv/                # Virtual environment (created during setup)
└── generated_images/    # Output directory (created automatically)
```

### Dependencies

- `torch`: PyTorch for deep learning
- `diffusers`: Hugging Face diffusion models
- `transformers`: Text processing and model loading
- `accelerate`: Optimized model loading
- `Pillow`: Image processing
- `streamlit`: Web interface
- `numpy`: Numerical computations

## 🎯 Tips for Better Results

1. **Be Specific**: Include details about style, lighting, and composition
2. **Use Style Keywords**: Add terms like "digital art", "watercolor", "oil painting"
3. **Describe Lighting**: Mention "sunset", "dramatic lighting", "soft shadows"
4. **Include Setting**: Specify background, environment, and atmosphere
5. **Keep Prompts Concise**: Aim for 50-200 characters for optimal results

## 🔧 Troubleshooting

### Common Issues

**Model Loading Errors**
- Ensure stable internet connection
- Check available disk space (models are ~4GB)
- Try running with CPU if GPU memory is insufficient

**Slow Generation**
- Reduce number of inference steps
- Use smaller image dimensions
- Close other applications to free memory

**Memory Issues**
- Use CPU mode if GPU memory is limited
- Reduce image dimensions
- Close other applications

### Performance Optimization

- **GPU Users**: Enable CUDA for 5-10x faster generation
- **CPU Users**: Use smaller models and fewer steps
- **Memory**: Close unnecessary applications during generation

## 📚 Educational Value

This project demonstrates several important concepts:

- **AI/ML Integration**: Using pre-trained models for practical applications
- **Web Development**: Building user interfaces with Streamlit
- **API Design**: Creating reusable classes and functions
- **Error Handling**: Robust error management and fallback options
- **User Experience**: Intuitive interfaces and helpful feedback

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the user interface
- Optimizing performance
- Adding more example prompts
- Creating documentation

## 📄 License

This project is for educational purposes. The underlying models are subject to their respective licenses.

## 🙏 Acknowledgments

- **Hugging Face**: For providing the diffusion models and libraries
- **Stability AI**: For developing Stable Diffusion
- **Streamlit**: For the excellent web framework
- **PyTorch**: For the deep learning framework

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Ensure all dependencies are properly installed
3. Verify your Python version (3.8+)
4. Check your internet connection for model downloads

---

**Happy Generating! 🎨✨** 