from typing import List
from operator import itemgetter
from typing import TypedDict

import os
import time
import textwrap

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.responses import RedirectResponse
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag_chain import rag_chain

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Backend ai chat python",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Adds routes to the app for using the chain under:
# /invoke
# /batch
# /stream
add_routes(app, rag_chain, enable_feedback_endpoint=True)

#@app.get('/sse')
#async def stream():
#    return StreamingResponse(get_openai_generator(prompt), media_type='text/event-stream')

@app.get("/stream_log")
async def stream_log(question: str):
    async def event_generator():
        # Replace with your logic to generate responses
        #responses = ["Processing your question...", "Fetching data...", "Here is the answer to your question."]
        #for response in rag_chain.stream(question):
        #    yield f"data: {response}\n\n"
        #    time.sleep(1)  # Simulate delay
        response = await rag_chain.ainvoke(question)
        yield f"data: {response}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

class Message(BaseModel):
    content: str
    role: str

class RagInput(BaseModel):
    message: Message
    history: List[str]

@app.post('/')
async def invoke(query: RagInput):
    response = rag_chain.invoke(query.message.content)
    return {"data": response}

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=5000)

