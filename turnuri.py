import random

def is_safe(board, row, col):
    # Verify if it's safe to place Tower
    
    # Verify Column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Verify Line
    for j in range(col):
        if board[row][j] == 1:
            return False
    
    return True

def solve_tower_problem_util(board, row, solutions):
    if row == 8:
        # We placed all 8 Towers
        solutions.append([row[:] for row in board])
        return
    
    for col in range(8):
        if is_safe(board, row, col):
            # Place a Tower (row, col)
            board[row][col] = 1
            
            # Placing Towers recursively
            solve_tower_problem_util(board, row + 1, solutions)
            
            # Reset position for backtracking
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
    
# Resolves the problem
all_solutions = generate_all_solutions()

if all_solutions:
    print(f"Total number of solutions: {len(all_solutions)}\n")
    
    # Show a random solution
    random_solution = random.choice(all_solutions)
    print("One of the Solutions:")
    print_board(random_solution)
else:
    print("No solutions exist.")
