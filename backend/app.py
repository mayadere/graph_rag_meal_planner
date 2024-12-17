from fastapi import FastAPI, Query
from rag_pipeline import generate_meal_plan

app = FastAPI()

@app.get("/api/generate-meal-plan")
def get_meal_plan(constraint: str = Query("Vegetarian")):
    result = generate_meal_plan(constraint)
    return {"meal_plan": result}
