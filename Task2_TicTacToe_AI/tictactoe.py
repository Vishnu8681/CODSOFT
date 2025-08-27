import math
from typing import List, Optional, Tuple

HUMAN = "X"
AI = "O"
EMPTY = " "

Board = List[str]
def print_board(b: Board) -> None:
    def cell(i):
        return b[i] if b[i] != EMPTY else str(i + 1)
    row = lambda r: f" {cell(3*r)} | {cell(3*r+1)} | {cell(3*r+2)} "
    line = "---+---+---"
    print()
    print(row(0)); print(line)
    print(row(1)); print(line)
    print(row(2))
    print()

def available_moves(b: Board) -> List[int]:
    return [i for i, v in enumerate(b) if v == EMPTY]

def winner(b: Board) -> Optional[str]:
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  
        (0,3,6),(1,4,7),(2,5,8),  
        (0,4,8),(2,4,6)           
    ]
    for a, c, d in wins:
        if b[a] != EMPTY and b[a] == b[c] == b[d]:
            return b[a]
    return None

def terminal(b: Board) -> bool:
    return winner(b) is not None or not available_moves(b)

def evaluate(b: Board, depth: int) -> int:
    w = winner(b)
    if w == AI:
        return 10 - depth   
    if w == HUMAN:
        return depth - 10   
    return 0                

def minimax(b: Board, depth: int, alpha: int, beta: int, maximizing: bool) -> Tuple[int, Optional[int]]:
    if terminal(b):
        return evaluate(b, depth), None

    best_move: Optional[int] = None

    if maximizing:
        best_score = -math.inf
        for m in available_moves(b):
            b[m] = AI
            score, _ = minimax(b, depth + 1, alpha, beta, False)
            b[m] = EMPTY
            if score > best_score:
                best_score, best_move = score, m
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = math.inf
        for m in available_moves(b):
            b[m] = HUMAN
            score, _ = minimax(b, depth + 1, alpha, beta, True)
            b[m] = EMPTY
            if score < best_score:
                best_score, best_move = score, m
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

def ai_pick(b: Board) -> int:
    if b.count(EMPTY) == 9:  
        return 4
    _, move = minimax(b, 0, -math.inf, math.inf, True)
    return move if move is not None else available_moves(b)[0]

def ask_first() -> bool:
    while True:
        ans = input("Do you want to go first? (y/n): ").strip().lower()
        if ans in ("y", "yes"): return True
        if ans in ("n", "no"): return False
        print("Please type y or n.")

def read_human_move(b: Board) -> int:
    while True:
        raw = input("Choose a position (1-9) or 'q' to quit: ").strip().lower()
        if raw == "q":
            print("Quitting game. Bye!")
            raise SystemExit(0)
        if not raw.isdigit():
            print("Enter a number 1-9.")
            continue
        pos = int(raw)
        if not 1 <= pos <= 9:
            print("Pick between 1 and 9.")
            continue
        idx = pos - 1
        if b[idx] != EMPTY:
            print("That spot is taken. Try another.")
            continue
        return idx

def game_loop() -> None:
    print("\n=== Vishnu's Tic-Tac-Toe AI  ===")
    print("You are X, AI is O. Get three in a row to win!")
    board: Board = [EMPTY] * 9
    human_turn = ask_first()
    print_board(board)

    while True:
        if human_turn:
            idx = read_human_move(board)
            board[idx] = HUMAN
        else:
            print("AI is thinking...")
            idx = ai_pick(board)
            board[idx] = AI

        print_board(board)

        w = winner(board)
        if w == HUMAN:
            print("🎉 You win! (That’s rare!)")
            break
        if w == AI:
            print("🤖 AI wins! (Unbeatable strikes again)")
            break
        if not available_moves(board):
            print("🤝 It's a draw!")
            break

        human_turn = not human_turn

if __name__ == "__main__":
    game_loop()
