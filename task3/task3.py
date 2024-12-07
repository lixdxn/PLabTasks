import json
import sys


def fill_values(tests, values):
    for test in tests:
        matching_value = None
        for value in values:
            if value['id'] == test['id']:
                matching_value = value['value']
                break
        if matching_value is not None:
            test['value'] = matching_value

        if 'values' in test:
            fill_values(test['values'], values)

def main():
    if len(sys.argv) != 4:
        print("usage: python3 task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]

    with open(values_file_path, 'r') as values_file:
        values_data = json.load(values_file)["values"]

    with open(tests_file_path, 'r') as tests_file:
        tests_data = json.load(tests_file)["tests"]

    fill_values(tests_data, values_data)

    with open(report_file_path, 'w') as report_file:
        json.dump({"tests": tests_data}, report_file, indent=4)

    print(f"Report has been written to {report_file_path}")

main()