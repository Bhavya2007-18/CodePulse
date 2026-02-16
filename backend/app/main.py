# Entry point of FastAPI app.
#Creates FastAPI instance
#Includes all route files
#Handles CORS
#Starts server
#This file should stay small.

from fastapi import FastAPI # creates backend application

app = FastAPI()

@app.get("/")  # route decorator
def root():
    return {"message": "CodePulse backend is running successfully"}

