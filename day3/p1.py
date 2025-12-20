
def get_input(file):
    result = 0
    with open(file, "r") as f:
        for line in f:
            res = get_max_batteries(line)
            result += res
    return result
    
def get_max_batteries(line):
    clean_line = line.strip()
    # 234234234234278

    # first pass get max indexs
    # second pass from index to rest of list
    # return max(append(first_pass, second_pass))

    first_digit = sorted(clean_line)[-1]
    backup_digit = sorted(clean_line)[-2]
    if clean_line.index(first_digit) == len(clean_line) - 1:
        first_digit = backup_digit
    first_pass_max_indexes = []
    for c in range(len(clean_line)):
        if clean_line[c] == first_digit:
            first_pass_max_indexes.append(c)
    second_pass_max_result = 0
    for c in range(len(first_pass_max_indexes)):
        for j in range(first_pass_max_indexes[c] + 1, len(clean_line)):
            second_pass_max_result = max(int(second_pass_max_result), int(clean_line[first_pass_max_indexes[c]] + clean_line[j]))
    return second_pass_max_result


if __name__=="__main__":
    print(get_input('input.txt'))
