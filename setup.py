#!/usr/bin/env python3
"""
Potato Disease Classification - Setup Script
Automated setup for the potato disease classification project
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, description=""):
    """Run a shell command with error handling"""
    print(f"\n📦 {description or command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("✅ Success")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print(f"stderr: {e.stderr}")
        return None

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def create_virtual_environment():
    """Create and activate virtual environment"""
    print("\n🏗️  Creating virtual environment...")
    
    venv_path = Path("venv")
    if venv_path.exists():
        print("Virtual environment already exists")
        return True
    
    # Create virtual environment
    result = run_command(f"{sys.executable} -m venv venv", "Creating virtual environment")
    return result is not None

def activate_virtual_environment():
    """Get activation command for virtual environment"""
    if platform.system() == "Windows":
        return "venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def install_dependencies():
    """Install all project dependencies"""
    print("\n📚 Installing dependencies...")
    
    # Get pip path
    if platform.system() == "Windows":
        pip_path = "venv\\Scripts\\pip"
    else:
        pip_path = "venv/bin/pip"
    
    # Upgrade pip
    run_command(f"{pip_path} install --upgrade pip", "Upgrading pip")
    
    # Install main requirements
    if Path("requirements.txt").exists():
        run_command(f"{pip_path} install -r requirements.txt", "Installing main requirements")
    
    # Install API requirements
    if Path("api/requirements.txt").exists():
        run_command(f"{pip_path} install -r api/requirements.txt", "Installing API requirements")
    
    # Install website requirements
    if Path("website/requirements.txt").exists():
        run_command(f"{pip_path} install -r website/requirements.txt", "Installing website requirements")

def create_model_directory():
    """Create model directory structure"""
    print("\n📁 Creating model directory...")
    model_dir = Path("training/models")
    model_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created directory: {model_dir}")

def download_sample_model():
    """Download a sample model (placeholder)"""
    print("\n🤖 Model Setup:")
    print("⚠️  Please download the trained model '1.keras' and place it in 'training/models/'")
    print("📥 You can train your own model using training/training.ipynb")
    print("🔗 Or download a pre-trained model from the releases section")

def create_launcher_script():
    """Create platform-specific launcher scripts"""
    print("\n🚀 Creating launcher scripts...")
    
    if platform.system() == "Windows":
        # Windows batch script already exists
        if Path("start_app.bat").exists():
            print("✅ Windows launcher already exists: start_app.bat")
    else:
        # Create Unix launcher
        launcher_content = """#!/bin/bash
# Potato Disease Classification Launcher

echo "🥔 Starting Potato Disease Classification App..."
echo "=================================="

# Start backend
echo "🔧 Starting FastAPI backend..."
cd api
python main.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 5

# Start frontend
echo "🌐 Starting Streamlit frontend..."
cd website
streamlit run app.py &
FRONTEND_PID=$!
cd ..

echo "✅ Application started successfully!"
echo "📊 API: http://localhost:8000"
echo "🌐 Frontend: http://localhost:8501"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"
echo "=================================="

# Wait for interrupt
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
"""
        
        with open("start_app.sh", "w") as f:
            f.write(launcher_content)
        
        # Make executable
        os.chmod("start_app.sh", 0o755)
        print("✅ Created Unix launcher: start_app.sh")

def print_next_steps():
    """Print next steps for the user"""
    print("\n" + "="*50)
    print("🎉 Setup completed successfully!")
    print("="*50)
    print("\n📋 Next Steps:")
    print("1. 📥 Download the trained model '1.keras'")
    print("2. 📁 Place it in 'training/models/' directory")
    print("3. 🚀 Start the application:")
    
    if platform.system() == "Windows":
        print("   start_app.bat")
    else:
        print("   ./start_app.sh")
    
    print("\n🌐 Access Points:")
    print("   • Frontend: http://localhost:8501")
    print("   • API: http://localhost:8000")
    print("   • API Docs: http://localhost:8000/docs")
    
    print(f"\n💡 To activate the virtual environment:")
    print(f"   {activate_virtual_environment()}")

def main():
    """Main setup function"""
    print("🥔 Potato Disease Classification - Setup Script")
    print("="*50)
    
    try:
        # Check Python version
        check_python_version()
        
        # Create virtual environment
        if not create_virtual_environment():
            print("❌ Failed to create virtual environment")
            return
        
        # Install dependencies
        install_dependencies()
        
        # Create model directory
        create_model_directory()
        
        # Model setup instructions
        download_sample_model()
        
        # Create launcher scripts
        create_launcher_script()
        
        # Print next steps
        print_next_steps()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()