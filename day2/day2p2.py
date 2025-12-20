
def check_seq(id):
    invalid_id = False
    for i in range(1, len(id)):
        pattern = id[0 : i]
        invalid_id = True
        for j in range(0, len(id), i):
            if len(id) % i == 0:
                if id[j : j + i] != pattern:
                    invalid_id = False
            else:
                invalid_id = False
        if invalid_id:
            break
    return invalid_id            
        

def parse_line(input_arr, sum):
    for index_range in input_arr:
        left, right = index_range.split("-")
        for i in range(int(left), int(right) + 1):
            check = check_seq(str(i))
            if check:
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