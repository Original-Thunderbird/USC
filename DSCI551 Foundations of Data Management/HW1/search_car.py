import sys
import requests
import re

query_ls = re.sub(r'[^\w\s]', ' ', sys.argv[1]).lower().split()
id_ls = []
for query in query_ls:
    # print(query)
    response = requests.get('https://dsci551-85451-default-rtdb.firebaseio.com/inv_ind/' + query + '.json')
    # print(type(response))
    # print(response.json())
    if response.json() is not None:
        id_ls += response.json()
if len(id_ls) == 0:
    print("No cars found")
else:
    id_cnt = {}
    for id in id_ls:
        if id not in id_cnt.keys():
            id_cnt[id] = 0
        id_cnt[id] += 1
    # print(id_cnt)
    id_sorted = [k for k, v in sorted(id_cnt.items(), key=lambda item: item[1], reverse=True)]
    print(id_sorted)