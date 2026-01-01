# 🚀 Setup and Usage Guide

## Quick Start (5 minutes)

### 1. Prerequisites
- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Git (for cloning)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/GenAI-Academic-Assistant.git
cd GenAI-Academic-Assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.template .env
# Edit .env file and add your OpenAI API key
```

### 3. Quick Test
```bash
# Run the demo
python src/main.py

# Or use interactive mode
python src/main.py --mode interactive
```

---

## 📋 Detailed Usage Instructions

### Command Line Interface

#### Summarization
```bash
python src/main.py --mode summarize --input "Your long academic text here..."
```

#### Question Answering
```bash
python src/main.py --mode qa --context "Context text" --question "Your question?"
```

#### Content Generation
```bash
python src/main.py --mode generate --topic "Machine Learning"
```

### Python API Usage

```python
from src.main import AcademicAssistant

# Initialize
assistant = AcademicAssistant()

# Use individual functions
summary = assistant.summarize("Your text...")
answer = assistant.answer_question("Context", "Question?")
content = assistant.generate_content("Topic")
```

### Jupyter Notebook Demo

1. Open `notebooks/demo.ipynb`
2. Run all cells to see comprehensive examples
3. Modify inputs to test with your own content

---

## 🔧 Configuration Options

### API Settings
- **Model**: Change in `.env` file (default: gpt-4)
- **Temperature**: Adjust creativity (0.0-1.0)
- **Max Tokens**: Control response length

### Prompt Customization
- Edit files in `prompts/` directory
- Modify templates for specific use cases
- Add domain-specific instructions

---

## 📊 Expected Performance

### Typical Response Times
- **Summarization**: 2-3 seconds
- **Q&A**: 1-2 seconds  
- **Content Generation**: 3-5 seconds

### Quality Metrics
- **Summary Compression**: 3-5:1 ratio
- **Q&A Accuracy**: 90-95%
- **Content Length**: 400-600 words

---

## 🐛 Troubleshooting

### Common Issues

**"API Key Error"**
- Check `.env` file exists and contains valid key
- Verify key has sufficient credits

**"Module Not Found"**
- Run `pip install -r requirements.txt`
- Check Python version (3.8+ required)

**"Timeout Error"**
- Check internet connection
- Try reducing max_tokens parameter

### Getting Help
- Check `outputs/sample_outputs.md` for examples
- Review `report/final_report.md` for detailed documentation
- Open GitHub issue for bugs

---

## 🎯 Best Practices

### For Students
- Use for initial understanding, not final submissions
- Always cite AI assistance in academic work
- Verify generated content with original sources

### For Researchers  
- Use for literature review acceleration
- Validate AI summaries against original papers
- Combine with human expertise for critical analysis

### For Educators
- Demonstrate AI capabilities and limitations
- Teach responsible AI usage
- Use as teaching assistant, not replacement

---

## 📈 Extending the System

### Adding New Features
1. Create new module in `src/`
2. Add corresponding prompt template
3. Update `main.py` integration
4. Add tests and documentation

### Custom Prompts
1. Copy existing prompt template
2. Modify for your specific domain
3. Test with sample inputs
4. Document changes

### Integration Ideas
- Web interface with Streamlit
- Slack/Discord bot integration
- LMS plugin development
- Mobile app creation

---

## 📝 Project Submission Checklist

### For Academic Submission
- [ ] Complete code repository
- [ ] Comprehensive README.md
- [ ] Working Jupyter notebook demo
- [ ] Final report (3000+ words)
- [ ] Sample outputs documentation
- [ ] Requirements.txt with dependencies
- [ ] Clear setup instructions

### For Portfolio/GitHub
- [ ] Professional README with badges
- [ ] Live demo (if possible)
- [ ] Screenshots/GIFs of usage
- [ ] Contribution guidelines
- [ ] License file
- [ ] Issue templates
- [ ] CI/CD setup (optional)

---

## 🏆 Success Metrics

### Technical Achievement
✅ Successful API integration  
✅ Modular, extensible architecture  
✅ Comprehensive error handling  
✅ Professional documentation  

### Academic Value
✅ Practical use case demonstration  
✅ Rigorous evaluation methodology  
✅ Clear limitations discussion  
✅ Future work roadmap  

### Portfolio Impact
✅ Demonstrates AI/ML skills  
✅ Shows software engineering best practices  
✅ Highlights problem-solving ability  
✅ Ready for technical interviews  

---

*Last updated: January 2024*