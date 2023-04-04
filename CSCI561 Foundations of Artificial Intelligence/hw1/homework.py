from collections import deque
import heapq

class Solution:
    def __init__(self, file: str) -> None:
        input = open(file, 'r')
        self.method = input.readline()[:-1]
        col, row = input.readline().split()
        col, row = int(col), int(row)
        startJ, startI = input.readline().split()
        self.startJ, self.startI = int(startJ), int(startI)
        self.stamina = int(input.readline())
        lodegNum = int(input.readline())
        self.lodges = []
        for _ in range(lodegNum):
            lodgeJ, lodgeI = input.readline().split()
            self.lodges.append((int(lodgeI), int(lodgeJ)))
        # print(lodges)
        self.mesh = []
        for _ in range(row):
            eLs = input.readline().split()
            self.mesh.append([int(e) for e in eLs])
        # print(mesh)
        input.close()
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        
    def computePath(self) -> list:
        if self.method == 'A*':
            print('A*')
            resLs = AStar().findWay(self.startI, self.startJ, self.stamina, self.lodges, self.mesh, self.dirs)
        elif self.method == 'UCS':
            print('UCS')
            resLs = UniformCost().findWay(self.startI, self.startJ, self.stamina, self.lodges, self.mesh, self.dirs)
        else:
            print('BFS')
            resLs = BreadthFirst().findWay(self.startI, self.startJ, self.stamina, self.lodges, self.mesh, self.dirs)
        return resLs

    def writeFile(self, resLs: list, file: str):
        output = open(file, 'w')
        for res in resLs:
            if res == None:
                output.write('FAIL\n')
            else:
                output.write(' '.join([str(x[1])+','+str(x[0]) for x in res]) + '\n')
        output.close()



class BreadthFirst:
    def trackPath(self, parent: list, curPos: tuple) -> list:
        res = []
        while parent[curPos[0]][curPos[1]] != curPos:
            res.append(curPos)
            curPos = parent[curPos[0]][curPos[1]]
        res.append(curPos)
        res.reverse()
        return res

    def findWay(self, startI: int, startJ: int, stamina: int, lodges: list, mesh: list, dirs: list) -> list:
        lodgesIndMap = {}
        for i in range(len(lodges)):
            lodgesIndMap[lodges[i]] = i
        reached = 0
        # elems in deq: (i, j)
        deq = deque()
        deq.append((startI, startJ))
        row, col = len(mesh), len(mesh[0])
        resLs = [None for _ in range(len(lodges))]
        # elems in parent: (i, j)
        # print('startI:', startI, ' startJ:', startJ, ' row:', row, ' col:', col)
        parent = [[None for _ in range(col)] for _ in range(row)]
        parent[startI][startJ] = (startI, startJ)
        
        while reached < len(lodges) and len(deq) > 0:
            curPos = deq.popleft()
            if curPos in lodgesIndMap:
                resLs[lodgesIndMap[curPos]] = self.trackPath(parent, curPos)
                reached += 1
            for dir in dirs:
                newI, newJ = curPos[0] + dir[0], curPos[1] + dir[1]
                # invalid/duplicate move
                if newI < 0 or newI >= row or newJ < 0 or newJ >= col:
                    continue
                # mesh[newI][newJ] < 0: tree / mesh[newI][newJ] > 0: ground
                if (mesh[newI][newJ] < 0 and abs(mesh[curPos[0]][curPos[1]]) < -mesh[newI][newJ]) or (mesh[newI][newJ] > 0 and abs(mesh[curPos[0]][curPos[1]])+stamina < mesh[newI][newJ]):
                    continue
                # visited
                if parent[newI][newJ] != None:
                    continue
                parent[newI][newJ] = curPos
                deq.append((newI, newJ))
        return resLs



