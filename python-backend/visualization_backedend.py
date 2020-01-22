import regex as regex
from neo4j.v1 import GraphDatabase
import csv
import neo4j
from py2neo import cypher


def backend(path):
    uri = "bolt://localhost:7687"
    password = "neo4j"
    user = "neo4j"

        # connecting to server

    graphDB_driver = GraphDatabase.driver(uri, auth=(user, password))
    session = graphDB_driver.session()
        #session.run('create(:car {name: $vehicle})',vehicle="mercedes")

    with open(path, 'r') as file:
        reader = csv.DictReader(file,delimiter='|')
        print(*reader)
        keys = reader.fieldnames

        node = []
        created = []
        i = 0
        graph_db = neo4j.v1.GraphDatabase()
        for line in reader:
            for j in range(0, 2):
                if line[keys[j]] not in created:
                    session.run("CREATE ("+"neo"+regex.sub('[^A-Za-z0-9]+', '', line[keys[j]])+" :"+keys[j]+ "{ name: $name})",name=line[keys[j]])
                    created.append(line[keys[j]])
