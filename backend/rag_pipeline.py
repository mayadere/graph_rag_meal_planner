from neo4j_connector import Neo4jConnector
import openai
from config import OPENAI_API_KEY

def generate_meal_plan(constraint: str):
    neo4j = Neo4jConnector("bolt://localhost:7687", "neo4j", "password")
    recipes = neo4j.find_recipes(constraint)
    neo4j.close()

    # Build LLM prompt
    prompt = "Generate a 14-day meal plan based on the following recipes:\n"
    for r in recipes:
        prompt += f"- {r['Recipe']}: Ingredients {r['Ingredients']}\n"
    prompt += "\nInclude constraints: No visible pulp separation in Juice for breakfast.\n"

    # Call OpenAI API
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