class UniformCost:
    class Node:
        def __init__(self, curPos: tuple, cost: int) -> None:
            self.curPos = curPos
            self.cost = cost
        def __gt__(self, o: object) -> bool:
            return self.cost > o.cost
        def __ge__(self, o: object) -> bool:
            return self.cost >= o.cost
        def __eq__(self, o: object) -> bool:
            return self.cost == o.cost
        def __le__(self, o: object) -> bool:
            return self.cost <= o.cost
        def __lt__(self, o: object) -> bool:
            return self.cost < o.cost
    
    def trackPath(self, parent: list, curPos: tuple) -> list:
        res = []
        while parent[curPos[0]][curPos[1]] != curPos:
            res.append(curPos)
            curPos = parent[curPos[0]][curPos[1]]
        res.append(curPos)
        res.reverse()
        return res
    
    def findWay(self, startI: int, startJ: int, stamina: int, lodges: list, mesh: list, dirs: list) -> list:
        lodgesIndMap = {}
        for i in range(len(lodges)):
            lodgesIndMap[lodges[i]] = i
        reached = 0
        # elems in priorq: (i, j)
        priorq = []
        heapq.heapify(priorq)
        heapq.heappush(priorq, self.Node((startI, startJ), 0))
        row, col = len(mesh), len(mesh[0])
        resLs = [None for _ in range(len(lodges))]
        cost = [None for _ in range(len(lodges))]
        # elems in parent: (i, j)
        parent = [[None for _ in range(col)] for _ in range(row)]
        parent[startI][startJ] = (startI, startJ)
        dist = [[float('inf') for _ in range(col)] for _ in range(row)]
        dist[startI][startJ] = 0

        while reached < len(lodges) and len(priorq) > 0:
            curNode = heapq.heappop(priorq)
            if dist[curNode.curPos[0]][curNode.curPos[1]] < curNode.cost:
                continue
            if curNode.curPos in lodgesIndMap:
                resLs[lodgesIndMap[curNode.curPos]] = self.trackPath(parent, curNode.curPos)
                cost[lodgesIndMap[curNode.curPos]] = dist[curNode.curPos[0]][curNode.curPos[1]]
                reached += 1
            for dir in dirs:
                newI, newJ = curNode.curPos[0] + dir[0], curNode.curPos[1] + dir[1]
                # invalid/duplicate move
                if newI < 0 or newI >= row or newJ < 0 or newJ >= col:
                    continue
                # mesh[newI][newJ] < 0: tree / mesh[newI][newJ] > 0: ground
                if (mesh[newI][newJ] < 0 and abs(mesh[curNode.curPos[0]][curNode.curPos[1]]) < -mesh[newI][newJ]) or (mesh[newI][newJ] > 0 and abs(mesh[curNode.curPos[0]][curNode.curPos[1]])+stamina < mesh[newI][newJ]):
                    continue
                newCost = dist[curNode.curPos[0]][curNode.curPos[1]] + (14 if dir[0]*dir[1] != 0 else 10)
                if newCost < dist[newI][newJ]:
                    dist[newI][newJ] = newCost
                    parent[newI][newJ] = curNode.curPos
                    heapq.heappush(priorq, self.Node((newI, newJ), newCost))
        print(cost)
        return resLs



class AStar():
    # Node: (f: int, curPos: tuple, momentum: int, g: int, h: int, parent: Node*)
    def trackPath(self, node: tuple) -> list:
        res = []
        while node[5] != None:
            res.append(node[1])
            node = node[5]
        res.append(node[1])
        res.reverse()
        return res

    def findWay(self, startI: int, startJ: int, stamina: int, lodges: list, mesh: list, dirs: list) -> list:
        resLs = []
        row, col = len(mesh), len(mesh[0])
        for lodge in lodges:
            found = False
            # costMap: {node: {momentum: min cost}} i.e. for each node, larger momentum is needed to reach more neighbors
            costMap = {}
            costMap[(startI, startJ)] = {0: 0}
            priorq = []
            heapq.heapify(priorq)
            diffI, diffJ = abs(startI-lodge[0]), abs(startJ-lodge[1])
            diagLen, orthLen = min(diffI, diffJ), max(diffI, diffJ)-min(diffI, diffJ)
            initEst = diagLen*14 + orthLen*10
            heapq.heappush(priorq, (initEst, (startI, startJ), 0, 0, initEst, None))
            while len(priorq) != 0:
                curNode = heapq.heappop(priorq)
                curPos = curNode[1]
                if curPos == (62, 33):
                    1+1
                curMomentum = curNode[2]
                if curPos == lodge:
                    print(curNode[0])
                    resLs.append(self.trackPath(curNode))
                    found = True
                    break
                for dir in dirs:
                    newI, newJ = curPos[0] + dir[0], curPos[1] + dir[1]
                    # invalid/duplicate move
                    if newI < 0 or newI >= row or newJ < 0 or newJ >= col:
                        continue
                    if (mesh[newI][newJ] < 0 and abs(mesh[curPos[0]][curPos[1]]) < -mesh[newI][newJ]) or (mesh[newI][newJ] > 0 and abs(mesh[curPos[0]][curPos[1]]) + stamina + curMomentum < mesh[newI][newJ]):
                        continue
                    elev = max(0, abs(mesh[newI][newJ]) - abs(mesh[curPos[0]][curPos[1]]) - curMomentum)
                    newCost = costMap[curPos][curMomentum] + (14 if dir[0]*dir[1] != 0 else 10) + elev
                    newMomentum = max(0, abs(mesh[curPos[0]][curPos[1]]) - abs(mesh[newI][newJ]))
                    # a visited node, cost not decreasing, not discovering new path
                    if (newI, newJ) in costMap and newMomentum in costMap[(newI, newJ)] and newCost >= costMap[(newI, newJ)][newMomentum]:
                        continue
                    if (newI, newJ) not in costMap:
                        costMap[(newI, newJ)] = {newMomentum: newCost}
                    elif newMomentum not in costMap[(newI, newJ)] or newCost < costMap[(newI, newJ)][newMomentum]:
                        costMap[(newI, newJ)][newMomentum] = newCost
                    diffI, diffJ = abs(newI-lodge[0]), abs(newJ-lodge[1])
                    diagLen, orthLen = min(diffI, diffJ), max(diffI, diffJ)-min(diffI, diffJ)
                    newEst = diagLen*14 + orthLen*10
                    newNode = (newCost+newEst, (newI, newJ), newMomentum, newCost, newEst, curNode)
                    heapq.heappush(priorq, newNode)
            if found == False:
                resLs.append(None)
        return resLs


# sol = Solution('input.txt')
# resLs = sol.computePath()
# sol.writeFile(resLs, 'output.txt')