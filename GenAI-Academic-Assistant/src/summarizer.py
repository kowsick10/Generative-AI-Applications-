"""
Text Summarization Module for Academic Assistant
"""

import openai
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class TextSummarizer:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the summarizer with OpenAI API key."""
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
    def load_prompt_template(self) -> str:
        """Load the summarization prompt template."""
        try:
            with open("prompts/summarization.txt", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return self._default_prompt()
    
    def _default_prompt(self) -> str:
        """Default prompt if file not found."""
        return """You are an academic assistant. Summarize the following text in 5-6 clear bullet points.
        Use formal language and do not add external information.
        
        Text: {input_text}"""
    
    def summarize(self, text: str, max_tokens: int = 500) -> str:
        """
        Summarize the given text using GPT-4.
        
        Args:
            text (str): Text to summarize
            max_tokens (int): Maximum tokens for response
            
        Returns:
            str: Summarized text
        """
        if not text.strip():
            return "Error: No text provided for summarization."
        
        prompt_template = self.load_prompt_template()
        prompt = prompt_template.format(input_text=text)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.3,
                top_p=0.9
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error in summarization: {str(e)}"
    
    def batch_summarize(self, texts: list) -> list:
        """Summarize multiple texts."""
        return [self.summarize(text) for text in texts]

if __name__ == "__main__":
    # Test the summarizer
    summarizer = TextSummarizer()
    
    sample_text = """
    Federated learning is a machine learning technique that trains an algorithm across 
    multiple decentralized edge devices or servers holding local data samples, without 
    exchanging them. This approach stands in contrast to traditional centralized machine 
    learning techniques where all the local datasets are uploaded to one server, as well 
    as to more classical decentralized approaches which often assume that local data 
    samples are identically distributed. Federated learning enables multiple actors to 
    build a common, robust machine learning model without sharing data, thus allowing to 
    address critical issues such as data privacy, data security, data access rights and 
    access to heterogeneous data.
    """
    
    result = summarizer.summarize(sample_text)
    print("Summary:")
    print(result)