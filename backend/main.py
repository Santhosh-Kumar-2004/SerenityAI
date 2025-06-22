# main.py

from fastapi import FastAPI
from routes import chat, affirmation, motivate, tip
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS settings if needed for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chat.router)
app.include_router(affirmation.router)
app.include_router(motivate.router)
app.include_router(tip.router)

#Sample ROute for Testing   
@app.get("/")
def root():
    return {"message": "SerenityAI backend is running"}
