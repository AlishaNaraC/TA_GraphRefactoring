from config import *
from refactor.property_becoming_node import PropertyBecomingNode
from refactor.edge_specification import EdgeSpecification

class RefactorManager:

    def run_pbn_refactor(self, properties):

        refactor = PropertyBecomingNode(
            NEO4J_URI,
            NEO4J_USER,
            NEO4J_PASSWORD,
            PBN_DB
        )

        refactor.refactor_properties(properties)

        refactor.close()

    def run_es_refactor(self, rel_type, properties):

        refactor = EdgeSpecification(
            NEO4J_URI,
            NEO4J_USER,
            NEO4J_PASSWORD,
            ES_DB
        )

        refactor.specialize_relationships(
            rel_type,
            properties
        )

        refactor.close()