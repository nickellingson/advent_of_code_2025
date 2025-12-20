
def read_file(path):
    result = 0
    global_list = []
    with open(path, "r") as f:
        for line in f:
            if line == "\n":
                break
            line = line.strip()
            l, r = line.split("-")
            l = int(l.rstrip())
            r = int(r.rstrip())

            global_list.append((l, r))
        print(len(global_list))
        range_list = get_fresh(global_list)
        print(len(range_list))
        result = count_fresh(range_list)
    return result

def get_fresh(global_list):

# (1,2), (3,4), (5,6), (7,8)

    result_list = []
    i = 0
    j = 1
    global_list.sort()
    while i < len(global_list):

        left, right = global_list[i]
        j = i + 1
        while j < len(global_list):
            left2, right2 = global_list[j]
            if right >= left2:
                right = max(right, right2)
            else:
                break
            j += 1
        result_list.append((left, right))
        i = j
    return result_list

def count_fresh(range_list):
    count = 0
    for left, right in range_list:
        count += (right - left + 1)
    return count  

if __name__=="__main__":
    result = read_file("input.txt")
    print(result)
