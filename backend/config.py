import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    # Neo4j Database Configuration
    NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

    # OpenAI Configuration (optional, for RAG + LLM integration)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Meal Plan Configuration (example constraints)
    CONSTRAINTS = {
        "BREAKFAST": {
            "juice_restriction": "No visible pulp separation",
            "max_calories": 500
        },
        "LUNCH": {
            "max_calories": 800
        },
        "DINNER": {
            "max_calories": 700
        }
    }

    # Date Range for Meal Plan Generation
    DATE_RANGE = {
        "start_date": "2024-12-02",
        "end_date": "2024-12-15"
    }
