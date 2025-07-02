"""
Setup script for News Impact Analyzer
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    if not os.path.exists(env_file):
        print("🔧 Creating .env file...")
        with open(env_file, "w") as f:
            f.write("# OpenAI API Configuration\n")
            f.write("# Get your API key from: https://platform.openai.com/api-keys\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n\n")
            f.write("# Application Configuration\n")
            f.write("APP_NAME=News Impact Analyzer\n")
            f.write("APP_VERSION=1.0.0\n\n")
            f.write("# OpenAI Model Settings\n")
            f.write("OPENAI_MODEL=gpt-3.5-turbo\n")
            f.write("OPENAI_MAX_TOKENS=1000\n")
            f.write("OPENAI_TEMPERATURE=0.3\n\n")
            f.write("# Web Scraping Settings\n")
            f.write("REQUEST_TIMEOUT=10\n")
            f.write("MAX_CONTENT_LENGTH=4000\n\n")
            f.write("# Streamlit Settings\n")
            f.write("STREAMLIT_SERVER_PORT=8501\n")
            f.write("STREAMLIT_SERVER_ADDRESS=localhost\n")
        print("✅ .env file created!")
        print("⚠️  Please edit .env file and add your OpenAI API key")
    else:
        print("ℹ️  .env file already exists")

def main():
    print("🚀 Setting up News Impact Analyzer...\n")
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed. Please check your Python environment.")
        return
    
    # Create .env file
    create_env_file()
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run: streamlit run app.py")
    print("3. Open your browser to http://localhost:8501")

if __name__ == "__main__":
    main() 