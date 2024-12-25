#!/usr/bin/env python3

def solve_n_queens_dp(n):
    # DP table: stores valid board configurations for placing `row` queens
    dp = [[] for _ in range(n + 1)]
    dp[0] = [[]]  # Base case: one way to place 0 queens

    # Iterate row by row, building configurations
    for row in range(1, n + 1):
        for config in dp[row - 1]:  # Take each valid configuration from the previous row
            for col in range(n):  # Try placing a queen in each column
                if is_safe(config, row - 1, col):
                    dp[row].append(config + [col])

    return dp[n]

def is_safe(board, row, col):
    # Check previous queens for conflicts
    for r, c in enumerate(board):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def print_solutions(n, solutions):
    for solution in solutions:
        for row in solution:
            print(" ".join("Q" if i == row else "." for i in range(n)))
        print("\n")

# Example usage
n = 4
solutions = solve_n_queens_dp(n)
print(f"Found {len(solutions)} solutions for {n}-Queens.")
print_solutions(n, solutions[:1])  # Print the first solution
