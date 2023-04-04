from homework import Solution

sample = [15]
BFSLs = [1, 2, 3, 8, 9, 12]
UCSLs = [4, 10, 16]
AStarLs = [5, 6, 7, 11, 13, 14, 15]

for i in sample:
    inp = 'input\input'+str(i)+'.txt'
    sol = Solution(inp)
    resLs = sol.computePath()
    sol.writeFile(resLs, 'output/output' + str(i) + '.txt')
