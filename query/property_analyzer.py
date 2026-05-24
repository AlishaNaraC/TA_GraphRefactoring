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

    def save_report_to_csv(self, report, csv_path):
        import csv
        # Tentukan header CSV
        headers = [
            "property",
            "total_redundancy",
            "most_called_value",
            "value_redundancy",
            "is_redundant",
            "redundant_values"
        ]
        with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in report:
                # redundant_values disimpan sebagai string
                row_copy = row.copy()
                row_copy["redundant_values"] = str(row_copy["redundant_values"])
                writer.writerow(row_copy)

    def generate_report(self, property_counter, value_counter):
        report = []

        for prop in property_counter:
            # Cek apakah semua value unik (tidak ada redundansi)
            value_counts = value_counter[prop]
            if all(cnt == 1 for cnt in value_counts.values()):
                most_common_value = None
                most_common_count = 0
                redundant_values = []
                is_redundant = False
            else:
                most_common_value, most_common_count = value_counts.most_common(1)[0]
                redundant_values = [
                    {"value": val, "count": cnt}
                    for val, cnt in value_counts.items()
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