print('Day 8, puzzle 2 - Handheld Halting corrupted')

import copy

# input_file = "example_set"
input_file = "input"

line_count = 0
acc = 0
origin_ops = []
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1
        op = line.split()[0]
        val = int(line.split()[1])
        origin_ops.append({'op':op,'val':val})
        print(line)

print('line_count',line_count)
print(origin_ops)


for j in range(len(origin_ops)):
    is_looper = False
    ops = copy.deepcopy(origin_ops)

    if ops[j]['op'] == 'nop':
        ops[j]['op'] = 'jmp'
        print('nop change to jmp', ops[j])
    elif ops[j]['op'] == 'jmp':
        ops[j]['op'] = 'nop'
        print('jmp change to nop',ops[j])

    acc = 0
    i = 0
    last = len(ops)
    print(i,last)
    set_of_instr = set()
    while i != last:
        if set_of_instr.__contains__(i):
            print('instr to be repeated',i,'exiting inf loop...')
            is_looper = True
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
    if not is_looper:
        print('bad op found')
        break


print('Answer to puzzle',acc)
