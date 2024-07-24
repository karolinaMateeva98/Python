import requests
import numpy as np
import pandas as pd

# __define-ocg__: This script counts the number of items with age >= 50
'''
Python Age Counting In the Python file, write a program to perform a GET request on the route https://coderbyte.com/api/challenges/json/age-counting 
which contains a data key and the value is a string which contains items in the format: key=STRING, age=INTEGER. 
Your goal is to count how many items exist that have an age equal to or greater than 50, and print this final value.
'''

def count_items_with_age_above_50():
  url = 'https://coderbyte.com/api/challenges/json/age-counting'

  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    data_string = data.get("data", "")

    items = data_string.split(", ")

    varOcg = 0

    for item in items:
      if "age=" in item:
        key_value=item.split("age=")
        if len(key_value) > 1:
          age_str = key_value[1].strip()
          try:
            age = int(age_str)

            if age >= 50:
              varOcg += 1
          except ValueError:
            print("Invalid age value")

    print(varOcg)
  
  except requests.RequestException as e:
    print(f"An error occurred: {e}")


count_items_with_age_above_50()