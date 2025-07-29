import streamlit as st
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image
import os
import time
import io
import base64

# Page configuration
st.set_page_config(
    page_title="AI Text-to-Image Generator",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.2rem;
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 10px;
    }
    .stButton > button:hover {
        background-color: #0d5aa7;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
    }
    .parameter-info {
        background-color: #e8f4fd;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
    
    /* Hide Streamlit menu and deploy button */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide the hamburger menu (three dots) */
    .stDeployButton {display: none;}
    
    /* Hide the "Made with Streamlit" footer */
    .reportview-container .main footer {display: none;}
    
    /* Additional hiding for newer Streamlit versions */
    [data-testid="stDeployButton"] {display: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the diffusion model with caching."""
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Use a smaller model for CPU usage
        if device == "cpu":
            model_name = "CompVis/stable-diffusion-v1-4"
        else:
            model_name = "runwayml/stable-diffusion-v1-5"
        
        pipeline = DiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            safety_checker=None,
            requires_safety_checker=False
        )
        
        # Use DPM++ 2M scheduler for faster inference
        pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
            pipeline.scheduler.config
        )
        
        pipeline = pipeline.to(device)
        
        if device == "cuda":
            pipeline.enable_attention_slicing()
            pipeline.enable_sequential_cpu_offload()
        
        return pipeline, device
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

def generate_image(pipeline, prompt, num_inference_steps, guidance_scale, width, height):
    """Generate image using the pipeline."""
    try:
        image = pipeline(
            prompt=prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            width=width,
            height=height
        ).images[0]
        return image
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🎨 AI Text-to-Image Generator</h1>', unsafe_allow_html=True)
    
    # Model loading (hidden)
    if 'pipeline' not in st.session_state:
        with st.spinner("Loading AI model... This may take a few minutes on first run."):
            pipeline, device = load_model()
            st.session_state.pipeline = pipeline
            st.session_state.device = device
    
    if st.session_state.pipeline is None:
        st.error("Failed to load model. Please check your internet connection and try again.")
        return
    
    # Default parameters
    num_inference_steps = 20
    guidance_scale = 7.5
    width = 512
    height = 512
    

    
    # Main content
    st.header("🎯 Enter Your Prompt")
    
    # Prompt input
    prompt = st.text_area(
        "",
        height=100,
        placeholder="Describe your image in detail... (e.g., 'A beautiful sunset over mountains, digital art style')"
    )
    
    # Generate button
    if st.button("🚀 Generate Image", type="primary"):
        if not prompt.strip():
            st.warning("Please enter a prompt first!")
        else:
            with st.spinner("🎨 Generating your image... This may take a minute or two."):
                start_time = time.time()
                
                image = generate_image(
                    st.session_state.pipeline,
                    prompt,
                    num_inference_steps,
                    guidance_scale,
                    width,
                    height
                )
                
                if image:
                    generation_time = time.time() - start_time
                    
                    # Display the generated image
                    st.success(f"✅ Image generated successfully in {generation_time:.2f} seconds!")
                    
                    # Display image
                    st.image(image, caption=f"Generated from: '{prompt}'", use_container_width=True)
                    
                    # Download button
                    buf = io.BytesIO()
                    image.save(buf, format='PNG')
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="📥 Download Image",
                        data=byte_im,
                        file_name=f"generated_image_{int(time.time())}.png",
                        mime="image/png"
                    )
    


if __name__ == "__main__":
    main() 