def read_file_and_load(path):
    matrix = []
    with open(path, "r") as f:
        for line in f:
            temp_line = []
            line = line.rstrip()
            for c in range(len(line)):
                temp_line.append(line[c])
            matrix.append(temp_line)
    return matrix


def count_roll_access(matrix):

    # get_adj = [[-1,-1],[-1,1],[1,-1],[1,1],[-1,0],[0,-1],[1,0],[0,1]]

    ROWS, COLS = len(matrix), len(matrix[0])
    epocs = True
    total_res = 0
    while epocs:
        result = 0
        changes = []
        for r in range(ROWS):
            for c in range(COLS):

                # make this O(N) -> perform one shot addition

                count_adj = 0
                if matrix[r][c] == "@":
                    if r - 1 >= 0 and c - 1 >= 0 and matrix[r-1][c-1] == "@":
                        count_adj += 1
                    if r - 1 >= 0 and c + 1 < COLS and matrix[r-1][c+1] == "@":
                        count_adj += 1
                    if r + 1 < ROWS and c - 1 >= 0 and matrix[r+1][c-1] == "@":
                        count_adj += 1
                    if r + 1 < ROWS and c + 1 < COLS and matrix[r+1][c+1] == "@":
                        count_adj += 1
                    if r - 1 >= 0 and matrix[r-1][c] == "@":
                        count_adj += 1
                    if c - 1 >= 0 and matrix[r][c-1] == "@":
                        count_adj += 1
                    if r + 1 < ROWS and matrix[r+1][c] == "@":
                        count_adj += 1
                    if c + 1 < COLS and matrix[r][c+1] == "@":
                        count_adj += 1

                    if count_adj < 4:
                        result += 1
                        changes.append((r,c))

        for change_r, change_c in changes:
            matrix[change_r][change_c] = "."

        total_res += result
        if result == 0:
            epocs = False
            break
    return total_res



if __name__=="__main__":
    matrix = read_file_and_load("input.txt")
    result = count_roll_access(matrix)
    print(result)