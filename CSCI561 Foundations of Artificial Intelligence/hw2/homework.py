from copy import deepcopy
import numpy as np
import time

dirs = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
boardSize = 19
globDepth = 3
initBoard = None

class Board:
  def __init__(self, board, capW: int, capB: int) -> None:
    self.board, self.capW, self.capB = board, capW, capB
    self.countW = (self.board == 'w').sum()
    self.countB = (self.board == 'b').sum()
    self.moveW, self.moveB = None, None


  def getCandMoves(self) -> set:
    res = set()
    for i in range(boardSize):
      for j in range(boardSize):
        if self.board[i][j] != '.':
          for dir in dirs:
            newI1, newJ1 = i+dir[0], j+dir[1]
            if newI1 > -1 and newI1 < boardSize and newJ1 > -1 and newJ1 < boardSize:
              if self.board[newI1][newJ1] == '.':
                res.add((newI1, newJ1))
              newI2, newJ2 = newI1+dir[0], newJ1+dir[0]
              if newI2 > -1 and newI2 < boardSize and newJ2 > -1 and newJ2 < boardSize and self.board[newI2][newJ2] == '.':
                res.add((newI2, newJ2))
    return res
  

  def makeMove(self, move: tuple, role: str) -> None:
    self.board[move[0]][move[1]] = role
    if role == 'b':
      self.countB += 1
      self.moveB = move
    else:
      self.countW += 1
      self.moveW = move
    oppRole = 'w' if role == 'b' else 'b'
    # (-1, 0)
    if move[0]-3 > -1 and self.board[move[0]-3][move[1]] == role and self.board[move[0]-2][move[1]] == oppRole and self.board[move[0]-1][move[1]] == oppRole: 
      self.board[move[0]-2][move[1]] = '.'
      self.board[move[0]-1][move[1]] = '.'
      self.captureOpponent(role)
    # (-1, 1)
    if move[0]-3 > -1 and move[1]+3 < 19 and self.board[move[0]-3][move[1]+3] == role and self.board[move[0]-2][move[1]+2] == oppRole and self.board[move[0]-1][move[1]+1] == oppRole:
      self.board[move[0]-2][move[1]+2] = '.'
      self.board[move[0]-1][move[1]+1] = '.'
      self.captureOpponent(role)
    # (0, 1)
    if move[1]+3 < 19 and self.board[move[0]][move[1]+3] == role and self.board[move[0]][move[1]+2] == oppRole and self.board[move[0]][move[1]+1] == oppRole:
      self.board[move[0]][move[1]+2] = '.'
      self.board[move[0]][move[1]+1] = '.'
      self.captureOpponent(role)
    # (1, 1)
    if move[0]+3 < 19 and move[1]+3 < 19 and self.board[move[0]+3][move[1]+3] == role and self.board[move[0]+2][move[1]+2] == oppRole and self.board[move[0]+1][move[1]+1] == oppRole:
      self.board[move[0]+2][move[1]+2] == '.'
      self.board[move[0]+1][move[1]+1] == '.'
      self.captureOpponent(role)
    # (1, 0)
    if move[0]+3 < 19 and self.board[move[0]+3][move[1]] == role and self.board[move[0]+2][move[1]] == oppRole and self.board[move[0]+1][move[1]] == oppRole:
      self.board[move[0]+2][move[1]] == '.'
      self.board[move[0]+1][move[1]] == '.'
      self.captureOpponent(role)
    # (1, -1)
    if move[0]+3 < 19 and move[1]-3 > -1 and self.board[move[0]+3][move[1]-3] == role and self.board[move[0]+2][move[1]-2] == oppRole and self.board[move[0]+1][move[1]-1] == oppRole:
      self.board[move[0]+2][move[1]-2] == '.'
      self.board[move[0]+1][move[1]-1] == '.'
      self.captureOpponent(role)
    # (0, -1)
    if move[1]-3 > -1 and self.board[move[0]][move[1]-3] == role and self.board[move[0]][move[1]-2] == oppRole and self.board[move[0]][move[1]-1] == oppRole:
      self.board[move[0]][move[1]-2] = '.'
      self.board[move[0]][move[1]-1] = '.'
      self.captureOpponent(role)
    # (-1, -1)
    if move[0]-3 > -1 and move[1]-3 > -1 and self.board[move[0]-3][move[1]-3] == role and self.board[move[0]-2][move[1]-2] == oppRole and self.board[move[0]-1][move[1]-1] == oppRole:
      self.board[move[0]-2][move[1]-2] == '.'
      self.board[move[0]-1][move[1]-1] == '.'
      self.captureOpponent(role)
  

  def captureOpponent(self, role: str) -> None:
    if role == 'b':
      self.capB += 2
      self.countW -= 2
    else:
      self.capW += 2
      self.countB -= 2


