#include <fstream> 
#include <vector>
#include <string>
#include <algorithm>
#include <limits.h>
#include <set>
#include <iostream>
#include <chrono>
using namespace std;

struct Coord {
  int row, col;
  bool operator < (const Coord &a) const {
    return (row < a.row) || (!(row < a.row) && col < a.col);
  }
};

const char* MoveToStr(Coord move) {
  string str;
  str.push_back('(');
  str += to_string(move.row);
  str.push_back(',');
  str += to_string(move.col);
  str.push_back(')');
  return str.c_str();
}

struct MMRet {
  Coord coord;
  int score;
  bool operator < (const MMRet& a) const {
    return (score < a.score);
  }
};

char globRole;
int searchDepth = 3;
int boardSize = 19;
int dirs[8][2] = {{0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}};

string BA5("bbbbb");
string BA4_A1(".bbbb."), BA4_A2(".bbb.b."), BA4_A3(".bb.bb.");
string BA4_B1("wbbbb."), BA4_B2("wbbb.b"), BA4_B3("wbb.bb."), BA4_B4("wb.bbb");
string BA3_A1(".bbb.."), BA3_A2(".bb.b."), BA3_A3(".bb..b");
string BA3_B1("wbbb.."), BA3_B2("wb.bb.");
string BA2_A1(".bb.."), BA2_A2(".b.b.");
string BD4_1("bwwwwb"), BD4_2("wwwbw"), BD4_3("b..bww");
string BD3_A1(".bwww."), BD3_A2(".wbww.");
string BD3_B1("bwwwb."), BD3_B2("bwww.b"), BD3_B3("b..bw"), BD3_B4("bwbww."), BD2("bww.");

string WA5("wwwww");
string WA4_A1(".wwww."), WA4_A2(".www.w."), WA4_A3(".ww.ww.");
string WA4_B1("bwwww."), WA4_B2("bwww.w"), WA4_B3("bww.ww."), WA4_B4("bw.www");
string WA3_A1(".www.."), WA3_A2(".ww.w."), WA3_A3(".ww..w");
string WA3_B1("bwww.."), WA3_B2("bw.ww.");
string WA2_A1(".ww.."), WA2_A2(".w.w.");
string WD4_1("wbbbbw"), WD4_2("bbbwb"), WD4_3("w..wbb");
string WD3_A1(".wbbb."), WD3_A2(".bwbb.");
string WD3_B1("wbbbw."), WD3_B2("wbbb.w"), WD3_B3("w..wb"), WD3_B4("wbwbb."), WD2("wbb.");

class State {
  public:
    // countB: # of black pieces on board
    // countW: # of white pieces on board
    int score, capB, capW, countB, countW;
    vector<string> board;
    Coord moveW, moveB;

    State() {}

    State(const State &ano) {
      score = ano.score;
      capB = ano.capB;
      capW = ano.capW;
      countB = ano.countB;
      countW = ano.countW;
      moveB = ano.moveB;
      moveW = ano.moveW;
      board.assign(ano.board.begin(), ano.board.end());
    }

