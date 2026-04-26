from config import NEO4J_CONFIG

from importer.neo4j_importer import (
    Neo4jImporter
)

from importer.schema_initializer import (
    create_indexes
)

from importer.label_manager import (
    remove_temp_labels
)


# =====================================
# CONNECT
# =====================================

importer = Neo4jImporter(
    **NEO4J_CONFIG
)


# =====================================
# IMPORT MOVIES
# =====================================

print("Import movies...")

importer.import_movies()


# =====================================
# IMPORT PEOPLES
# =====================================

print("Import peoples...")

importer.import_peoples()


# =====================================
# CREATE INDEXES
# =====================================

print("Create indexes...")

create_indexes(importer)


# =====================================
# IMPORT EDGES
# =====================================

print("Import edges...")

importer.import_edges()


# =====================================
# REMOVE TEMP LABELS
# =====================================

print("Remove temp labels...")

remove_temp_labels(importer)


# =====================================
# CLOSE
# =====================================

importer.close()


print("Import selesai")