print('Day 5, puzzle 1 - binary boarding')

from numpy import random

# input_file = "example_set"
input_file = "input"

def parse_position(id,limit,low,high):
    # print(id,limit,low,high)

    seat_range = limit
    start = 0
    end = limit - 1
    for i in id:
        if i == low:
            end = end - int(((end + 1) - start) / 2)
        else:
            start = start + int(((end + 1) - start)/ 2)

    return start


highest_rid = 0
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        # print(line)
        r = parse_position(line[:7],128,'F','B')
        c = parse_position(line[7:],8,'L','R')
        rid = r * 8 + c
        if rid > highest_rid:
            highest_rid = rid
        print('row',r,'col',c,'row id',rid,highest_rid)

print('The highest seat Id:',highest_rid)
