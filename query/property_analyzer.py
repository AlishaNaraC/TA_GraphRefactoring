from collections import Counter, defaultdict

class PropertyAnalyzer:

    def analyze(self, conditions):
        property_counter = Counter()
        value_counter = defaultdict(Counter)

        for item in conditions:
            prop = item["property"]
            value = item["value"]

            property_counter[prop] += 1
            value_counter[prop][value] += 1

        return property_counter, value_counter

    def generate_report(self, property_counter, value_counter):
        report = []

        for prop in property_counter:
            value, count = value_counter[prop].most_common(1)[0]
            is_redundant = count > 1

            report.append({
                "property": prop,
                "total_redundancy": property_counter[prop],
                "most_called_value": value,
                "value_redundancy": count,
                "is_redundant": is_redundant
            })

        return report