def readBoard(file: str):
  input = open(file, 'r')
  role = 'b' if input.readline() == 'BLACK\n' else 'w'
  remTime = float(input.readline())
  capW, capB = input.readline().split(',')
  capW, capB = int(capW), int(capB)
  board = []
  for _ in range(boardSize):
    board.append([*input.readline()[:-1]])
  initBoard = Board(np.array(board), capW, capB)
  return initBoard, remTime, role


def writeRes(file: str, coord: tuple) -> None:
  output = open(file, 'w')
  ordA = ord('A')
  output.write(str(19-coord[0]) + (chr(ordA+coord[1]) if coord[1] < 8 else chr(ordA+coord[1]+1)))
  output.close()


def KMPSearch(pat, txt) -> list:
    M = len(pat)
    N = len(txt)
    res = []
 
    lps = [0]*M
    j = 0  # index for pat[]
    computeLPSArray(pat, M, lps)
    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            # print("Found pattern at index " + str(i-j))
            res.append(i-j)
            j = lps[j-1]
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res


def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
    lps[0] = 0 # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1


def isLeafState(state: Board, role: str) -> bool:
  if state.capB >= 10 or state.capW >= 10:
    return True
  pat5 = 'wwwww' if role == 'w' else 'bbbbb'
  live4 = '.wwww.' if role == 'w' else '.bbbb.'
  move = (state.moveW if role == 'w' else state.moveB)
  # horizonal
  if len(KMPSearch(pat5, state.board[move[0]])) != 0 or len(KMPSearch(live4, state.board[move[1]])) != 0:
    return True
  # vertical
  if len(KMPSearch(pat5, state.board[:, move[1]])) != 0 or len(KMPSearch(live4, state.board[:, move[1]])) != 0:
    return True
  
  # diag main
  # top-left
  dMain = []
  i = 1
  while move[0]-i > -1 and move[1]-i > -1:
    dMain.append(state.board[move[0]-i][move[1]-i])
    i += 1
  dMain.reverse()
  dMain.append(state.board[move[0]][move[1]])
  # bottom-right
  i = 1
  while move[0]+i < boardSize and move[1]+i < boardSize:
    dMain.append(state.board[move[0]+i][move[1]+i])
    i += 1
  if len(KMPSearch(pat5, dMain)) != 0 or len(KMPSearch(live4, dMain)) != 0:
    return True
  
  # diag sub
  dSub = []
  # top-right
  i = 1
  while move[0]-i > -1 and move[1]+i < boardSize:
    dSub.append(state.board[move[0]-i][move[1]+i])
    i += 1
  dSub.reverse()
  dSub.append(state.board[move[0]][move[1]])
  # bottom-left
  i = 1
  while move[0]+i < boardSize and move[1]-i > -1:
    dSub.append(state.board[move[0]+i][move[1]-i])
    i += 1
  if len(KMPSearch(pat5, dSub)) != 0 or len(KMPSearch(live4, dSub)) != 0:
    return True
  
  # # horizonal
  # for row in state.board:
  #   if len(KMPSearch(pat5, row)) != 0 or len(KMPSearch(live4, row)) != 0:
  #     return True
  # # vertical
  # tmp = np.transpose(state.board)
  # for row in tmp:
  #   if len(KMPSearch(pat5, row)) != 0 or len(KMPSearch(live4, row)) != 0:
  #     return True

  # # diag main
  # tmp = [[] for _ in range((boardSize-5)*2+1)]
  # k = 0
  # for i in range(boardSize-5, -1, -1):
  #   for j in range(i, boardSize):
  #     tmp[k].append(state.board[j-i][j])
  #   k += 1
  # for i in range(1, boardSize-5+1):
  #   for j in range(0, boardSize-i):
  #     tmp[k].append(state.board[j+i][j])
  #   k += 1
  # for row in tmp:
  #   if len(KMPSearch(pat5, row)) != 0 or len(KMPSearch(live4, row)) != 0:
  #     return True
  
  # # diag sub
  # tmp = [[] for _ in range((boardSize-5)*2+1)]
  # k = 0
  # for i in range(4, boardSize):
  #   for j in range(i+1):
  #     tmp[k].append(state.board[j][i-j])
  #   k += 1
  # for i in range(1, boardSize-4):
  #   for j in range(boardSize-1, i-1, -1):
  #     tmp[k].append(state.board[i+boardSize-1-j][j])
  #   k += 1
  # for row in tmp:
  #   if len(KMPSearch(pat5, row)) != 0 or len(KMPSearch(live4, row)) != 0:
  #     return True

  # no one success
  for i in range(boardSize):
    for j in range(boardSize):
      if(state.board[i][j] == '.'):
        return False
  return True


