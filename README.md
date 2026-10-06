# LLM-Powered Developer Tool

Answers questions about codebase documentation using Claude API. Demonstrates retrieval over docs with cited source passages.

## Setup
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=<your-key>
python app.py
```

## Features
- Query docs via FastAPI backend
- Claude-powered retrieval and answering
- Cites source passages
- Simple HTML frontend

## Testing
- Health check: `GET /health`
- Ask question: `POST /ask?question=What%20is%20the%20cache%20layer`
