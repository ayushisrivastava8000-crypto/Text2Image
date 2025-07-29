# 🚀 Setup Guide - Text-to-Image Generator

This guide will help you set up and run the Text-to-Image Generator project using a virtual environment.

## 🔧 Complete Setup Instructions

### Step 1: Verify Current Setup

Your project is now properly set up with a virtual environment. Check the current structure:

```bash
ls -la
```

You should see:
- `venv/` - Virtual environment directory
- `app.py` - Streamlit web application
- `text_to_image.py` - Command-line interface
- `demo.py` - Demo script
- `requirements.txt` - Dependencies
- `README.md` - Documentation
- `.gitignore` - Git ignore file
- `test_setup.py` - Setup verification script

### Step 2: Activate Virtual Environment

**Always activate the virtual environment before running the project:**

```bash
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

You'll know it's activated when you see `(venv)` at the start of your command prompt.

### Step 3: Verify Installation

Run the test script to ensure everything is working:

```bash
python test_setup.py
```

You should see: `🎉 All tests passed! Your setup is ready.`

### Step 4: Run the Application

#### Option A: Web Interface (Recommended)
```bash
streamlit run app.py
```
Then open your browser to `http://localhost:8501`

#### Option B: Demo Mode
```bash
python demo.py
```
This will generate 4 example images automatically.

#### Option C: Command Line Interface
```bash
python text_to_image.py
```
Interactive mode where you can enter prompts.

## 🎯 Understanding Parameters

### Number of Steps (Inference Steps)
- **What it does**: Controls how many times the AI refines the image
- **Range**: 10-50 (default: 20)
- **Impact**: More steps = better quality but slower generation
- **Recommendations**:
  - 10-15: Fast generation, basic quality
  - 20-25: Balanced quality and speed (recommended)
  - 30-50: High quality, slower generation

### Guidance Scale (CFG Scale)
- **What it does**: Controls how closely the AI follows your text prompt
- **Range**: 1.0-20.0 (default: 7.5)
- **Impact**: Higher values = more prompt adherence
- **Recommendations**:
  - 1.0-3.0: Very creative, may ignore parts of prompt
  - 3.0-7.0: Balanced creativity and prompt following
  - 7.0-10.0: Closely follows prompt (recommended)
  - 10.0-20.0: Strictly follows prompt, may look artificial

## 🎨 Example Prompts to Try

### Landscapes
- "A beautiful sunset over mountains, digital art style"
- "A peaceful forest with sunlight filtering through trees"
- "A serene Japanese garden with cherry blossoms, watercolor painting"

### Fantasy/Sci-Fi
- "A majestic dragon flying over a medieval castle, fantasy art style"
- "A futuristic cyberpunk city at night with neon lights, digital art"
- "A magical castle floating in the clouds, fantasy art"

### Everyday Scenes
- "A cozy coffee shop interior with warm lighting, oil painting style"
- "A cute cat sitting on a windowsill, watercolor painting"
- "A vintage car driving through a neon-lit city at night"

## 🔧 Troubleshooting

### Virtual Environment Issues

**Problem**: `command not found: python`
**Solution**: Make sure virtual environment is activated:
```bash
source venv/bin/activate
```

**Problem**: `ModuleNotFoundError`
**Solution**: Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Model Loading Issues

**Problem**: Model download fails
**Solution**: 
- Check internet connection
- Ensure 5GB+ free disk space
- Try again later (Hugging Face servers might be busy)

**Problem**: Out of memory
**Solution**:
- Close other applications
- Use smaller image dimensions (512x512)
- Reduce number of steps to 15-20

### Performance Issues

**Slow Generation**:
- Reduce number of inference steps
- Use smaller image dimensions
- Close other applications

**High Memory Usage**:
- Use CPU mode (automatic on most systems)
- Reduce image dimensions
- Close unnecessary applications

## 📁 File Structure Explained

```
text-to-img/
├── venv/                    # Virtual environment (isolated Python)
├── app.py                   # Streamlit web application
├── text_to_image.py         # Command-line interface
├── demo.py                  # Demo script with examples
├── test_setup.py           # Setup verification script
├── requirements.txt        # Python dependencies
├── README.md              # Main documentation
├── .gitignore             # Git ignore rules
└── generated_images/      # Output directory (created automatically)
```

## 🎓 Best Practices

### Always Use Virtual Environment
- **Why**: Keeps project dependencies isolated
- **How**: Always activate with `source venv/bin/activate`
- **Benefit**: Prevents conflicts with system Python packages

### Parameter Tuning
- **Start with defaults**: 20 steps, 7.5 guidance
- **For speed**: Reduce steps to 15
- **For quality**: Increase steps to 30
- **For creativity**: Reduce guidance to 5-7
- **For accuracy**: Increase guidance to 10-12

### Prompt Writing
- **Be specific**: Include style, lighting, mood
- **Use style keywords**: "digital art", "watercolor", "oil painting"
- **Keep concise**: 50-200 characters for best results
- **Include details**: Setting, lighting, atmosphere

## 🚀 Quick Commands Reference

```bash
# Activate virtual environment
source venv/bin/activate

# Test setup
python test_setup.py

# Run web interface
streamlit run app.py

# Run demo
python demo.py

# Run command line interface
python text_to_image.py

# Deactivate virtual environment
deactivate
```

## 🎉 Success!

Your Text-to-Image Generator is now properly set up with:
- ✅ Virtual environment for isolation
- ✅ All dependencies installed
- ✅ Multiple interfaces (web, CLI, demo)
- ✅ Comprehensive documentation
- ✅ Parameter explanations
- ✅ Troubleshooting guide

**Happy generating! 🎨✨** 