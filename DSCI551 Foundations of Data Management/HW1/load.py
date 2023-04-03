import sys
import requests
import json
import pandas as pd

url = 'https://dsci551-85451-default-rtdb.firebaseio.com/cars.json'


df = pd.read_csv(sys.argv[1])
json = df.to_json(orient='records')
resp = requests.put(url, json)