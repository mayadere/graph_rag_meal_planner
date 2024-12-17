from fastapi import FastAPI, Query
from models.schema import MealPlanRequest, MealPlanResponse, HealthCheckResponse
from rag_pipeline import generate_meal_plan

app = FastAPI()

@app.get("/api/generate-meal-plan", response_model=MealPlanResponse)
def get_meal_plan(constraint: str = Query(..., description="Dietary constraint")):
    """
    Endpoint to generate a meal plan based on a dietary constraint.
    """
    meal_plan_text = generate_meal_plan(constraint)
    return MealPlanResponse(meal_plan=meal_plan_text)

@app.get("/health", response_model=HealthCheckResponse)
def health_check():
    """
    Health check endpoint to verify API status.
    """
    return HealthCheckResponse(status="OK")
