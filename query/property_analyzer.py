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


            most_common_value, most_common_count = value_counter[prop].most_common(1)[0]
            # Ambil redundant_values, tapi exclude most_common_value
            redundant_values = [
                {"value": val, "count": cnt}
                for val, cnt in value_counter[prop].items()
                if cnt > 1 and val != most_common_value
            ]
            redundant_values.sort(key=lambda x: x["count"], reverse=True)
            is_redundant = (most_common_count > 1) or (len(redundant_values) > 0)

            report.append({
                "property": prop,
                "total_redundancy": property_counter[prop],
                "most_called_value": most_common_value,
                "value_redundancy": most_common_count,
                "is_redundant": is_redundant,
                "redundant_values": redundant_values
            })

        return report