def read_file(path):
    result = 0
    global_list = []
    global_cache = set()
    check = True
    with open(path, "r") as f:
        for line in f:
            if check:
                if line == "\n":
                    check = False
                    global_list.sort()
                    continue
                get_range(line, global_list, global_cache)
            else:
                result += check_fresh(int(line), global_list, global_cache)
    return result


def get_range(line, global_list, global_cache):
    l, r = line.split("-")
    global_list.append((int(l), int(r)))
    global_cache.add(int(l.rstrip()))
    global_cache.add(int(r.rstrip()))

def check_fresh(line, global_list, global_cache):
    if line in global_cache:
        return 1
    
    for start, end in global_list:
        if start > line:
            return 0
        if start <= line:
            if end >= line:
                return 1
    return 0



if __name__=="__main__":
    result = read_file("input.txt")
    print(result)