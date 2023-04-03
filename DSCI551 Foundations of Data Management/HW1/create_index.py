import sys
import requests
import json
import pandas as pd
import re

url = 'https://dsci551-85451-default-rtdb.firebaseio.com/cars.json'

df = pd.read_csv(sys.argv[1])[["car_ID", "CarName"]]

inv_ind = {}
for car in df.values:
    words = re.sub(r'[^\w\s]', ' ', car[1]).lower().split()
    for word in words:
        if word not in inv_ind.keys():
            inv_ind[word] = []
        inv_ind[word].append(car[0])
for key in inv_ind.keys():
    inv_ind[key] = list(set(inv_ind[key]))

requests.put('https://dsci551-85451-default-rtdb.firebaseio.com/inv_ind.json', json.dumps(inv_ind))