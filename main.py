from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import subprocess
import time

app = FastAPI()

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Launch the Vite development server in middleware mode
@app.on_event("startup")
async def start_vite():
    # Start the Vite process (runs vite in middleware mode)
    vite_process = subprocess.Popen(
        ["vite", "--port", "3000"], cwd="./"
    )
    time.sleep(3)  # Wait for Vite to boot up

@app.get("/")
async def serve_vite():
    # Serve the index.html from Vite server
    return HTMLResponse(content="<!DOCTYPE html><html><body><script type='module' src='http://localhost:3000/src/main.js'></script></body></html>", status_code=200)

