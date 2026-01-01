"""
Question Answering Module for Academic Assistant
"""

import openai
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class QATool:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Q&A tool with OpenAI API key."""
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
    def load_prompt_template(self) -> str:
        """Load the Q&A prompt template."""
        try:
            with open("prompts/qa.txt", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return self._default_prompt()
    
    def _default_prompt(self) -> str:
        """Default prompt if file not found."""
        return """Answer the question ONLY using the given context.
        If the answer is not present, say "Information not found in the text."
        
        Context: {context}
        Question: {question}"""
    
    def answer_question(self, context: str, question: str, max_tokens: int = 300) -> str:
        """
        Answer a question based on the provided context.
        
        Args:
            context (str): Context text to search for answers
            question (str): Question to answer
            max_tokens (int): Maximum tokens for response
            
        Returns:
            str: Answer to the question
        """
        if not context.strip() or not question.strip():
            return "Error: Both context and question must be provided."
        
        prompt_template = self.load_prompt_template()
        prompt = prompt_template.format(context=context, question=question)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.2,
                top_p=0.9
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"Error in question answering: {str(e)}"
    
    def batch_qa(self, context: str, questions: list) -> dict:
        """Answer multiple questions for the same context."""
        results = {}
        for i, question in enumerate(questions):
            results[f"Q{i+1}"] = {
                "question": question,
                "answer": self.answer_question(context, question)
            }
        return results
    
    def validate_answer(self, context: str, answer: str) -> bool:
        """Basic validation to check if answer is grounded in context."""
        # Simple keyword matching - can be enhanced
        answer_words = set(answer.lower().split())
        context_words = set(context.lower().split())
        
        # Check if at least 30% of answer words are in context
        overlap = len(answer_words.intersection(context_words))
        return overlap / len(answer_words) >= 0.3 if answer_words else False

if __name__ == "__main__":
    # Test the Q&A tool
    qa_tool = QATool()
    
    sample_context = """
    Federated learning is a machine learning technique that trains an algorithm across 
    multiple decentralized edge devices or servers holding local data samples, without 
    exchanging them. This approach enables multiple actors to build a common, robust 
    machine learning model without sharing data, thus addressing critical issues such 
    as data privacy, data security, and access to heterogeneous data.
    """
    
    sample_question = "What are the privacy benefits of federated learning?"
    
    result = qa_tool.answer_question(sample_context, sample_question)
    print("Question:", sample_question)
    print("Answer:", result)