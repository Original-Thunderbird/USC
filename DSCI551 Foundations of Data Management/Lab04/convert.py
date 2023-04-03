import json
import sys

def parseNum(str):
    if '.' not in str:
        return int(str)
    else:
        return float(str)

f = open(sys.argv[1])
data = json.load(f)
f.close()
res = {}
for k in data:
    #print(k, list(data[k].keys())[0], data[k])
    type = list(data[k].keys())[0]
    if type == 'L':
        ls = []
        for e in data[k]['L']:
            #print(list(e.values())[0])
            if list(e.keys())[0] == 'S':
                ls.append(list(e.values())[0])
            else:
                ls.append(parseNum(list(e.values())[0]))
        res[k] = ls
    elif type == 'N':
        res[k] = parseNum(data[k][list(data[k].keys())[0]])
    elif type == 'NS':
        ls = []
        for e in data[k]['NS']:
            ls.append(parseNum(e))
        res[k] = ls
    elif type == 'M':
        orig_map = data[k]['M']
        dense_map = {}
        #print(map)
        for mk in orig_map:
            #print(list(map[mk].keys())[0])
            if list(orig_map[mk].keys())[0] == 'N':
                dense_map[mk] = parseNum(orig_map[mk]['N'])
            else:
                dense_map[mk] = orig_map[mk]['S']
        res[k] = dense_map
    else:
        res[k] = data[k][type]

f = open(sys.argv[2], 'w')
f.write(json.dumps(res, indent=2))
f.close()