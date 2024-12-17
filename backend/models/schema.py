from pydantic import BaseModel, Field
from typing import List, Optional

# Input schema for dietary constraint
class MealPlanRequest(BaseModel):
    constraint: str = Field(..., example="Vegetarian", description="Dietary constraint for the meal plan")

# Output schema for individual recipes
class Recipe(BaseModel):
    name: str = Field(..., example="Tofu Stir Fry", description="Name of the recipe")
    ingredients: List[str] = Field(..., example=["Tofu", "Soy Sauce", "Broccoli"], description="List of ingredients")

# Output schema for the full meal plan
class MealPlanResponse(BaseModel):
    meal_plan: str = Field(
        ...,
        example="Day 1: Tofu Stir Fry for lunch. Day 2: Veggie Wrap for dinner.",
        description="Generated meal plan based on dietary constraints"
    )

# Output schema for graph query results (optional)
class GraphRecipeResult(BaseModel):
    recipe_name: str = Field(..., example="Tofu Stir Fry", description="Name of the recipe")
    ingredients: List[str] = Field(..., example=["Tofu", "Soy Sauce"], description="Ingredients used in the recipe")

# Optional health check response
class HealthCheckResponse(BaseModel):
    status: str = Field(..., example="OK", description="API health status")
