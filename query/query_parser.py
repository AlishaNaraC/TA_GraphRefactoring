import re

class QueryParser:

    WHERE_PATTERN = re.compile(r'\bWHERE\b(.*?)(\bRETURN\b|$)', re.IGNORECASE | re.DOTALL)

    CONDITION_PATTERN = re.compile(
        r'(\w+)\.(\w+)\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|(\d+))',
        re.IGNORECASE
    )

    def extract_where_clause(self, query):
        match = self.WHERE_PATTERN.search(query)
        return match.group(1) if match else ""

    def extract_conditions(self, query):
        where_clause = self.extract_where_clause(query)
        matches = self.CONDITION_PATTERN.findall(where_clause)

        conditions = []

        for match in matches:
            conditions.append({
                "variable": match[0],
                "property": match[1],
                "value": match[2] or match[3] or match[4]
            })

        return conditions