"""
Web Interface Launcher for AI Academic Assistant
Run this script to start the web interface
"""

import os
import sys
import subprocess
import webbrowser
import time
from threading import Timer

def install_requirements():
    """Install Flask and CORS if not already installed."""
    try:
        import flask
        from flask_cors import CORS
        print("✅ Flask dependencies already installed")
    except ImportError:
        print("📦 Installing Flask dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "flask-cors"])
        print("✅ Flask dependencies installed successfully")

def open_browser():
    """Open the web browser after a short delay."""
    time.sleep(2)
    webbrowser.open('http://localhost:5000')

def main():
    """Main function to launch the web interface."""
    print("🎓 AI Academic Assistant - Web Interface Launcher")
    print("=" * 60)
    
    # Install requirements
    install_requirements()
    
    # Change to frontend directory
    frontend_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(frontend_dir)
    
    print(f"📁 Working directory: {frontend_dir}")
    print("🚀 Starting web server...")
    
    # Open browser after delay
    Timer(3.0, open_browser).start()
    
    # Start Flask app
    try:
        from app import app
        print("\n🌐 Web interface starting at: http://localhost:5000")
        print("🔑 Remember to add your OpenAI API key in the web interface!")
        print("⏹️  Press Ctrl+C to stop the server")
        print("-" * 60)
        
        app.run(debug=False, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\n👋 Web server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting web server: {e}")
        print("💡 Try running: python app.py")

if __name__ == "__main__":
    main()