    void MakeMove(Coord move, char role) {
      board[move.row][move.col] = role;
      if(role == 'b') {
        countB++;
        moveB = move;
      }
      else {
        countW++;
        moveW = move;
      }
      char oppRole = (role == 'b' ? 'w' : 'b');
      // (-1, 0)
      if(move.row-3 > -1 && board[move.row-3][move.col] == role && board[move.row-2][move.col] == oppRole && board[move.row-1][move.col] == oppRole) {
        board[move.row-2][move.col] = '.';
        board[move.row-1][move.col] = '.';
        CaptureOpponent(role);
      }
      // (-1, 1)
      if(move.row-3 > -1 && move.col+3 < 19 && board[move.row-3][move.col+3] == role && board[move.row-2][move.col+2] == oppRole && board[move.row-1][move.col+1] == oppRole) {
        board[move.row-2][move.col+2] = '.';
        board[move.row-1][move.col+1] = '.';
        CaptureOpponent(role);
      }
      // (0, 1)
      if(move.col+3 < 19 && board[move.row][move.col+3] == role && board[move.row][move.col+2] == oppRole && board[move.row][move.col+1] == oppRole) {
        board[move.row][move.col+2] = '.';
        board[move.row][move.col+1] = '.';
        CaptureOpponent(role);
      }
      // (1, 1)
      if(move.row+3 < 19 && move.col+3 < 19 && board[move.row+3][move.col+3] == role && board[move.row+2][move.col+2] == oppRole && board[move.row+1][move.col+1] == oppRole) {
        board[move.row+2][move.col+2] == '.';
        board[move.row+1][move.col+1] == '.';
        CaptureOpponent(role);
      }
      // (1, 0)
      if(move.row+3 < 19 && board[move.row+3][move.col] == role && board[move.row+2][move.col] == oppRole && board[move.row+1][move.col] == oppRole) {
        board[move.row+2][move.col] == '.';
        board[move.row+1][move.col] == '.';
        CaptureOpponent(role);
      }
      // (1, -1)
      if(move.row+3 < 19 && move.col-3 > -1 && board[move.row+3][move.col-3] == role && board[move.row+2][move.col-2] == oppRole && board[move.row+1][move.col-1] == oppRole) {
        board[move.row+2][move.col-2] == '.';
        board[move.row+1][move.col-1] == '.';
        CaptureOpponent(role);
      }
      // (0, -1)
      if(move.col-3 > -1 && board[move.row][move.col-3] == role && board[move.row][move.col-2] == oppRole && board[move.row][move.col-1] == oppRole) {
        board[move.row][move.col-2] = '.';
        board[move.row][move.col-1] = '.';
        CaptureOpponent(role);
      }
      // (-1, -1)
      if(move.row-3 > -1 && move.col-3 > -1 && board[move.row-3][move.col-3] == role && board[move.row-2][move.col-2] == oppRole && board[move.row-1][move.col-1] == oppRole) {
        board[move.row-2][move.col-2] == '.';
        board[move.row-1][move.col-1] == '.';
        CaptureOpponent(role);
      }
    }

    void CaptureOpponent(char role) {
      if(role == 'b') {
        capB += 2;
        countW -= 2;
      }
      else {
        capW +=2;
        countB -= 2;
      }
    }
};

State initBoard;

// int MaxPlay(State state, int alpha, int beta, int depth);

void ReadInput(float& remTime, string& role, State& state, string inFile) {
  ifstream input(inFile);
  string buff;
  input >> role >> remTime >> buff;

  string split = ",";
  int commaInd = buff.find(split);
  string capWStr = buff.substr(0, commaInd);
  string capBStr =  buff.substr(commaInd+1, buff.length()-commaInd);
  state.capW = stoi(capWStr);
  state.capB = stoi(capBStr);

  getline(input, buff);
  while(getline(input, buff)) {
    // cout << buff.size() << endl;
    state.board.push_back(buff);
  }
  state.countB = 0, state.countW = 0;
  for(int i=0; i<boardSize; i++) {
    for(int j=0; j<boardSize; j++) {
      if(state.board[i][j] == 'w') {
        state.countW++;
      }
      else if(state.board[i][j] == 'b') {
        state.countB++;
      }
    }
  }
  input.close();
}

void WriteCoord(Coord resCoord, string outFile) {
  string res;
  // row
  res.append(to_string(19-resCoord.row));
  // column
  res.push_back(resCoord.col < 8 ? (char)('A'+resCoord.col) : (char)('A'+resCoord.col+1));
  
  ofstream output(outFile);
  output << res;
  output.close();
}

void computeLPSArray(string& pat, int M, int* lps) {
    int len = 0;
    lps[0] = 0; // lps[0] is always 0

    int i = 1;
    while (i < M) {
        if (pat[i] == pat[len]) {
            len++;
            lps[i] = len;
            i++;
        }
        else {// (pat[i] != pat[len])
            if (len != 0) {
                len = lps[len - 1];
            }
            else {// if (len == 0) 
                lps[i] = 0;
                i++;
            }
        }
    }
}

