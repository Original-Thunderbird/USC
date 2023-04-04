# CSCI561
## CSCI561.1 Search
BFS, UCS, A*.

Develop an algorithm to find the optimal path to reach our destination (and to a cup of hot cocoa) based on a particular objective.

I/O format: see page 7 of pdf


### 1. Getting Started
```
python runner.py
```


### 2. Technologies
python



## CSCI561.2 Pente Agent
Develop an agent for pente game. Every agent has 300s to think per game. See rules, board definition & I/O format explanation in pdf.

Idea: Minimax with alpha-beta pruning, local evaluation of moves used to rank search sequence and accelerate pruning.

Heuristics used for leaf state evaluation recorded in heuristic_design.txt

### 1. Getting Started
#### .py agent
venv
```
python -m venv pente
source pente/bin/activate
pip install numpy
```
run
```
python homework.py
```

#### .cpp agent
```
g++ -std=c++11 -o homework homework_x.cpp && ./homework
```
x in homework_x.cpp should be replaced by -0,1,or 2.

Game host agent owned by the instructor, so there's no way to run the game automatically.



### 2. Technologies
python, C++



## CSCI561.3 Knowledge Infernece Engine
Give a knowledge base (KB) and a Query, see if the Query can be inferenced from the KB. Basic idea is prove by refutation.

See I/O format explanation in pdf.


### 1. Getting Started
```
python homework_x.py
```
x in homework_x.cpp should be replaced by - a number


### 2. Technologies
python