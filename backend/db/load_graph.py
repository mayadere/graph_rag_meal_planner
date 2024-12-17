from neo4j import GraphDatabase
import pandas as pd

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "password")

def load_data_to_graph():
    driver = GraphDatabase.driver(URI, auth=AUTH)
    data = pd.read_csv("meal_data.csv")

    def create_graph(tx, recipe_id, recipe_name, meal_period, section, ingredient_name):
        query = (
            "MERGE (r:Recipe {id: $recipe_id, name: $recipe_name}) "
            "MERGE (m:MealPeriod {name: $meal_period}) "
            "MERGE (s:Section {name: $section}) "
            "MERGE (i:Ingredient {name: $ingredient_name}) "
            "MERGE (r)-[:BELONGS_TO]->(m) "
            "MERGE (r)-[:HAS_SECTION]->(s) "
            "MERGE (r)-[:REQUIRES]->(i)"
        )
        tx.run(query, recipe_id=recipe_id, recipe_name=recipe_name,
               meal_period=meal_period, section=section, ingredient_name=ingredient_name)

    with driver.session() as session:
        for _, row in data.iterrows():
            session.write_transaction(
                create_graph, row["Recipe ID"], row["Recipe Name"],
                row["Meal Period"], row["Section"], row["Ingredient Name"]
            )
    driver.close()

if __name__ == "__main__":
    load_data_to_graph()
