# store in matrix including blanks
# running total sum
# running column sum/product
# boolean for all blanks in a column or mult/add symbol
    # new running column sum/product



def read_file(path, mat):

    with open(path, "r") as f:

        for line in f:
            new_line_arr = []
            for c in line[:-1]:
                new_line_arr.append(c)
            mat.append(new_line_arr)

    operations = mat[-1]
    mat = mat[:-1][:]

    return mat, operations


def clean_ops(operations):
    clean_operations = []
    for op in operations:
        if op != " ":
            clean_operations.append(op)
    return clean_operations


def run_sum(global_matrix, operations):
    ROWS = len(global_matrix)
    COLS = len(global_matrix[0])
    op_index = len(operations) - 1
    grand_total = 0
    op = operations[op_index]


    if op == "*":
        running_column_total = 1
    else:
        running_column_total = 0

    for c in range(COLS - 1, -1, -1):

        build_int = ""
        blank_col = True

        for r in range(ROWS):
            if global_matrix[r][c] != " ":
                build_int += global_matrix[r][c]
                blank_col = False
     
        if blank_col:
            grand_total += running_column_total
            op_index -= 1
            op = operations[op_index]
            if op == "*":
                running_column_total = 1
            else:
                running_column_total = 0

            continue

        if op == "*":
            running_column_total *= int(build_int)
        else:
            running_column_total += int(build_int)

    # first col doesn't have blank col in front of it
    grand_total += running_column_total

    return grand_total


if __name__=="__main__":
    global_matrix = []
    path = "input.txt"
    global_matrix, operations = read_file(path, global_matrix)
    operations = clean_ops(operations)
    # print(global_matrix)
    # print(operations)
    print("Num of operations:", len(operations))
    print()
    print(run_sum(global_matrix, operations))