def evalState(state: Board, prevRole: str) -> int:
  localStar = getLocalLines(state, prevRole)
  if prevRole == 'w':
    scoreW = 0
    if state.capW >= 10:
      scoreW += 10000
    scoreW += (state.capW - initBoard.capW)*175
    scoreW += state.countW//2
    for line in localStar:
      # attack
      scoreW += len(KMPSearch('wwwww', line))*10000
      scoreW += len(KMPSearch('.wwww.', line))*4000
      scoreW += len(KMPSearch('.www.w.', line))*400
      scoreW += len(KMPSearch('.ww.ww.', line))*250
      scoreW += len(KMPSearch('bwwww.', line))*300
      scoreW += len(KMPSearch('bwww.w', line))*300
      scoreW += len(KMPSearch('bww.ww', line))*100
      scoreW += len(KMPSearch('.www..', line))*150
      scoreW += len(KMPSearch('.ww.w.', line))*80
      scoreW += len(KMPSearch('.ww..w', line))*70
      scoreW += len(KMPSearch('bwww..', line))*60
      scoreW += len(KMPSearch('bw.ww.', line))*45
      scoreW += len(KMPSearch('.ww..', line))*20
      scoreW += len(KMPSearch('.w.w.', line))*10
      # defense
      scoreW += len(KMPSearch('wbbbbw', line))*800
      scoreW += len(KMPSearch('wbbb.', line))*250
      scoreW += len(KMPSearch('wbbbw', line))*200
      scoreW += len(KMPSearch('wbb.', line))*40
      line.reverse()
      # attack
      scoreW += len(KMPSearch('.www.w.', line))*400
      scoreW += len(KMPSearch('bwwww.', line))*300
      scoreW += len(KMPSearch('bwww.w', line))*300
      scoreW += len(KMPSearch('bww.ww', line))*100
      scoreW += len(KMPSearch('.www..', line))*150
      scoreW += len(KMPSearch('.ww.w.', line))*80
      scoreW += len(KMPSearch('.ww..w', line))*70
      scoreW += len(KMPSearch('bwww..', line))*60
      scoreW += len(KMPSearch('bw.ww.', line))*45
      scoreW += len(KMPSearch('.ww..', line))*20
      # defense
      scoreW += len(KMPSearch('wbbb.', line))*250
      scoreW += len(KMPSearch('wbb.', line))*40
    # return scoreW if selfRole == 'w' else -scoreW
    return scoreW if selfRole == 'w' else -scoreW
  else:
    scoreB = 0
    if state.capB >= 10:
      scoreB += 10000
    scoreB += (state.capB - initBoard.capB)*175
    scoreB += state.countB//2
    for line in localStar:
      # attack
      scoreB += len(KMPSearch('bbbbb', line))*10000
      scoreB += len(KMPSearch('.bbbb.', line))*4000
      scoreB += len(KMPSearch('.bbb.b.', line))*400
      scoreB += len(KMPSearch('.bb.bb.', line))*250
      scoreB += len(KMPSearch('wbbbb.', line))*300
      scoreB += len(KMPSearch('wbbb.b', line))*300
      scoreB += len(KMPSearch('wbb.bb', line))*100
      scoreB += len(KMPSearch('.bbb..', line))*150
      scoreB += len(KMPSearch('.bb.b.', line))*80
      scoreB += len(KMPSearch('.bb..b', line))*70
      scoreB += len(KMPSearch('wbbb..', line))*60
      scoreB += len(KMPSearch('wb.bb.', line))*45
      scoreB += len(KMPSearch('.bb..', line))*20
      scoreB += len(KMPSearch('.b.b.', line))*10
      # defense
      scoreB += len(KMPSearch('bwwwwb', line))*800
      scoreB += len(KMPSearch('bwww.', line))*250
      scoreB += len(KMPSearch('bwwwb', line))*200
      scoreB += len(KMPSearch('bww.', line))*40
      line.reverse()
      # attack
      scoreB += len(KMPSearch('.bbb.b.', line))*400
      scoreB += len(KMPSearch('wbbbb.', line))*300
      scoreB += len(KMPSearch('wbbb.b', line))*300
      scoreB += len(KMPSearch('wbb.bb', line))*100
      scoreB += len(KMPSearch('.bbb..', line))*150
      scoreB += len(KMPSearch('.bb.b.', line))*80
      scoreB += len(KMPSearch('.bb..b', line))*70
      scoreB += len(KMPSearch('wbbb..', line))*60
      scoreB += len(KMPSearch('wb.bb.', line))*45
      scoreB += len(KMPSearch('.bb..', line))*20
      # defense
      scoreB += len(KMPSearch('bwww.', line))*250
      scoreB += len(KMPSearch('bww.', line))*40
    # return scoreB if selfRole == 'b' else -scoreB
    return scoreB if selfRole == 'b' else -scoreB

