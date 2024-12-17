from neo4j import GraphDatabase

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def find_recipes(self, dietary_constraint):
        query = (
            "MATCH (r:Recipe)-[:REQUIRES]->(i:Ingredient) "
            "WHERE i.name CONTAINS $dietary_constraint "
            "RETURN r.name AS Recipe, collect(i.name) AS Ingredients"
        )
        with self.driver.session() as session:
            results = session.run(query, dietary_constraint=dietary_constraint)
            return [record for record in results]

# Example usage
# neo4j = Neo4jConnector("bolt://localhost:7687", "neo4j", "password")
# print(neo4j.find_recipes("Soy"))
# neo4j.close()
