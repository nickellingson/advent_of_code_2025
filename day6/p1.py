

def read_file(file, global_matrix):
    with open(file, "r") as f:
        for line in f:
            global_matrix.append(handle_line(line))
    return global_matrix

def handle_line(line):
    temp_lst = line.split()
    return temp_lst

def compute(global_matrix):
    ROWS, COLS = len(global_matrix), len(global_matrix[0])
    result = 0
    for c in range(COLS):
        operation = global_matrix[ROWS - 1][c]
        if operation == "*":
            rolling = 1
        else:
            rolling = 0
        for r in range(ROWS - 1):
            if operation == "*":
                rolling *= int(global_matrix[r][c])
            else:
                rolling += int(global_matrix[r][c])
        result += rolling
    return result
        
if __name__=="__main__":
    global_matrix = []
    global_matrix = read_file("input.txt", global_matrix)
    print(compute(global_matrix))
