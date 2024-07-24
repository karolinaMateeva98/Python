'''
Python CSV to JSON In the Python file, you have a program that performs a GET request on the route
https://coderbyte.com/api/challenges/logs/user-info-csv and then sort the CSV data by the second column. 
Finally, convert the sorted CSV data to a JSON object and print it. Be sure to call json.dumps on the final object. 
Example Input: name,email,phone John Doe,johndoe@example.com,555-1234 Jane Smith,janesmith@example.com,555-5678 
Example Output: [{"name":"John Doe","email":"johndoe@example.com","phone":"555-1234"},{"name":"Jane Smith","email":"janesmith@example.com","phone":"555-5678"}] 
'''

import requests
import csv
import json
from io import StringIO

# __define-ocg__: This script sorts CSV data by the second column and converts data to JSON

def csv_to_json_sorted():
  url = "https://coderbyte.com/api/challenges/logs/user-info-csv"

  try:
    response = requests.get(url)
    response.raise_for_status()

    csv_data = response.text
    # print(csv_data)
    csv_reader = csv.reader(StringIO(csv_data))

    header = next(csv_reader)
    rows = list(csv_reader)
    # print(header)
    # print(rows)
    sorted_rows = sorted(rows, key=lambda row: row[1]) 
    # print(sorted_rows)

    json_data = [dict(zip(header,row)) for row in sorted_rows]

    varOcg = json.dumps(json_data, indent=2)
    print(varOcg)

  except requests.RequestException as e:
    print(f"An error occurred: {e}")

csv_to_json_sorted()