def getLocalLines(state: Board, role: str):
  oppRole = ('b' if role == 'w' else 'w')
  move = (state.moveW if role == 'w' else state.moveB)
  # diag main
  # top-left
  dMain = []
  i = 1
  while i<6 and move[0]-i > -1 and move[1]-i > -1:
    dMain.append(state.board[move[0]-i][move[1]-i])
    i += 1
  # reaches edge of board
  if i<6:
    dMain.append(oppRole)
  dMain.reverse()
  dMain.append(state.board[move[0]][move[1]])
  # bottom-right
  i = 1
  while i<6 and move[0]+i < boardSize and move[1]+i < boardSize:
    dMain.append(state.board[move[0]+i][move[1]+i])
    i += 1
  # reaches edge of board
  if i<6:
    dMain.append(oppRole)
  
  # diag sub
  dSub = []
  # top-right
  i = 1
  while i<6 and move[0]-i > -1 and move[1]+i < boardSize:
    dSub.append(state.board[move[0]-i][move[1]+i])
    i += 1
  # reaches edge of board
  if i<6:
    dSub.append(oppRole)
  dSub.reverse()
  dSub.append(state.board[move[0]][move[1]])
  # bottom-left
  i = 1
  while i<6 and move[0]+i < boardSize and move[1]-i > -1:
    dSub.append(state.board[move[0]+i][move[1]-i])
    i += 1
  # reaches edge of board
  if i<6:
    dSub.append(oppRole)
  
  # vert
  vert = []
  # top
  i = 1
  while i<6 and move[0]-i > -1:
    vert.append(state.board[move[0]-i][move[1]])
    i += 1
  # reaches edge of board
  if i<6:
    vert.append(oppRole)
  vert.reverse()
  vert.append(state.board[move[0]][move[1]])
  # bottom-left
  i = 1
  while i<6 and move[0]+i < boardSize:
    vert.append(state.board[move[0]+i][move[1]])
    i += 1
  # reaches edge of board
  if i<6:
    vert.append(oppRole)

  # horiz
  horiz = state.board[move[0]][max(0, move[1]-5):min(boardSize, move[1]+6)].tolist()
  # print(horiz)
  if move[1]-5 < 0:
    horiz.insert(0, oppRole)
  if move[1]+6 > boardSize:
    horiz.append(oppRole)
  
  return [dMain, dSub, vert, horiz]
  

