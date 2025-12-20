def parse_line(input_arr, sum):
    for index_range in input_arr:
        left, right = index_range.split("-")
        for i in range(int(left), int(right) + 1):
            # get len, slice and dice, compare
            str_index = str(i)
            str_ln = len(str_index)
            if str_ln % 2 == 0:
                left_half = str_index[:str_ln//2]
                right_half = str_index[str_ln//2:]

                if left_half == right_half:
                    sum += i

    return sum

def main():
    with open("input.txt", "r") as f:
        count = 0
        input_str = f.readline()
        input_arr = input_str.split(",")
        count = parse_line(input_arr, count)
        return count

if __name__=="__main__":
    invalid_sum = main()
    print(invalid_sum)