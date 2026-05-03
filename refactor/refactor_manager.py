from config import *

from refactor.db_cloner import DBCloner
from refactor.property_becoming_node import PropertyBecomingNode
from refactor.edge_specification import EdgeSpecification

class RefactorManager:

    def __init__(self):
        self.cloner = DBCloner(NEO4J_CONFIG)

    def create_pbn_database(self):

        print("Cloning baseline -> PBN")

        self.cloner.clone_database(
            BASELINE_DB,
            PBN_DB
        )

    def create_es_database(self):

        print("Cloning baseline -> ES")

        self.cloner.clone_database(
            BASELINE_DB,
            ES_DB
        )

    def run_pbn_refactor(self, properties):

        refactor = PropertyBecomingNode(NEO4J_CONFIG, database=PBN_DB)

        refactor.refactor_properties(properties)

        refactor.close()

    def run_es_refactor(self, rel_type, properties):

        refactor = EdgeSpecification(NEO4J_CONFIG, database=ES_DB)

        refactor.specialize_relationships(
            rel_type,
            properties
        )

        refactor.close()