def alphaBeta(state: Board, depth: int, curRole: str, alpha, beta):
  if state.countB == 0 and state.countW == 0 and curRole == 'w':
    return (9, 9), 0
  elif state.countW == 1 and state.countB == 0 and curRole == 'b':
    return (8, 8), 0
  # 2nd white move
  elif state.countW == 1 and state.countB == 1 and curRole == 'w':
    (bI, bJ) = list(zip(*np.where(state.board == 'b')))[0]
    dI, dJ = bI-9, bJ-9
    if dI < 0 and dJ > 0 and -dI <= dJ:
      return (6, 6), 0
    elif dI < 0 and dJ >= 0 and -dI > dJ:
      return (9, 6), 0
    elif dI < 0 and dJ < 0 and dI <= dJ:
      return (12, 6), 0
    elif dI <= 0 and dJ < 0 and dI > dJ:
      return (12, 9), 0
    elif dI > 0 and dJ < 0 and -dJ >= dI:
      return (12, 12), 0
    elif dI > 0 and dJ <= 0 and -dJ < dI:
      return (9, 12), 0
    elif dI > 0 and dJ > 0 and dI >= dJ:
      return (6, 12), 0
    elif dI >= 0 and dJ >= 0 and dI < dJ:
      return (6, 9), 0
  else:
    if depth == 0 or (depth != globDepth and isLeafState(state, 'b' if curRole == 'w' else 'w')):
      return state.moveB if curRole == 'w' else state.moveW, evalState(state, 'b' if curRole == 'w' else 'w')
    candMoves = state.getCandMoves()
    if selfRole == curRole:
      maxScore, score, maxMove = -10000000, -10000000, None
      for coord in candMoves:
        # log.write('  '*(globDepth-depth) + 'before -- depth: ' + str(depth) + ' move:' + str(coord) + ' role: ' + str(curRole) + ' maxScore: ' + (str(maxScore) if maxMove != None else '-inf') + ' maxMove: ' + (str(maxMove) if maxMove != None else ' Null') + '\n')
        newState = deepcopy(state)
        newState.makeMove(coord, curRole)
        tmp, score = alphaBeta(newState, depth-1, 'b' if curRole == 'w' else 'w', alpha, beta)
        if score > maxScore:
          maxScore = score
          maxMove = coord
        # log.write('  '*(globDepth-depth) + 'after -- score: ' + str(score) + ' maxScore: ' + (str(maxScore) if maxMove != None else '-inf') + ' maxMove: ' + (str(maxMove) if maxMove != None else ' Null') + '\n')
        if maxScore >= beta:
          return maxMove, maxScore
        alpha = max(maxScore, alpha)
      return maxMove, maxScore
    else:
      minScore, score, minMove = 10000000, 10000000, None
      for coord in candMoves:
        # log.write('  '*(globDepth-depth) + 'before -- depth: ' + str(depth) + ' move:' + str(coord) + ' role: ' + str(curRole) + ' minScore: ' + (str(minScore) if minMove != None else 'inf') + ' minMove: ' + (str(minMove) if minMove != None else ' Null') + '\n')
        newState = deepcopy(state)
        newState.makeMove(coord, curRole)
        tmp, score = alphaBeta(newState, depth-1, 'b' if curRole == 'w' else 'w', alpha, beta)
        if score < minScore:
          minScore = score
          minMove = coord
        # log.write('  '*(globDepth-depth) + 'after -- score: ' + str(score) + ' minScore: ' + (str(minScore) if minMove != None else 'inf') + ' minMove: ' + (str(minMove) if minMove != None else ' Null') + '\n')
        if minScore <= alpha:
          return minMove, minScore
        beta = min(minScore, beta)
      return minMove, minScore

# log = open('log_py.txt', 'w')
# start = time.time()
initBoard, remTIme, selfRole = readBoard('input.txt')
if 50 < remTIme <= 200:
  globDepth = 3
elif 15 < remTIme <= 50:
  globDepth = 2
elif remTIme <= 15:
  globDepth = 1
move, score = alphaBeta(initBoard, globDepth, selfRole, -10000000, 10000000)
writeRes('output.txt', move)
# end = time.time()
# print(end - start)
# log.close()

# sample = [10]
# for i in sample:
#     print(i)
#     start = time.time()
#     initBoard, remTIme, selfRole = readBoard('input/input' + str(i) + '.txt')
#     move, score = alphaBeta(initBoard, globDepth, selfRole, -10000000, 10000000)
#     print(move)
#     writeRes('output/output' + str(i) + '.txt', move)
#     end = time.time()
#     print(end - start)