"""
Content Generation Module for Academic Assistant
"""

import openai
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the content generator with OpenAI API key."""
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
    def load_prompt_template(self) -> str:
        """Load the content generation prompt template."""
        try:
            with open("prompts/generation.txt", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return self._default_prompt()
    
    def _default_prompt(self) -> str:
        """Default prompt if file not found."""
        return """Explain the following topic for a university-level student.
        Use headings, examples, and a clear conclusion.
        
        Topic: {topic}"""
    
    def generate_content(self, topic: str, max_tokens: int = 800) -> str:
        """
        Generate structured academic content for a given topic.
        
        Args:
            topic (str): Topic to explain
            max_tokens (int): Maximum tokens for response
            
        Returns:
            str: Generated academic content
        """
        if not topic.strip():
            return "Error: No topic provided for content generation."
        
        prompt_template = self.load_prompt_template()
        prompt = prompt_template.format(topic=topic)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.4,
                top_p=0.9
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error in content generation: {str(e)}"
    
    def generate_outline(self, topic: str) -> str:
        """Generate a structured outline for a topic."""
        outline_prompt = f"""
        Create a detailed outline for the topic: {topic}
        
        Format the outline with:
        1. Main sections (I, II, III...)
        2. Subsections (A, B, C...)
        3. Key points (1, 2, 3...)
        
        Make it suitable for a university-level academic paper.
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": outline_prompt}],
                max_tokens=500,
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error in outline generation: {str(e)}"
    
    def expand_section(self, topic: str, section: str) -> str:
        """Expand a specific section of a topic."""
        expand_prompt = f"""
        Write a detailed explanation for the following section of {topic}:
        
        Section: {section}
        
        Provide:
        - Clear definitions
        - Relevant examples
        - Academic references where appropriate
        - 200-300 words
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": expand_prompt}],
                max_tokens=400,
                temperature=0.4
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error in section expansion: {str(e)}"

if __name__ == "__main__":
    # Test the content generator
    generator = ContentGenerator()
    
    sample_topic = "Machine Learning Ethics"
    
    result = generator.generate_content(sample_topic)
    print("Generated Content:")
    print(result)
    
    print("\n" + "="*50 + "\n")
    
    outline = generator.generate_outline(sample_topic)
    print("Generated Outline:")
    print(outline)