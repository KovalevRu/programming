from fastapi import FastAPI
from database import engine
import models
from routers import teams, players

app = FastAPI()

app.include_router(teams.router)
app.include_router(players.router)
@app.get("/")
def root():
    return {"message": "Basketball API"}