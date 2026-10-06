from fastapi import FastAPI
from anthropic import Anthropic

app = FastAPI()
client = Anthropic()

DOCS = """
# Service Architecture
- **API Gateway**: Routes all requests, handles auth
- **Worker Pool**: Processes async tasks
- **Cache Layer**: Redis for hot data
- **Database**: PostgreSQL for persistence
"""

def answer_docs_question(question: str) -> dict:
    """Answer questions about codebase docs using Claude."""
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        system=f"You are a helpful assistant answering questions about this codebase.\n\nDocumentation:\n{DOCS}",
        messages=[{"role": "user", "content": question}]
    )
    answer = response.content[0].text
    return {
        "question": question,
        "answer": answer,
        "source": "Service Architecture docs"
    }

@app.post("/ask")
def ask(question: str):
    return answer_docs_question(question)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
