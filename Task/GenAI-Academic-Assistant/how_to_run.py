"""
Quick Demo Script - Shows how to use the AI Academic Assistant
"""

import sys
import os
sys.path.append('src')

def demo_usage():
    """Show different ways to use the system."""
    
    print("=" * 60)
    print("AI ACADEMIC ASSISTANT - USAGE DEMO")
    print("=" * 60)
    
    print("\n1. COMMAND LINE USAGE:")
    print("-" * 30)
    print("# Summarize text:")
    print('python src/main.py --mode summarize --input "Your long text here..."')
    print()
    print("# Answer questions:")
    print('python src/main.py --mode qa --context "Context text" --question "Your question?"')
    print()
    print("# Generate content:")
    print('python src/main.py --mode generate --topic "Machine Learning"')
    print()
    print("# Interactive mode:")
    print('python src/main.py --mode interactive')
    
    print("\n2. PYTHON API USAGE:")
    print("-" * 30)
    print("""
from src.main import AcademicAssistant

# Initialize the assistant
assistant = AcademicAssistant()

# Summarize text
text = "Your long academic text here..."
summary = assistant.summarize(text)
print("Summary:", summary)

# Answer questions
context = "Context about the topic..."
question = "What is the main point?"
answer = assistant.answer_question(context, question)
print("Answer:", answer)

# Generate content
topic = "Artificial Intelligence"
content = assistant.generate_content(topic)
print("Generated Content:", content)
""")
    
    print("\n3. SAMPLE INPUTS AND OUTPUTS:")
    print("-" * 30)
    
    # Sample academic text
    sample_text = """
    Artificial Intelligence (AI) has revolutionized numerous industries and continues 
    to shape the future of technology. Machine learning, a subset of AI, enables 
    computers to learn and improve from experience without being explicitly programmed. 
    Deep learning, which uses neural networks with multiple layers, has achieved 
    remarkable success in image recognition, natural language processing, and game 
    playing. However, AI also raises important ethical considerations including bias, 
    privacy, job displacement, and the need for transparency in algorithmic 
    decision-making.
    """
    
    print("SAMPLE INPUT:")
    print(sample_text.strip())
    
    print("\nEXPECTED SUMMARY OUTPUT:")
    print("• AI has revolutionized industries and shapes technology's future")
    print("• Machine learning enables computers to learn from experience without explicit programming")
    print("• Deep learning uses multi-layer neural networks for various applications")
    print("• Achieved success in image recognition, NLP, and game playing")
    print("• Raises ethical concerns about bias, privacy, job displacement, and transparency")
    
    print("\nSAMPLE Q&A:")
    print("Question: What are the ethical considerations of AI?")
    print("Expected Answer: AI raises important ethical considerations including bias,")
    print("privacy concerns, job displacement, and the need for transparency in")
    print("algorithmic decision-making processes.")
    
    print("\n4. JUPYTER NOTEBOOK DEMO:")
    print("-" * 30)
    print("Run: jupyter notebook notebooks/demo.ipynb")
    print("- Complete interactive demonstration")
    print("- Visualizations and performance analysis")
    print("- Step-by-step examples")
    
    print("\n5. PROJECT FILES OVERVIEW:")
    print("-" * 30)
    print("src/main.py           - Main application")
    print("src/summarizer.py     - Text summarization module")
    print("src/qa_tool.py        - Question answering module")
    print("src/content_generator.py - Content generation module")
    print("notebooks/demo.ipynb  - Interactive Jupyter demo")
    print("test_system.py        - System validation script")
    print("README.md             - Complete documentation")
    print("report/final_report.md - Academic report (3000+ words)")
    
    print("\n" + "=" * 60)
    print("READY TO USE!")
    print("=" * 60)
    print("1. Add your OpenAI API key to .env file")
    print("2. Choose any of the usage methods above")
    print("3. Start generating AI-powered academic content!")

if __name__ == "__main__":
    demo_usage()