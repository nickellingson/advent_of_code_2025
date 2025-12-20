def get_input(file):
    result = 0
    with open(file, "r") as f:
        for line in f:
            if res := get_max_batteries(line):
                result += res
    return result
    
def get_max_batteries(line):
    clean_line = line.strip()

    n = len(clean_line)
    stack = []
    for i, d in enumerate(clean_line):
        # remaining digits including current position = n - i
        # 5 2   <- 6  pop both
        while stack and d > stack[-1] and (len(stack) - 1 + (n - i)) >= 12:
            stack.pop()
        if len(stack) < 12:
            stack.append(d)
    return int("".join(stack))


if __name__=="__main__":
    total = get_input('input.txt')
    print()
    print(total)