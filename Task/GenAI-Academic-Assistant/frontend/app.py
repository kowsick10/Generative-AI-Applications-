"""
Flask Backend for AI Academic Assistant Frontend
Serves the web interface and handles API calls
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import AcademicAssistant

app = Flask(__name__, 
            template_folder='.',
            static_folder='static')
CORS(app)

@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')

@app.route('/api/summarize', methods=['POST'])
def api_summarize():
    """Handle text summarization requests."""
    try:
        data = request.get_json()
        text = data.get('text', '')
        api_key = data.get('api_key', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        if not api_key:
            return jsonify({'error': 'API key required'}), 400
        
        assistant = AcademicAssistant(api_key)
        result = assistant.summarize(text)
        
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/qa', methods=['POST'])
def api_qa():
    """Handle question answering requests."""
    try:
        data = request.get_json()
        context = data.get('context', '')
        question = data.get('question', '')
        api_key = data.get('api_key', '')
        
        if not context or not question:
            return jsonify({'error': 'Both context and question required'}), 400
        
        if not api_key:
            return jsonify({'error': 'API key required'}), 400
        
        assistant = AcademicAssistant(api_key)
        result = assistant.answer_question(context, question)
        
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/generate', methods=['POST'])
def api_generate():
    """Handle content generation requests."""
    try:
        data = request.get_json()
        topic = data.get('topic', '')
        api_key = data.get('api_key', '')
        
        if not topic:
            return jsonify({'error': 'No topic provided'}), 400
        
        if not api_key:
            return jsonify({'error': 'API key required'}), 400
        
        assistant = AcademicAssistant(api_key)
        result = assistant.generate_content(topic)
        
        return jsonify({'result': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'message': 'AI Academic Assistant API is running'})

if __name__ == '__main__':
    print("🚀 Starting AI Academic Assistant Web Interface...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🔑 Don't forget to add your OpenAI API key in the web interface!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)