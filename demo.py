#!/usr/bin/env python3
"""
Demo script for the Text-to-Image Generator
This script demonstrates the capabilities of the AI image generator with predefined examples.
"""

import os
import time
from text_to_image import TextToImageGenerator

def run_demo():
    """Run a demonstration of the text-to-image generator."""
    print("🎨 Text-to-Image Generator Demo")
    print("=" * 50)
    print("This demo will generate several example images to showcase the AI's capabilities.")
    print()
    
    # Initialize the generator
    print("Initializing AI model...")
    generator = TextToImageGenerator()
    
    # Load the model
    generator.load_model()
    print()
    
    # Demo prompts with different styles and themes
    demo_prompts = [
        {
            "prompt": "A majestic dragon flying over a medieval castle, fantasy art style",
            "description": "Fantasy scene with detailed dragon and castle"
        },
        {
            "prompt": "A serene Japanese garden with cherry blossoms, watercolor painting",
            "description": "Peaceful nature scene in traditional Japanese style"
        },
        {
            "prompt": "A futuristic cyberpunk city at night with neon lights, digital art",
            "description": "Sci-fi urban landscape with vibrant colors"
        },
        {
            "prompt": "A cozy coffee shop interior with warm lighting, oil painting style",
            "description": "Intimate indoor scene with atmospheric lighting"
        }
    ]
    
    # Create output directory
    output_dir = "demo_images"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Generating {len(demo_prompts)} demo images...")
    print(f"Images will be saved in the '{output_dir}' directory.")
    print()
    
    total_start_time = time.time()
    
    for i, demo in enumerate(demo_prompts, 1):
        print(f"🎨 Generating image {i}/{len(demo_prompts)}")
        print(f"   Description: {demo['description']}")
        print(f"   Prompt: {demo['prompt']}")
        
        # Generate the image
        output_filename = f"demo_image_{i:02d}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            image = generator.generate_image(
                prompt=demo['prompt'],
                output_path=output_path,
                num_inference_steps=25,  # Slightly higher quality for demo
                guidance_scale=8.0
            )
            print(f"   ✅ Successfully generated: {output_filename}")
            
        except Exception as e:
            print(f"   ❌ Error generating image: {e}")
        
        print()
    
    total_time = time.time() - total_start_time
    print("=" * 50)
    print(f"🎉 Demo completed in {total_time:.2f} seconds!")
    print(f"📁 Check the '{output_dir}' directory for generated images.")
    print()
    print("💡 Tips for using the generator:")
    print("   • Be specific about style and mood")
    print("   • Include details about lighting and composition")
    print("   • Try different art styles (digital art, watercolor, oil painting)")
    print("   • Experiment with different prompts to see varied results")
    print()
    print("🚀 To run the full application:")
    print("   • Web interface: streamlit run app.py")
    print("   • Command line: python text_to_image.py")

def main():
    """Main function to run the demo."""
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\n⚠️ Demo interrupted by user.")
        print("Thanks for trying the Text-to-Image Generator!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    main() 