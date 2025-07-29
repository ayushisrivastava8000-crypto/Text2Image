#!/usr/bin/env python3
"""
Simple test script to verify the virtual environment setup
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported."""
    print("🧪 Testing Virtual Environment Setup")
    print("=" * 40)
    
    required_packages = [
        'torch',
        'diffusers', 
        'transformers',
        'accelerate',
        'PIL',
        'streamlit',
        'numpy'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                importlib.import_module('PIL.Image')
            else:
                importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Please check your virtual environment setup.")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_basic_functionality():
    """Test basic functionality without loading the full model."""
    print("\n🔧 Testing Basic Functionality")
    print("=" * 40)
    
    try:
        # Test if we can import our custom module
        from text_to_image import TextToImageGenerator
        print("✅ TextToImageGenerator class imported successfully")
        
        # Test if we can create an instance
        generator = TextToImageGenerator()
        print("✅ TextToImageGenerator instance created successfully")
        
        print("✅ Basic functionality test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    """Main test function."""
    print("🎨 Text-to-Image Generator - Setup Test")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test basic functionality
    functionality_ok = test_basic_functionality()
    
    print("\n" + "=" * 50)
    if imports_ok and functionality_ok:
        print("🎉 All tests passed! Your setup is ready.")
        print("\n🚀 Next steps:")
        print("1. Run demo: python demo.py")
        print("2. Run web app: streamlit run app.py")
        print("3. Run CLI: python text_to_image.py")
    else:
        print("❌ Some tests failed. Please check your setup.")
        print("\n💡 Troubleshooting:")
        print("1. Make sure virtual environment is activated")
        print("2. Run: pip install -r requirements.txt")
        print("3. Check your Python version (3.8+)")

if __name__ == "__main__":
    main() 