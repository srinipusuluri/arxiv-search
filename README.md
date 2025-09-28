# 🔎 ArXiv Research Bot  

A simple **AI-powered search engine for ArXiv** papers, built with **NiceGUI**.  
I developed this project with the help of **Cline AI Agent inside VS Code**, which acted like a coding pair programmer.  

![Demo Screenshot](screenshot.png)  

---

## 🚀 Features
- Search **latest ArXiv papers** on AI, LLMs, RAG, and more  
- Filter results by **topic keyword** (e.g., `"RAG"`, `"federated learning"`)  
- Clean **card-style UI** powered by [NiceGUI](https://nicegui.io)  
- Each result shows:  
  - 📌 Title  
  - 👨‍🔬 Authors  
  - 📅 Date  
  - 📝 Abstract  
  - 🔗 Direct link to paper  

---

## ⚙️ Tech Stack
- **Python 3.9+**  
- [NiceGUI](https://nicegui.io) – UI framework  
- `requests` – HTTP requests  
- `beautifulsoup4` – parsing ArXiv API responses  
- **Cline AI** – VS Code AI agent for interactive development  

---

## 📦 Installation

```bash
git clone https://github.com/your-username/arxiv-research-bot.git
cd arxiv-research-bot
pip install -r requirements.txt
