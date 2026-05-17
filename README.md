# 📚 AI Study - Intelligent Flashcard Generator

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status: Active Development](https://img.shields.io/badge/Status-Active%20Development-brightgreen)]()

## 🎯 Overview

**AI Study** is an intelligent flashcard generation platform that transforms learning materials into effective study tools. Using advanced AI models, it automatically extracts key concepts from URLs or text and generates contextually accurate flashcards—cutting study preparation time by up to 80%.

Perfect for students, educators, and professionals who need to learn more efficiently without the tedious manual flashcard creation process.

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔗 **URL-to-Flashcards** | Extract content from web pages and instantly generate flashcards |
| 📝 **Text-to-Flashcards** | Convert any text material (documents, articles, notes) into study cards |
| 🤖 **AI-Powered Generation** | Leverages Llama 3.3 70B for intelligent question-answer pair creation |
| 🎨 **Visual Flashcards** | Beautiful, automatically formatted flashcard images ready for study |
| 🎵 **Audio Transcription** | Download and transcribe video/audio content (YouTube support) |
| 💾 **Session Management** | Browser-based interface with stateful session handling |
| 🌐 **Multi-Language Support** | Automatically detects and generates content in Portuguese or English |

## 🛠 Technology Stack

- **Backend Framework**: Python 3.8+
- **Frontend**: Streamlit (web-based UI)
- **AI/LLM**: Groq API (Llama 3.3 70B model)
- **Media Processing**: yt-dlp, FFmpeg
- **Speech-to-Text**: Whisper API
- **Image Generation**: Pillow (PIL)
- **API Communication**: Python Requests

## 📋 Prerequisites

Before installation, ensure you have:
- Python 3.8 or higher installed
- A Groq API key (free tier available at [console.groq.com](https://console.groq.com))
- FFmpeg installed (for audio processing)
- pip package manager

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-study.git
cd ai-study
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.streamlit/secrets.toml` file in your project root:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

You can obtain a free API key from [Groq Console](https://console.groq.com).

## 🎮 Usage

### Running the Application

```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

### Workflow

#### Method 1: URL to Flashcards
1. Navigate to the **"🖥 Url to Flashcards"** tab
2. Paste a URL (webpage, article, or video link)
3. Click **"Gerar Flashcards URL"**
4. Browse generated flashcards using navigation arrows

#### Method 2: Text to Flashcards
1. Go to the **"📙 Text to Flashcards"** tab
2. Paste or type your study material
3. Click **"Gerar Flashcards Texto"**
4. Review and navigate through the generated cards

#### Example Input
```
Deep Learning is a subset of machine learning that uses neural networks 
with multiple layers. These networks can automatically learn hierarchical 
representations of data, making them effective for complex tasks like 
image recognition, natural language processing, and speech recognition.
```

#### Expected Output
```
R: What is Deep Learning?
Q: A subset of machine learning using multi-layer neural networks that 
   automatically learn hierarchical data representations for complex tasks.

R: Name three applications of Deep Learning.
Q: Image recognition, natural language processing, and speech recognition.
```

## 📁 Project Structure

```
ai-study/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
├── README.md              # This file
│
├── app/
│   ├── __init__.py        
│   └── interface.py       # Streamlit UI and session management
│
├── services/
│   ├── __init__.py
│   ├── flashcards.py      # Flashcard image generation logic
│   ├── perguntas.py       # AI-powered Q&A generation (Groq integration)
│   ├── audio.py           # Media download utilities (yt-dlp)
│   └── transcrever.py     # Audio transcription (Whisper API)
│
├── flashcards/            # Generated flashcard images (PNG)
├── downloads/             # Downloaded media files
└── .streamlit/
    └── secrets.toml       # API configuration (git-ignored)
```

## 📊 How It Works

```
User Input (URL/Text)
        ↓
Audio Download & Transcription (if URL is media)
        ↓
Text Extraction & Normalization
        ↓
Groq Llama 3.3 70B (AI Processing)
        ↓
Q&A Pair Generation
        ↓
Flashcard Image Creation (Pillow)
        ↓
Interactive Browser Display (Streamlit)
```

## 🎨 Screenshots & Demo

## 🚀 Future Improvements

- [ ] **Export Formats**: Download flashcards as PDF, DOCX, or Anki decks
- [ ] **Spaced Repetition**: Built-in SRS algorithm for optimal learning
- [ ] **Analytics Dashboard**: Track study progress and retention metrics
- [ ] **Collaborative Features**: Share decks and study with teammates
- [ ] **Multiple AI Models**: Support for GPT-4, Claude, and other LLMs
- [ ] **Advanced Formatting**: Support for images, code blocks, and LaTeX equations in cards
- [ ] **Mobile App**: React Native version for iOS/Android
- [ ] **Batch Processing**: Generate multiple decks from bulk content
- [ ] **Custom Themes**: User-configurable flashcard designs
- [ ] **API Endpoint**: RESTful API for programmatic access

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, features, or documentation improvements, your help makes this project better.

### Getting Started with Development

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and commit (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to functions
- Test your changes locally before submitting
- Update documentation as needed
- Reference any related issues in your PR

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License allows you to:
- ✅ Use commercially
- ✅ Modify the code
- ✅ Distribute
- ✅ Use privately
- ⚠️ Must include license and copyright notice

## 💬 Contact & Support

**Author**: [Eduardo Bonemetti]

**Questions or Need Help?**
- 💼 LinkedIn: [www.linkedin.com/in/eduardobonometti](https://linkedin.com/in/yourprofile)

**Found a Bug?**
- Open an [Issue](../../issues) on GitHub
- Include detailed steps to reproduce
- Attach relevant logs or screenshots

## 🌟 Acknowledgments

- [Groq](https://groq.com/) - Fast, production-ready LLM API
- [Streamlit](https://streamlit.io/) - Rapid web app development
- [OpenAI Whisper](https://openai.com/research/whisper) - Speech recognition
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Media downloading

---

<div align="center">

**Made with ❤️ for learners everywhere**

[⭐ Star this repo](../../) if you found it useful!

</div>
