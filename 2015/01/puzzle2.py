print('Day 1, puzzle 2 - Not Quite Lisp basement')

# input_file = "example"
input_file = "input"

line_count = 0
floor = 0
count = 0
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        print('length',len(line))
        line_count += 1

        for i in line:
            count += 1
            if i == '(':
                floor += 1
            elif i == ')':
                floor -= 1
            else:
                print('invalid char:',i)
            if floor == -1:
                break
        # print(line)

# print('line_count',line_count)
print('Answer to puzzle',count)
