import math
def parse_line(line, new_start, zero_count):
    rotate_direction = line[0]
    rotate_magnitude = int(line[1:])
    print(rotate_direction, new_start,rotate_magnitude, zero_count)

    if rotate_direction == "R":
        temp = new_start + rotate_magnitude
        new_start = temp % 100
        zero_count += temp // 100
        if temp % 100 == 0:
            zero_count -= 1

    else:
        if new_start == 0 and rotate_magnitude > 0:
            zero_count -= 1
        zero_count += rotate_magnitude // 100
        new_start = new_start - rotate_magnitude % 100
        
        if new_start < 0:
            zero_count += 1
            new_start = new_start + 100


    if new_start == 0:
        zero_count += 1
    return new_start, zero_count


def p1(input_txt, zero_count, initial_start):
    start = initial_start
    with open(input_txt, 'r') as input:
        for line in input:
            start, zero_count = parse_line(line, start, zero_count)
    return zero_count

if __name__=="__main__":
    zero_count = 0
    initial_start = 50
    input_txt = 'input.txt'
    print(p1(input_txt, zero_count, initial_start))