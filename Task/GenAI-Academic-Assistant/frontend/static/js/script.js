// Modern JavaScript for AI Academic Assistant
class AcademicAssistant {
    constructor() {
        this.apiKey = '';
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupAnimations();
        this.loadApiKey();
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const section = link.getAttribute('data-section');
                this.showSection(section);
            });
        });

        // Tab switching
        document.querySelectorAll('.tab-button').forEach(button => {
            button.addEventListener('click', () => {
                const tab = button.getAttribute('data-tab');
                this.switchTab(tab);
            });
        });

        // API key toggle
        const toggleBtn = document.getElementById('toggleApiKey');
        const apiKeyInput = document.getElementById('apiKey');
        
        if (toggleBtn && apiKeyInput) {
            toggleBtn.addEventListener('click', () => {
                const type = apiKeyInput.type === 'password' ? 'text' : 'password';
                apiKeyInput.type = type;
                toggleBtn.innerHTML = type === 'password' ? 
                    '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
            });

            apiKeyInput.addEventListener('input', () => {
                this.apiKey = apiKeyInput.value;
                localStorage.setItem('openai_api_key', this.apiKey);
            });
        }

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    }

    setupAnimations() {
        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe elements for animation
        document.querySelectorAll('.feature-card, .stat-item, .demo-card').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s ease';
            observer.observe(el);
        });
    }

    loadApiKey() {
        const savedKey = localStorage.getItem('openai_api_key');
        if (savedKey) {
            this.apiKey = savedKey;
            const apiKeyInput = document.getElementById('apiKey');
            if (apiKeyInput) {
                apiKeyInput.value = savedKey;
            }
        }
    }

    showSection(sectionId) {
        // Hide all sections
        document.querySelectorAll('.section').forEach(section => {
            section.classList.remove('active');
        });

        // Show target section
        const targetSection = document.getElementById(sectionId);
        if (targetSection) {
            targetSection.classList.add('active');
        }

        // Update navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        
        const activeLink = document.querySelector(`[data-section="${sectionId}"]`);
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }

    switchTab(tabId) {
        // Hide all tab contents
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });

        // Show target tab
        const targetTab = document.getElementById(`${tabId}-tab`);
        if (targetTab) {
            targetTab.classList.add('active');
        }

        // Update tab buttons
        document.querySelectorAll('.tab-button').forEach(button => {
            button.classList.remove('active');
        });

        const activeButton = document.querySelector(`[data-tab="${tabId}"]`);
        if (activeButton) {
            activeButton.classList.add('active');
        }
    }

    showLoading() {
        document.getElementById('loadingOverlay').style.display = 'flex';
    }

    hideLoading() {
        document.getElementById('loadingOverlay').style.display = 'none';
    }

    showResult(resultId, content) {
        const resultBox = document.getElementById(resultId);
        const resultContent = resultBox.querySelector('.result-content');
        
        resultContent.innerHTML = content;
        resultBox.style.display = 'block';
        
        // Smooth scroll to result
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        
        // Add animation
        resultBox.style.opacity = '0';
        resultBox.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            resultBox.style.transition = 'all 0.5s ease';
            resultBox.style.opacity = '1';
            resultBox.style.transform = 'translateY(0)';
        }, 100);
    }

    async makeApiCall(endpoint, data) {
        if (!this.apiKey) {
            throw new Error('Please enter your OpenAI API key first.');
        }

        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.apiKey}`
            },
            body: JSON.stringify({
                model: 'gpt-4',
                messages: [{ role: 'user', content: data.prompt }],
                max_tokens: data.max_tokens || 500,
                temperature: data.temperature || 0.3
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error?.message || 'API request failed');
        }

        const result = await response.json();
        return result.choices[0].message.content;
    }

    async summarizeText() {
        const text = document.getElementById('summarizeText').value.trim();
        
        if (!text) {
            alert('Please enter some text to summarize.');
            return;
        }

        this.showLoading();

        try {
            const prompt = `You are an expert academic assistant specializing in text summarization.
Your task is to summarize the following academic content into 5-6 clear, concise bullet points.

Guidelines:
- Use formal, academic language
- Focus on key concepts and main ideas
- Do not add external information not present in the text
- Each bullet point should be self-contained
- Maintain logical flow between points

Text to summarize:
${text}

Provide your summary in bullet point format.`;

            const result = await this.makeApiCall('summarize', {
                prompt: prompt,
                max_tokens: 500,
                temperature: 0.3
            });

            this.showResult('summarizeResult', `<div class="summary-result">${result}</div>`);
        } catch (error) {
            this.showResult('summarizeResult', `<div class="error-result">❌ Error: ${error.message}</div>`);
        } finally {
            this.hideLoading();
        }
    }

    async answerQuestion() {
        const context = document.getElementById('qaContext').value.trim();
        const question = document.getElementById('qaQuestion').value.trim();
        
        if (!context || !question) {
            alert('Please provide both context and question.');
            return;
        }

        this.showLoading();

        try {
            const prompt = `You are an expert academic assistant specializing in question answering.
Answer the question STRICTLY based on the provided context.

Guidelines:
- Only use information present in the given context
- If the answer is not found, respond with "Information not found in the provided text."
- Provide direct, factual answers
- Use academic tone and precise language

Context:
${context}

Question:
${question}

Answer:`;

            const result = await this.makeApiCall('qa', {
                prompt: prompt,
                max_tokens: 300,
                temperature: 0.2
            });

            this.showResult('qaResult', `<div class="qa-result"><strong>Q:</strong> ${question}<br><br><strong>A:</strong> ${result}</div>`);
        } catch (error) {
            this.showResult('qaResult', `<div class="error-result">❌ Error: ${error.message}</div>`);
        } finally {
            this.hideLoading();
        }
    }

    async generateContent() {
        const topic = document.getElementById('generateTopic').value.trim();
        
        if (!topic) {
            alert('Please enter a topic to generate content about.');
            return;
        }

        this.showLoading();

        try {
            const prompt = `You are an expert academic writer and educator.
Create a comprehensive explanation of the topic suitable for university-level students.

Guidelines:
- Use clear, academic language
- Structure with proper headings
- Include relevant examples
- Provide logical flow from basic to advanced concepts
- End with clear conclusion
- Keep between 300-500 words

Topic: ${topic}

Required structure:
1. Introduction
2. Key Concepts
3. Examples/Applications
4. Conclusion

Generate the content:`;

            const result = await this.makeApiCall('generate', {
                prompt: prompt,
                max_tokens: 800,
                temperature: 0.4
            });

            this.showResult('generateResult', `<div class="content-result">${result.replace(/\n/g, '<br>')}</div>`);
        } catch (error) {
            this.showResult('generateResult', `<div class="error-result">❌ Error: ${error.message}</div>`);
        } finally {
            this.hideLoading();
        }
    }
}

// Global functions for HTML onclick events
function showSection(sectionId) {
    window.assistant.showSection(sectionId);
}

function summarizeText() {
    window.assistant.summarizeText();
}

function answerQuestion() {
    window.assistant.answerQuestion();
}

function generateContent() {
    window.assistant.generateContent();
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    window.assistant = new AcademicAssistant();
    
    // Add some nice loading effects
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
    
    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero-image');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });
    
    // Add typing effect to hero text
    const heroTitle = document.querySelector('.hero-content h2');
    if (heroTitle) {
        const text = heroTitle.textContent;
        heroTitle.textContent = '';
        let i = 0;
        
        const typeWriter = () => {
            if (i < text.length) {
                heroTitle.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        };
        
        setTimeout(typeWriter, 500);
    }
});