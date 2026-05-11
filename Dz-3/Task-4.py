import json

def get_raw_report():
    return {
        "income": 10000,
        "expenses": 7000,
        "net_profit": 3000,
        "currency": "USD"
    }

# Decorator to convert raw report to a formatted statistics report
def to_statistics(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        currency = report.get("currency", "")
        result = "Report:"
        for key, value in report.items():
            if key != "currency":
                result += f"\n{key.capitalize()} = {value} {currency}"
        return result
    return wrapper

# Decorator to convert raw report to JSON format
def to_json(func):
    def wrapper(*args, **kwargs):
        report = func(*args, **kwargs)
        return json.dumps(report, indent=4)
    return wrapper

@to_statistics
def get_statistics_report():
    return get_raw_report()

@to_json
def get_json_report():
    return get_raw_report()

print()
print(get_raw_report())

print()
print(get_statistics_report())

print()
print(get_json_report())