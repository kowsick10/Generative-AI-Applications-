"""
Test Script for AI Academic Assistant
Run this to validate your setup and API connection
"""

import sys
import os
sys.path.append('src')

def test_imports():
    """Test if all modules can be imported."""
    try:
        from summarizer import TextSummarizer
        from qa_tool import QATool
        from content_generator import ContentGenerator
        from main import AcademicAssistant
        print("All modules imported successfully")
        return True
    except ImportError as e:
        print(f"Import error: {e}")
        return False

def test_api_connection():
    """Test API connection with a simple request."""
    try:
        from main import AcademicAssistant
        assistant = AcademicAssistant()
        test_text = "This is a simple test to verify API connectivity."
        result = assistant.summarize(test_text)
        
        if "Error" in result:
            print(f"API Error: {result}")
            return False
        else:
            print("API connection successful")
            print(f"Sample response: {result[:100]}...")
            return True
    except Exception as e:
        print(f"API connection failed: {e}")
        return False

def test_all_modules():
    """Test all three main modules."""
    try:
        from main import AcademicAssistant
        assistant = AcademicAssistant()
        
        # Test data
        test_text = "Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed."
        test_question = "What is machine learning?"
        test_topic = "Artificial Intelligence"
        
        print("\nTesting Summarization...")
        summary = assistant.summarize(test_text)
        print(f"Result: {summary[:100]}...")
        
        print("\nTesting Q&A...")
        answer = assistant.answer_question(test_text, test_question)
        print(f"Result: {answer[:100]}...")
        
        print("\nTesting Content Generation...")
        content = assistant.generate_content(test_topic)
        print(f"Result: {content[:100]}...")
        
        print("\nAll modules tested successfully!")
        return True
        
    except Exception as e:
        print(f"Module testing failed: {e}")
        return False

def main():
    """Run all tests."""
    print("AI Academic Assistant - System Test")
    print("=" * 50)
    
    # Check environment
    if not os.path.exists('.env') and not os.getenv('OPENAI_API_KEY'):
        print("Warning: No .env file found and no OPENAI_API_KEY environment variable")
        print("   Please set up your API key before running tests")
        return
    
    # Run tests
    tests = [
        ("Import Test", test_imports),
        ("API Connection Test", test_api_connection),
        ("Module Functionality Test", test_all_modules)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("\nAll tests passed! Your system is ready to use.")
        print("\nNext steps:")
        print("1. Try the interactive mode: python src/main.py --mode interactive")
        print("2. Open the Jupyter notebook: jupyter notebook notebooks/demo.ipynb")
        print("3. Read the documentation in README.md")
    else:
        print("\nSome tests failed. Please check your setup:")
        print("1. Ensure all dependencies are installed: pip install -r requirements.txt")
        print("2. Verify your OpenAI API key is set correctly")
        print("3. Check your internet connection")

if __name__ == "__main__":
    main()