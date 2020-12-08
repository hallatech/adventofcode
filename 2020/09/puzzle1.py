print('Day 9, puzzle 1 - ')

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1
        op = line.split()[0]
        print(line)

print('line_count',line_count)
print('Answer to puzzle',answer)
