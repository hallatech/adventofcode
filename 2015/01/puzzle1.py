print('Day 1, puzzle 1 - Not Quite Lisp')

# input_file = "example"
input_file = "input"

line_count = 0
floor = 0

with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        print('length',len(line))
        line_count += 1

        for i in line:
            if i == '(':
                floor += 1
            elif i == ')':
                floor -= 1

print('Answer to puzzle',floor)
