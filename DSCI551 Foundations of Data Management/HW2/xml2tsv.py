from lxml import etree
import datetime
import pandas
import sys

root_id = 0
tree = etree.parse(sys.argv[1])
record_dict = {}
record_ls = []
dependencies = {}

find_node_ls = etree.XPath("//inode")
node_find_id = etree.XPath("id/text()")
node_find_type = etree.XPath("type/text()")
node_find_name = etree.XPath("name/text()")
node_find_mtime = etree.XPath("mtime/text()")
node_find_perm = etree.XPath("permission/text()")
blocks_find_size = etree.XPath("blocks/block/numBytes/text()")
find_dep_ls = etree.XPath("//directory")
dep_find_parent = etree.XPath("parent/text()")
dep_find_child = etree.XPath("child/text()")

nodes = find_node_ls(tree)
deps = find_dep_ls(tree)

for node in nodes:
    id = int(node_find_id(node)[0])
    type = 'd' if node_find_type(node)[0] == 'DIRECTORY' else '-'
    name = node_find_name(node)
    if len(name) == 0:
        root_id = id
    [date, time] = datetime.datetime.utcfromtimestamp(int(node_find_mtime(node)[0])/1000).strftime('%Y-%m-%d %H:%M').split()
    [y, m, d] = date.split('-')
    if m[0] == '0':
        m = m[1:]
    if d[0] == '0':
        d = d[1:]
    if time[0] == '0':
        time = time[1:]
    tstr = '{}/{}/{} {}'.format(m, d, y, time)
    perm = node_find_perm(node)[0].split(':')[2]
    for ind in range(1,4):
        d = int(perm[ind])
        type += 'r' if d&4 else '-'
        type += 'w' if d&2 else '-'
        type += 'x' if d&1 else '-' 
    size_ls = [int(size) for size in blocks_find_size(node)]
    record_dict[id] = {'Path': '', 'name': '' if len(name) == 0 else name[0], 'ModificationTime': tstr, 'BlocksCount': len(size_ls), 'FileSize': sum(size_ls), 'Permission': type}

for dep in deps:
    parent = int(dep_find_parent(dep)[0])
    childs = sorted([int(child) for child in dep_find_child(dep)])
    dependencies[parent] = childs

def dfs(path, id):
    rec = record_dict[id]
    rec['Path'] = path + ('' if path == '/' else '/') + rec['name']
    rec.pop('name')
    record_ls.append(rec)
    if id in dependencies.keys():
        childs = dependencies[id]
        for child in childs:
            dfs(rec['Path'], child)
dfs('', root_id)

# df = pandas.DataFrame.from_records(record_ls)
f = open(sys.argv[2], "w")
f.write('Path\tModificationTime\tBlocksCount\tFileSize\tPermission\n')
for record in record_ls:
    f.write('{}\t{}\t{}\t{}\t{}\n'.format(record['Path'], record['ModificationTime'], record['BlocksCount'], record['FileSize'], record['Permission']))
f.close()





