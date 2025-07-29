import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image
import os
import time

class TextToImageGenerator:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        """
        Initialize the text-to-image generator with a pre-trained model.
        
        Args:
            model_name (str): Name of the Hugging Face model to use
        """
        self.model_name = model_name
        self.pipeline = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
    def load_model(self):
        """Load the diffusion model."""
        try:
            print("Loading model... This may take a few minutes on first run.")
            
            # Use a smaller, faster model for CPU usage
            if self.device == "cpu":
                model_name = "CompVis/stable-diffusion-v1-4"
            else:
                model_name = self.model_name
            
            # Load the pipeline
            self.pipeline = DiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            
            # Use DPM++ 2M scheduler for faster inference
            self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipeline.scheduler.config
            )
            
            # Move to device
            self.pipeline = self.pipeline.to(self.device)
            
            # Enable memory efficient attention if using CUDA
            if self.device == "cuda":
                self.pipeline.enable_attention_slicing()
                self.pipeline.enable_sequential_cpu_offload()
            
            print("Model loaded successfully!")
            
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Trying with a smaller model...")
            self._load_fallback_model()
    
    def _load_fallback_model(self):
        """Load a smaller fallback model if the main model fails."""
        try:
            self.pipeline = DiffusionPipeline.from_pretrained(
                "CompVis/stable-diffusion-v1-4",
                torch_dtype=torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            self.pipeline = self.pipeline.to(self.device)
            print("Fallback model loaded successfully!")
        except Exception as e:
            print(f"Error loading fallback model: {e}")
            raise
    
    def generate_image(self, prompt, output_path="generated_image.png", 
                      num_inference_steps=20, guidance_scale=7.5, 
                      width=512, height=512):
        """
        Generate an image from text prompt.
        
        Args:
            prompt (str): Text description of the image to generate
            output_path (str): Path to save the generated image
            num_inference_steps (int): Number of denoising steps
            guidance_scale (float): How closely to follow the prompt
            width (int): Width of the generated image
            height (int): Height of the generated image
            
        Returns:
            PIL.Image: Generated image
        """
        if self.pipeline is None:
            raise ValueError("Model not loaded. Call load_model() first.")
        
        try:
            print(f"Generating image for prompt: '{prompt}'")
            print(f"Steps: {num_inference_steps}, Guidance: {guidance_scale}")
            start_time = time.time()
            
            # Generate the image
            image = self.pipeline(
                prompt=prompt,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                width=width,
                height=height
            ).images[0]
            
            # Save the image
            image.save(output_path)
            
            generation_time = time.time() - start_time
            print(f"Image generated successfully in {generation_time:.2f} seconds!")
            print(f"Saved to: {output_path}")
            
            return image
            
        except Exception as e:
            print(f"Error generating image: {e}")
            raise
    
    def generate_multiple_images(self, prompt, num_images=4, output_dir="generated_images"):
        """
        Generate multiple images from the same prompt.
        
        Args:
            prompt (str): Text description of the image to generate
            num_images (int): Number of images to generate
            output_dir (str): Directory to save the generated images
            
        Returns:
            list: List of generated PIL images
        """
        if self.pipeline is None:
            raise ValueError("Model not loaded. Call load_model() first.")
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        images = []
        for i in range(num_images):
            output_path = os.path.join(output_dir, f"image_{i+1}.png")
            image = self.generate_image(prompt, output_path)
            images.append(image)
        
        return images

def main():
    """Main function to demonstrate the text-to-image generator."""
    print("=== Text-to-Image Generator ===")
    print("This project demonstrates AI-powered image generation from text descriptions.")
    print()
    
    # Initialize the generator
    generator = TextToImageGenerator()
    
    # Load the model
    generator.load_model()
    
    # Example prompts
    example_prompts = [
        "A beautiful sunset over mountains, digital art style",
        "A cute cat sitting on a windowsill, watercolor painting",
        "A futuristic city with flying cars, sci-fi style",
        "A peaceful forest with sunlight filtering through trees"
    ]
    
    print("\n=== Example Prompts ===")
    for i, prompt in enumerate(example_prompts, 1):
        print(f"{i}. {prompt}")
    
    print("\n=== Interactive Mode ===")
    while True:
        print("\nEnter your prompt (or 'quit' to exit):")
        user_prompt = input("> ").strip()
        
        if user_prompt.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_prompt:
            print("Please enter a valid prompt.")
            continue
        
        try:
            # Generate the image
            output_filename = f"user_generated_{int(time.time())}.png"
            image = generator.generate_image(user_prompt, output_filename)
            
            print(f"\nImage generated successfully!")
            print(f"Check '{output_filename}' in the current directory.")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 