vector<int> KMPSearch(string& pat, string& txt) {
    vector<int> res;
    int M = pat.length();
    int N = txt.length();
    int lps[M];

    computeLPSArray(pat, M, lps);
    int i = 0; // index for txt[]
    int j = 0; // index for pat[]
    while ((N - i) >= (M - j)) {
        if (pat[j] == txt[i]) {
            j++;
            i++;
        }
        if (j == M) {
            res.push_back(i-j);
            j = lps[j - 1];
        }
        else if (i < N && pat[j] != txt[i]) {
            if (j != 0)
                j = lps[j - 1];
            else
                i = i + 1;
        }
    }
    return res;
}

string GetMoveHorizNeighbor(vector<string>& board, Coord& move, char& curRole) {
  string res;
  char oppRole = (curRole == 'w' ? 'b' : 'w');
  int i=1;
  // left
  while(i<6 && move.col-i > -1) {
    res.push_back(board[move.row][move.col-i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }

  reverse(res.begin(), res.end());
  res.push_back(curRole);
  // right
  i=1;
  while(i<6 && move.col+i < boardSize) {
    res.push_back(board[move.row][move.col+i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }
  return res;
}

string GetMoveVertNeighbor(vector<string>& board, Coord& move, char& curRole) {
  string res;
  char oppRole = (curRole == 'w' ? 'b' : 'w');
  int i=1;
  // top
  while(i<6 && move.row-i > -1) {
    res.push_back(board[move.row-i][move.col]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }

  reverse(res.begin(), res.end());
  res.push_back(curRole);
  // bottom
  i=1;
  while(i<6 && move.row+i < boardSize) {
    res.push_back(board[move.row+i][move.col]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }
  return res;
}

string GetMoveMainDiagNeighbor(vector<string>& board, Coord& move, char& curRole) {
  string res;
  char oppRole = (curRole == 'w' ? 'b' : 'w');
  // top-left
  int i=1;
  while(i<6 && move.row-i > -1 && move.col-i > -1) {
    res.push_back(board[move.row-i][move.col-i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }

  reverse(res.begin(), res.end());
  res.push_back(curRole);
  // bottom-right
  i=1;
  while(i<6 && move.row+i < boardSize && move.col+i < boardSize) {
    res.push_back(board[move.row+i][move.col+i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }
  return res;
}

string GetMoveSubDiagNeighbor(vector<string>& board, Coord& move, char& curRole) {
  string res;
  char oppRole = (curRole == 'w' ? 'b' : 'w');
  // top-right
  int i=1;
  while(i<6 && move.row-i > -1 && move.col+i < boardSize) {
    res.push_back(board[move.row-i][move.col+i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }

  reverse(res.begin(), res.end());
  res.push_back(curRole);
  // bottom-left
  i=1;
  while(i<6 && move.row+i < boardSize && move.col-i > -1) {
    res.push_back(board[move.row+i][move.col-i]);
    i++;
  }
  if(i<6) {
    res.push_back(oppRole);
  }
  return res;
}

// role: role in prev depth, if role at current depth is 'w' then 'role' in this func is 'b', vice versa
bool IsLeafState(State& state, char& role) {
  if(state.capB >= 10 || state.capW >= 10) {
    return true;
  }
  string pat5 = (role == 'w' ? "wwwww" : "bbbbb");
  // string live4 = (role == 'w' ? ".wwww." : ".bbbb.");
  Coord move = (role == 'w' ? state.moveW : state.moveB);
  vector<int> res;

  
  // cout << role << " " << state.moveW.row << " " << state.moveW.col << " " << state.moveB.row << " " << state.moveB.col << endl;
  string horiz = GetMoveHorizNeighbor(state.board, move, role);
  if(KMPSearch(pat5, horiz).size() > 0) {
    return true;
  }
  string vert = GetMoveVertNeighbor(state.board, move, role);
  if(KMPSearch(pat5, vert).size() > 0) {
    return true;
  }
  string mainDiag = GetMoveMainDiagNeighbor(state.board, move, role);
  if(KMPSearch(pat5, mainDiag).size() > 0) {
    return true;
  }
  string subDiag = GetMoveSubDiagNeighbor(state.board, move, role);
  if(KMPSearch(pat5, subDiag).size() > 0) {
    return true;
  }

  for(int i=0; i<19; i++) {
    for(int j=0; j<19; j++) {
      if(state.board[i][j] == '.') {
        return false;
      }
    }
  }
  return true;
}

int EvalState(State& state, char& role) {
  Coord move = (role == 'w' ? state.moveW : state.moveB);

  vector<string> localStar;
  localStar.push_back(GetMoveHorizNeighbor(state.board, move, role));
  localStar.push_back(GetMoveVertNeighbor(state.board, move, role));
  localStar.push_back(GetMoveMainDiagNeighbor(state.board, move, role));
  localStar.push_back(GetMoveSubDiagNeighbor(state.board, move, role));

  if(role == 'w') {
    int scoreW = 0;
    if(state.capW >= 10) {
      return globRole == 'w' ? INT_MAX : INT_MIN;
    }
    for(string line: localStar) {
      if(KMPSearch(WA5, line).size() > 0) {
        return globRole == 'w' ? INT_MAX : INT_MIN;
      }
    }
    scoreW += (state.capW - initBoard.capW)*175;
    // scoreW += state.countW/2;
    for(string line: localStar) {
      // attack
      scoreW += KMPSearch(WA4_A1, line).size()*1200;
      scoreW += KMPSearch(WA4_A2, line).size()*550;
      scoreW += KMPSearch(WA4_A3, line).size()*650;

      scoreW += KMPSearch(WA4_B1, line).size()*300;
      scoreW += KMPSearch(WA4_B2, line).size()*280;
      scoreW += KMPSearch(WA4_B3, line).size()*70;
      scoreW += KMPSearch(WA4_B4, line).size()*280;
      
      scoreW += KMPSearch(WA3_A1, line).size()*250;
      scoreW += KMPSearch(WA3_A2, line).size()*210;
      scoreW += KMPSearch(WA3_A3, line).size()*60;

      scoreW += KMPSearch(WA3_B1, line).size()*75;
      scoreW += KMPSearch(WA3_B2, line).size()*45;

      scoreW += KMPSearch(WA2_A1, line).size()*50;
      scoreW += KMPSearch(WA2_A2, line).size()*50;
      // defense
      scoreW += KMPSearch(WD4_1, line).size()*5000;
      scoreW += KMPSearch(WD4_2, line).size()*2500;
      if(state.capW != initBoard.capW) {
        scoreW += KMPSearch(WD4_3, line).size()*2500;
      }

      scoreW += KMPSearch(WD3_A1, line).size()*275;
      scoreW += KMPSearch(WD3_A2, line).size()*275;

      scoreW += KMPSearch(WD3_B1, line).size()*200;
      scoreW += KMPSearch(WD3_B2, line).size()*175;
      if(state.capW != initBoard.capW) {
        scoreW += KMPSearch(WD3_B3, line).size()*175;
      }
      scoreW += KMPSearch(WD3_B4, line).size()*175;

      scoreW += KMPSearch(WD2, line).size()*15;


      reverse(line.begin(), line.end());
      // attack
      scoreW += KMPSearch(WA4_A2, line).size()*550;

      scoreW += KMPSearch(WA4_B1, line).size()*300;
      scoreW += KMPSearch(WA4_B2, line).size()*280;
      scoreW += KMPSearch(WA4_B3, line).size()*70;
      scoreW += KMPSearch(WA4_B4, line).size()*280;

      scoreW += KMPSearch(WA3_A1, line).size()*250;
      scoreW += KMPSearch(WA3_A2, line).size()*210;
      scoreW += KMPSearch(WA3_A3, line).size()*60;

      scoreW += KMPSearch(WA3_B1, line).size()*75;
      scoreW += KMPSearch(WA3_B2, line).size()*45;

      scoreW += KMPSearch(WA2_A1, line).size()*50;
      // defense
      scoreW += KMPSearch(WD4_2, line).size()*2500;
      if(state.capW != initBoard.capW) {
        scoreW += KMPSearch(WD4_3, line).size()*2500;
      }

      scoreW += KMPSearch(WD3_A1, line).size()*275;
      scoreW += KMPSearch(WD3_A2, line).size()*275;

      scoreW += KMPSearch(WD3_B1, line).size()*200;
      scoreW += KMPSearch(WD3_B2, line).size()*175;
      if(state.capW != initBoard.capW) {
        scoreW += KMPSearch(WD3_B3, line).size()*175;
      }

      scoreW += KMPSearch(WD2, line).size()*15;
    }
    return globRole == 'w' ? scoreW : -scoreW;
  }
  else {
    int scoreB = 0;
    if(state.capB >= 10) {
      return globRole == 'b' ? INT_MAX : INT_MIN;
    }
    for(string line: localStar) {
      if(KMPSearch(BA5, line).size() > 0) {
        return globRole == 'b' ? INT_MAX : INT_MIN;
      }
    }
    scoreB += (state.capB - initBoard.capB)*175;
    // scoreB += state.countB/2;
    for(string line: localStar) {
      // attack
      scoreB += KMPSearch(BA4_A1, line).size()*1200;
      scoreB += KMPSearch(BA4_A2, line).size()*550;
      scoreB += KMPSearch(BA4_A3, line).size()*650;

      scoreB += KMPSearch(BA4_B1, line).size()*300;
      scoreB += KMPSearch(BA4_B2, line).size()*280;
      scoreB += KMPSearch(BA4_B3, line).size()*70;
      scoreB += KMPSearch(BA4_B4, line).size()*280;
      
      scoreB += KMPSearch(BA3_A1, line).size()*250;
      scoreB += KMPSearch(BA3_A2, line).size()*210;
      scoreB += KMPSearch(BA3_A3, line).size()*60;

      scoreB += KMPSearch(BA3_B1, line).size()*75;
      scoreB += KMPSearch(BA3_B2, line).size()*45;

      scoreB += KMPSearch(BA2_A1, line).size()*50;
      scoreB += KMPSearch(BA2_A2, line).size()*50;
      // defense
      scoreB += KMPSearch(BD4_1, line).size()*5000;
      scoreB += KMPSearch(BD4_2, line).size()*2500;
      if(state.capB != initBoard.capB) {
        scoreB += KMPSearch(BD4_3, line).size()*2500;
      }

      scoreB += KMPSearch(BD3_A1, line).size()*275;
      scoreB += KMPSearch(BD3_A2, line).size()*275;

      scoreB += KMPSearch(BD3_B1, line).size()*200;
      scoreB += KMPSearch(BD3_B2, line).size()*175;
      if(state.capB != initBoard.capB) {
        scoreB += KMPSearch(BD3_B3, line).size()*175;
      }
      scoreB += KMPSearch(BD3_B4, line).size()*175;

      scoreB += KMPSearch(BD2, line).size()*15;


      reverse(line.begin(), line.end());
      // attack
      scoreB += KMPSearch(BA4_A2, line).size()*550;

      scoreB += KMPSearch(BA4_B1, line).size()*300;
      scoreB += KMPSearch(BA4_B2, line).size()*280;
      scoreB += KMPSearch(BA4_B3, line).size()*70;
      scoreB += KMPSearch(BA4_B4, line).size()*280;

      scoreB += KMPSearch(BA3_A1, line).size()*250;
      scoreB += KMPSearch(BA3_A2, line).size()*210;
      scoreB += KMPSearch(BA3_A3, line).size()*60;

      scoreB += KMPSearch(BA3_B1, line).size()*75;
      scoreB += KMPSearch(BA3_B2, line).size()*45;

      scoreB += KMPSearch(BA2_A1, line).size()*50;
      // defense
      scoreB += KMPSearch(BD4_2, line).size()*2500;
      if(state.capW != initBoard.capW) {
        scoreB += KMPSearch(BD4_3, line).size()*2500;
      }

      scoreB += KMPSearch(BD3_A1, line).size()*275;
      scoreB += KMPSearch(BD3_A2, line).size()*275;

      scoreB += KMPSearch(BD3_B1, line).size()*200;
      scoreB += KMPSearch(BD3_B2, line).size()*175;
      if(state.capW != initBoard.capW) {
        scoreB += KMPSearch(BD3_B3, line).size()*175;
      }

      scoreB += KMPSearch(BD2, line).size()*15;
    }
    return globRole == 'b' ? scoreB : -scoreB;
  }
}

set<Coord> FindCandidateMoves(State& state) {
  set<Coord> candSet;
  for(int i=0; i<boardSize; i++) {
    for(int j=0; j<boardSize; j++) {
      if(state.board[i][j] != '.') {
        for(int k=0; k<8; k++) {
          int newI1 = i+dirs[k][0], newJ1 = j+dirs[k][1];
          if(newI1 > -1 && newI1 < boardSize && newJ1 > -1 && newJ1 < boardSize) {
            if(state.board[newI1][newJ1] == '.') {
              candSet.insert(Coord{newI1, newJ1});
            }
            int newI2 = newI1+dirs[k][0], newJ2 = newJ1+dirs[k][1];
            if(newI2 > -1 && newI2 < boardSize && newJ2 > -1 && newJ2 < boardSize && state.board[newI2][newJ2] == '.') {
              candSet.insert(Coord{newI2, newJ2});
            }
          }
        }
      }
    }
  }
  return candSet;
}

vector<Coord> RankCandidateMoves(set<Coord>& candSet, State state, char& role) {
  vector<MMRet> rankList;
  vector<Coord> resList;
  for(Coord coord: candSet) {
    State tmp(state);
    tmp.MakeMove(coord, role);
    rankList.push_back(MMRet{coord, EvalState(tmp, role)});
  }
  sort(rankList.begin(), rankList.end());
  // after sort, move with smaller value will appear in the front
  // for max move, we want the list in dec order
  if(role == globRole) {
    reverse(rankList.begin(), rankList.end());
  }
  for(MMRet m: rankList) {
    // cout << "move: " << MoveToStr(m.coord) << " score:" << m.score << endl;
    resList.push_back(m.coord);
  }
  return resList;
}

MMRet AlphaBeta(State& state, int alpha, int beta, int depth, char role, FILE *log) {
  if(state.countB == 0 && state.countW == 0 && role == 'w') {
    return MMRet{Coord{9, 9}, 0};
  }
  else if (state.countW == 1 && state.countB == 0 && role == 'b') {
    return MMRet{Coord{8, 8}, 0};
  }
  else if (state.countW == 1 && state.countB == 1 && role == 'w') {
    int bI, bJ;
    for(bI=0; bI<boardSize; bI++) {
      for(bJ=0; bJ<boardSize; bJ++) {
        if(state.board[bI][bJ] == 'b') {
          goto found;
        }
      }
    }

    found:
    int dI = bI-9, dJ = bJ-9;
    // (0, 45]
    if(dI < 0 && dJ > 0 && -dI <= dJ) {
      return MMRet{Coord{6, 6}, 0};
    }
    // (45, 90]
    else if(dI < 0 && dJ >= 0 && -dI > dJ) {
      return MMRet{Coord{9, 6}, 0};
    }
    // (90, 135]
    else if(dI < 0 && dJ < 0 && dI <= dJ) {
      return MMRet{Coord{12, 6}, 0};
    }
    // (135, 180]
    else if(dI <= 0 && dJ < 0 && dI > dJ) {
      return MMRet{Coord{12, 9}, 0};
    }
    // (180, 225]
    else if(dI > 0 && dJ < 0 && -dJ >= dI) {
      return MMRet{Coord{12, 12}, 0};
    }
    // (225, 270]
    else if(dI > 0 && dJ <= 0 && -dJ < dI) {
      return MMRet{Coord{9, 12}, 0};
    }
    // (270, 315]
    else if(dI > 0 && dJ > 0 && dI >= dJ) {
      return MMRet{Coord{6, 12}, 0};
    }
    // (315, 360]
    else if (dI >= 0 && dJ > 0 && dI < dJ) {
      return MMRet{Coord{6, 9}, 0};
    }
  }
  else {
    char prevRole = (role == 'w' ? 'b' : 'w'), nextRole = prevRole;
    if(depth == 0 || depth != searchDepth && IsLeafState(state, prevRole) == true) {
        return MMRet{role == 'w' ? state.moveW : state.moveB, EvalState(state, prevRole)};
    } 
    set<Coord> candMoves = FindCandidateMoves(state);
    vector<Coord> rankedMoves = RankCandidateMoves(candMoves, state, role);
    MMRet res;
    string blank;
    const char* blackArr = blank.c_str();
    for(int i=0; i<searchDepth-depth; i++) {
      blank += "  ";
    }
    if(role == globRole) {
      int maxScore = INT_MIN;
      Coord maxMove = {-1, -1};
      for(Coord move: rankedMoves) {
        fprintf(log, "%sbefore -- depth: %d move: %s role: %c maxScore: %d maxMove: %s alpha: %d, beta: %d\n", blackArr, depth, MoveToStr(move), role, maxScore, MoveToStr(maxMove), alpha, beta);
        State tmpState(state);
        tmpState.MakeMove(move, role);
        res = AlphaBeta(tmpState, alpha, beta, depth-1, nextRole, log);
        if(res.score > maxScore) {
          maxScore = res.score;
          maxMove = move;
        }
        fprintf(log, "%safter -- score: %d maxScore: %d maxMove: %s\n", blackArr, res.score, maxScore, MoveToStr(maxMove));
        if(maxScore >= beta) {
          return MMRet{maxMove, maxScore};
        }
        if(depth == searchDepth) {
          printf("%safter -- score: %d maxScore: %d maxMove: %s\n", blackArr, res.score, maxScore, MoveToStr(maxMove));
        }
        alpha = max(maxScore, alpha);
      }
      return MMRet{maxMove, maxScore};
    }
    else {
      int minScore = INT_MAX;
      Coord minMove = {-1, -1};
      for(Coord move: candMoves) {
        fprintf(log, "%sbefore -- depth: %d move: %s role: %c minScore: %d minMove: %s alpha: %d, beta: %d\n", blackArr, depth, MoveToStr(move), role, minScore, MoveToStr(minMove), alpha, beta);
        State tmpState(state);
        tmpState.MakeMove(move, role);
        res = AlphaBeta(tmpState, alpha, beta, depth-1, nextRole, log);
        if(res.score < minScore) {
          minScore = res.score;
          minMove = move;
        }
        fprintf(log, "%safter -- score: %d minScore: %d minMove: %s\n", blackArr, res.score, minScore, MoveToStr(minMove));
        if(minScore <= alpha) {
          return MMRet{minMove, minScore};
        }
        beta = min(minScore, beta);
      }
      return MMRet{minMove, minScore};
    }
  }
  return MMRet{Coord{0, 0}, 0};
}

int main() {
  FILE *log;
  log = fopen("log_c++.txt", "w");
  float remTime;
  string roleStr;
  State state;
  auto start = chrono::high_resolution_clock::now();
  ReadInput(remTime, roleStr, state, "input/input20.txt");
  initBoard = state;
  char role = (roleStr == "BLACK" ? 'b' : 'w');
  globRole = role;
  // if(remTime > 200) {
  //   searchDepth = 4;
  // }
  // else if(remTime <= 200 && remTime > 100) {
  //   searchDepth = 3;
  // }
  // else if(remTime <= 100 && remTime > 50) {
  //   searchDepth = 3;
  // }
  // else if(remTime <= 50 && remTime > 20) {
  //   searchDepth = 3;
  // }
  // else {
  //   searchDepth = 2;
  // }
  MMRet res = AlphaBeta(state, INT_MIN, INT_MAX, searchDepth, role, log);
  printf("(%d, %d)\n", res.coord.row, res.coord.col);
  WriteCoord(res.coord, "output.txt");
  auto stop = chrono::high_resolution_clock::now();
  auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  cout << duration.count() << endl;
  fclose(log);

  // int sample[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20};
  // int sample[] = {20};
  // string inPath, outPath;
  // for(int i: sample) {
  //   State state;
  //   cout << i << endl;
  //   auto start = chrono::high_resolution_clock::now();
  //   inPath = "input/input" + to_string(i) + ".txt";
  //   outPath = "output/output" + to_string(i) + ".txt";
  //   ReadInput(remTime, roleStr, state, inPath);
  //   initBoard = state;
  //   char role = (roleStr == "BLACK" ? 'b' : 'w');
  //   globRole = role;
  //   cout << "searchDepth: " << searchDepth << endl;
  //   MMRet res = AlphaBeta(state, INT_MIN, INT_MAX, searchDepth, role, log);
  //   cout << MoveToStr(res.coord) << endl;
  //   WriteCoord(res.coord, outPath);
  //   auto stop = chrono::high_resolution_clock::now();
  //   auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
  //   cout << (float)duration.count()/1000000 << endl;
  // }
  return 0;
}