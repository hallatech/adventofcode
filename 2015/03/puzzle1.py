print('Day 3: ? - puzzle 1')

# input_file = "example"
input_file = "input"

line_count = 0
total = 0

with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1


# print('line_count',line_count)
print('Answer to puzzle',total)
