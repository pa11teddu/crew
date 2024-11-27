# AI-Powered Research and Writing Assistant

This project provides an AI-driven system for conducting research and writing engaging content on a given topic. It uses **Ollama OpenHermes**, OpenAI's ChatGPT, and DuckDuckGo Search, orchestrated through CrewAI for seamless task management.

## Features

- **Research Task**: Performs in-depth analysis of emerging trends and technologies.
- **Writing Task**: Generates insightful and engaging articles on a given topic.
- **DuckDuckGo Integration**: Uses web search to enhance research.
- **Locally Hosted Language Model**: Employs Ollama's OpenHermes for efficient NLP.
- **Task Automation**: Manages research and writing workflows through CrewAI.

## Prerequisites

### Required Packages

### Install Ollama
1. Install Ollama using Homebrew:
   ```bash
   brew install ollama
   ```

2. Pull the OpenHermes model:
   ```bash
   ollama pull openhermes
   ```

## Setup
1. Clone the repository
2. Create a `.env` file in the project root
3. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## How to Run
1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Run the script:
   ```bash
   python ai_bot.py
   ```

3. The script will:
   - Initialize the AI agents
   - Conduct research on the specified topic
   - Generate a detailed article
   - Save the output to `new-blog-post.md`

## Agent Roles

### Research Analyst
- Conducts comprehensive research on specified topics
- Analyzes trends and identifies key insights
- Provides structured research reports

### Tech Storyteller
- Transforms technical research into engaging narratives
- Ensures content accessibility while maintaining accuracy
- Produces markdown-formatted articles

## Output

The pipeline generates two main outputs:
1. A detailed research analysis
2. A polished article saved as `new-blog-post.md`
