"""
Main Academic Assistant Application
Integrates all modules: Summarizer, Q&A Tool, and Content Generator
"""

import argparse
import sys
import os
from typing import Optional

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from summarizer import TextSummarizer
from qa_tool import QATool
from content_generator import ContentGenerator

class AcademicAssistant:
    """Main class that integrates all academic assistant functionalities."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize all components."""
        self.summarizer = TextSummarizer(api_key)
        self.qa_tool = QATool(api_key)
        self.content_generator = ContentGenerator(api_key)
    
    def summarize(self, text: str) -> str:
        """Summarize text using the summarizer module."""
        return self.summarizer.summarize(text)
    
    def answer_question(self, context: str, question: str) -> str:
        """Answer question using the Q&A module."""
        return self.qa_tool.answer_question(context, question)
    
    def generate_content(self, topic: str) -> str:
        """Generate content using the content generator module."""
        return self.content_generator.generate_content(topic)
    
    def interactive_mode(self):
        """Run the assistant in interactive mode."""
        print("Academic Assistant - Interactive Mode")
        print("Available commands: summarize, qa, generate, quit")
        print("-" * 50)
        
        while True:
            command = input("\nEnter command (summarize/qa/generate/quit): ").strip().lower()
            
            if command == "quit":
                print("Goodbye!")
                break
            
            elif command == "summarize":
                text = input("Enter text to summarize: ")
                if text.strip():
                    result = self.summarize(text)
                    print(f"\nSummary:\n{result}")
                else:
                    print("Error: No text provided.")
            
            elif command == "qa":
                context = input("Enter context: ")
                question = input("Enter question: ")
                if context.strip() and question.strip():
                    result = self.answer_question(context, question)
                    print(f"\nAnswer:\n{result}")
                else:
                    print("Error: Both context and question required.")
            
            elif command == "generate":
                topic = input("Enter topic: ")
                if topic.strip():
                    result = self.generate_content(topic)
                    print(f"\nGenerated Content:\n{result}")
                else:
                    print("Error: No topic provided.")
            
            else:
                print("Invalid command. Use: summarize, qa, generate, or quit")

def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(description="AI-Powered Academic Assistant")
    parser.add_argument("--mode", choices=["summarize", "qa", "generate", "interactive"], 
                       required=True, help="Operation mode")
    parser.add_argument("--input", help="Input text for summarization")
    parser.add_argument("--context", help="Context for Q&A")
    parser.add_argument("--question", help="Question for Q&A")
    parser.add_argument("--topic", help="Topic for content generation")
    parser.add_argument("--api-key", help="OpenAI API key")
    
    args = parser.parse_args()
    
    # Initialize assistant
    assistant = AcademicAssistant(args.api_key)
    
    if args.mode == "interactive":
        assistant.interactive_mode()
    
    elif args.mode == "summarize":
        if not args.input:
            print("Error: --input required for summarization")
            return
        result = assistant.summarize(args.input)
        print("Summary:")
        print(result)
    
    elif args.mode == "qa":
        if not args.context or not args.question:
            print("Error: --context and --question required for Q&A")
            return
        result = assistant.answer_question(args.context, args.question)
        print("Answer:")
        print(result)
    
    elif args.mode == "generate":
        if not args.topic:
            print("Error: --topic required for content generation")
            return
        result = assistant.generate_content(args.topic)
        print("Generated Content:")
        print(result)

if __name__ == "__main__":
    # Check if running with command line arguments
    if len(sys.argv) > 1:
        main()
    else:
        # Run demo if no arguments provided
        print("Academic Assistant Demo")
        print("=" * 40)
        
        assistant = AcademicAssistant()
        
        # Demo text
        demo_text = """
        Artificial Intelligence (AI) has revolutionized numerous industries and continues 
        to shape the future of technology. Machine learning, a subset of AI, enables 
        computers to learn and improve from experience without being explicitly programmed. 
        Deep learning, which uses neural networks with multiple layers, has achieved 
        remarkable success in image recognition, natural language processing, and game 
        playing. However, AI also raises important ethical considerations including bias, 
        privacy, job displacement, and the need for transparency in algorithmic 
        decision-making. As AI systems become more sophisticated, it is crucial to 
        develop responsible AI practices that ensure these technologies benefit society 
        while minimizing potential risks.
        """
        
        print("\nDemo: Text Summarization")
        summary = assistant.summarize(demo_text)
        print(summary)
        
        print("\nDemo: Question Answering")
        question = "What are the ethical considerations of AI?"
        answer = assistant.answer_question(demo_text, question)
        print(f"Q: {question}")
        print(f"A: {answer}")
        
        print("\nDemo: Content Generation")
        topic = "Neural Networks"
        content = assistant.generate_content(topic)
        print(f"Topic: {topic}")
        print(content)