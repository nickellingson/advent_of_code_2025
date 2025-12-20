# loop through, sliding box... sum up, needs to under four (<4)
    # check if out of bounds

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

    result = 0
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

    return result



if __name__=="__main__":
    matrix = read_file_and_load("test.txt")
    result = count_roll_access(matrix)
    print(result)