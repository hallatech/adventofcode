print('Day 8, puzzle 1 - Handheld Halting')

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

ops = []
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1
        op = line.split()[0]
        val = int(line.split()[1])
        ops.append({'op':op,'val':val})
        print(line)

print('line_count',line_count)
print(ops)

acc = 0
i = 0
last = len(ops)
print(i,last)
set_of_instr = set()
while i != last:
    if set_of_instr.__contains__(i):
        print('instr to be repeated',i,'exiting inf loop...')
        break
    else:
        set_of_instr.add(i)
    instr = ops[i]
    print(i,last,instr['op'],instr['val'])
    if instr['op'] == 'acc':
        acc += instr['val']
        i += 1
    elif instr['op'] == 'jmp':
        i += instr['val']
    else:
        i += 1

print(i,acc)
print('Answer to puzzle',acc)
