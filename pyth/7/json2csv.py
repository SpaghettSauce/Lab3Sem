import json
import csv
import sys
import os

def json_to_csv(input_json_file):
    
    if not os.path.exists(input_json_file):
        print(f"Error: The JSON file '{input_json_file}' does not exist.")
        return

    
    base_name = os.path.splitext(os.path.basename(input_json_file))[0]
    output_csv_file = f"{base_name}.csv"

    try:
        with open(input_json_file, 'r') as json_file:
            data = json.load(json_file)

        with open(output_csv_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            
            header = data[0].keys()
            csv_writer.writerow(header)

           
            for item in data:
                csv_writer.writerow(item.values())

        print(f"Converted '{input_json_file}' в '{output_csv_file}'.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "main":
    if len(sys.argv) != 2:
        print("Usage: python json2csv.py <input_json_file>")
    else:
        input_json_file = sys.argv[1]
        json_to_csv(input_json_file)