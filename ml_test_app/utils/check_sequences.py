def count_sequence(sequence):
    valid_letters = {'A', 'T', 'C', 'G'}
    sequences_found = 0

    for i in range(len(sequence) - 3):
        if sequence[i].upper() in valid_letters and sequence[i].lower() == sequence[i + 1].lower() == sequence[i + 2].lower() == sequence[i + 3].lower():
            if i + 4 < len(sequence) and sequence[i].lower() == sequence[i + 4].lower():
                continue
            sequences_found += 1

    return sequences_found

def count_rows(grid):
    total_sequences = 0
    for row in grid:
        total_sequences += count_sequence(row)
    return total_sequences

def count_columns(grid):
    total_sequences = 0
    for col in range(len(grid)):
        column = [grid[row][col] for row in range(len(grid))]
        total_sequences += count_sequence(column)
    return total_sequences

def check_diagonals(grid):
    total_sequences = 0
    N = len(grid)
    for d in range(2 * N - 1):
        diag1 = []
        diag2 = []
        for row in range(N):
            col1 = d - row
            col2 = N - 1 - d + row
            if 0 <= col1 < N:
                diag1.append(grid[row][col1])
            if 0 <= col2 < N:
                diag2.append(grid[row][col2])
        total_sequences += count_sequence(diag1)
        total_sequences += count_sequence(diag2)
    return total_sequences

def check_sequences(grid):
    total_sequences = 0
    total_sequences += count_rows(grid)
    total_sequences += count_columns(grid)
    total_sequences += check_diagonals(grid)
    return total_sequences