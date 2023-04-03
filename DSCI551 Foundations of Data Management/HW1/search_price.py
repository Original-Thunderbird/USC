import sys
import requests

url = 'https://dsci551-85451-default-rtdb.firebaseio.com/cars.json'

response = requests.get(url + '?orderBy="price"&startAt=' + sys.argv[1] + '&endAt=' + sys.argv[2])
d = response.json()
if bool(d) == False:
    print("No cars found with the given range")
else:
    id_arr = []
    for ind in d:
        id_arr.append(d[ind]['car_ID'])
    print(id_arr)