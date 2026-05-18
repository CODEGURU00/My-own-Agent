# ⚡ Antigravity Agent

A free, terminal-based **"vibe code" AI assistant** that can build websites, apps, and AI services autonomously. Powered by a multi-agent CrewAI system with local LLM reasoning (Ollama) and Nvidia API for media generation.

## 🎯 What It Can Build

### Websites
- Portfolio, Freelancing Platform, E-Commerce
- Content Creation, Social Media, Dating
- Video Chat, AI-Powered Sites, Streaming

### Mobile Apps
- E-Commerce, Social Media, Video Chat
- Adult Games (with legal compliance), Streaming

### AI Services
- Image Generation (Nvidia SDXL)
- Video Generation (Nvidia Cosmos)
- Voice/TTS (Nvidia Riva)
- Music Generation

---

## 📦 Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | Core runtime |
| Ollama | Latest | Local LLM inference |
| Node.js | 18+ | Project scaffolding |
| Git | Latest | Version control |

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Clone and enter the project
cd "My agent"

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Linux/Mac

# Install Python packages
pip install -r requirements.txt
```

### 2. Set Up Ollama

```bash
# Install Ollama from https://ollama.ai
# Pull the model
ollama pull devstral-small:24b
# or
ollama pull qwen3:8b
```

### 3. Configure Environment

```bash
# Copy the example env file
copy .env.example .env

# Edit .env and set your NVIDIA_API_KEY
```

### 4. Index Knowledge Base

```bash
python main.py --index
```

### 5. Launch the TUI

```bash
python main.py
```

---

## 🖥️ Usage

### TUI Commands

| Command | Description |
|---------|-------------|
| `/build <description>` | Build a new project |
| `/search <query>` | Search the knowledge base |
| `/clear` | Clear the chat log |
| `/refresh` | Refresh the file tree |
| `/quit` | Exit the application |

### CLI Mode

```bash
# One-shot build
python main.py --build "a portfolio website with contact form"

# Check configuration
python main.py --check

# Re-index knowledge base
python main.py --index
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Q` | Quit |
| `Ctrl+R` | Refresh file tree |
| `Ctrl+K` | Clear chat |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                  Textual TUI                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ File Tree│  │ Chat Log │  │ Terminal Out  │  │
│  │          │  │          │  │              │  │
│  │ Knowledge│  │ Agent    │  │ Dev Server   │  │
│  │ Panel    │  │ Steps    │  │ Output       │  │
│  └──────────┘  └──────────┘  └──────────────┘  │
└──────────────────────┬──────────────────────────┘
                       │
              ┌────────▼────────┐
              │   CrewAI Crew    │
              │                  │
              │  ┌─ Architect    │  → Knowledge Search
              │  ├─ Developer   │  → File I/O, Scaffolding, Nvidia
              │  └─ QA Engineer │  → Testing, Dev Server
              └────────┬────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
    ┌────▼────┐  ┌─────▼─────┐  ┌───▼────┐
    │ Ollama  │  │ ChromaDB  │  │ Nvidia │
    │ (LLM)  │  │ (Vector)  │  │ (API)  │
    └─────────┘  └───────────┘  └────────┘
```

## 📁 Project Structure

```
My agent/
├── main.py                    # Entry point
├── crew_config.yaml           # CrewAI agent/task definitions
├── requirements.txt           # Python dependencies
├── .env.example               # Environment template
├── .gitignore
├── README.md
├── antigravity/               # Core package
│   ├── __init__.py
│   ├── config.py              # Configuration manager
│   ├── crew.py                # CrewAI crew builder
│   ├── knowledge_base.py      # ChromaDB manager
│   ├── tui.py                 # Textual TUI
│   └── tools/
│       ├── __init__.py
│       ├── local_tools.py     # File, bash, project tools
│       └── nvidia_tools.py    # Nvidia API tools
├── knowledge/                 # 18 knowledge base files
│   ├── web_portfolio.md
│   ├── web_freelancing.md
│   ├── web_ecommerce.md
│   ├── web_content_creation.md
│   ├── web_social_media.md
│   ├── web_dating.md
│   ├── web_video_chat.md
│   ├── web_ai_site.md
│   ├── web_streaming.md
│   ├── app_ecommerce.md
│   ├── app_social_media.md
│   ├── app_video_chat.md
│   ├── app_games_adult.md
│   ├── app_streaming.md
│   ├── ai_image_gen.md
│   ├── ai_video_gen.md
│   ├── ai_voice_gen.md
│   └── ai_music_gen.md
├── workspace/                 # Generated projects go here
└── chroma_db/                 # ChromaDB persistence
```

## 🔐 Security

- **Never commit `.env`** — API keys stay local
- Store `NVIDIA_API_KEY` in environment variables only
- All file operations are sandboxed to `workspace/`
- Nvidia API calls are server-side only

## 📅 Roadmap

| Phase | Task | Status |
|-------|------|--------|
| 1 | Core dependencies & Ollama setup | ✅ |
| 2 | 18 knowledge base files | ✅ |
| 3 | Tool functions (local + Nvidia) | ✅ |
| 4 | CrewAI crew configuration | ✅ |
| 5 | Textual TUI | ✅ |
| 6 | Testing on simple projects | 🔜 |
| 7 | Mobile & advanced apps | 🔜 |

---

**Built with ❤️ by Antigravity**
