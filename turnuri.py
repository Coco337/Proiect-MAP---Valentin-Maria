import random

def is_safe(board, row, col):
    # Verifică dacă este în siguranță să plasezi un turn pe poziția (row, col)
    
    # Verifică pe aceeași coloană
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Verifică pe aceeași linie
    for j in range(col):
        if board[row][j] == 1:
            return False
    
    return True

def solve_tower_problem_util(board, row, solutions):
    # Funcție utilitară pentru rezolvarea problemei folosind backtracking
    if row == 8:
        # Am plasat toate cele 8 turnuri
        solutions.append([row[:] for row in board])
        return
    
    for col in range(8):
        if is_safe(board, row, col):
            # Plasează un turn pe poziția (row, col)
            board[row][col] = 1
            
            # Explorează recursiv pentru a plasa turnurile în celelalte rânduri
            solve_tower_problem_util(board, row + 1, solutions)
            
            # Resetează poziția pentru backtracking
            board[row][col] = 0
            
def generate_all_solutions():
    solutions = []
    board = [[0 for _ in range(8)] for _ in range(8)]
    solve_tower_problem_util(board, 0, solutions)
    return solutions

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()
    
# Rezolvă problema celor 8 turnuri
all_solutions = generate_all_solutions()

if all_solutions:
    print(f"Numărul total de soluții: {len(all_solutions)}\n")
    
    # Afișează o soluție aleatoare
    random_solution = random.choice(all_solutions)
    print("Una dintre solutii:")
    print_board(random_solution)
else:
    print("Nu există soluții.")
