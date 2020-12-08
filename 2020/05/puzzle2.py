print('Day 5, puzzle 2 - binary boarding')

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


highest_sid = 0
seat_set = set()
my_seat = 0
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        # print(line)
        r = parse_position(line[:7],128,'F','B')
        c = parse_position(line[7:],8,'L','R')
        sid = r * 8 + c
        seat_set.add(sid)
        if sid > highest_sid:
            highest_sid = sid
        # print('row',r,'col',c,'row id',sid,highest_sid)

    seats = list(seat_set)
    print(seats)
    current_seat = seats[0]

    for i in seats:
        if seats[i+1] - seats[i] == 2:
            my_seat = seats[i] + 1
            break



print('The highest seat Id:',highest_sid)
print('Seat list:',seats)
print('My seat id:',my_seat)
