print('Day 2: I Was Told There Would Be No Math - puzzle 1')

# input_file = "example"
input_file = "input"

line_count = 0
paper = 0

with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1

        l = int(line.split('x')[0])
        w = int(line.split('x')[1])
        h = int(line.split('x')[2])

        a1 = l*w
        a2 = w*h
        a3 = h*l

        ax = a1 if a1 < a2 else a2
        ss = ax if ax < a3 else a3
        present = 2*a1 + 2*a2 + 2*a3 + ss
        paper = paper + present
        print('l=',l,'w=',w,'h=',h,'a1=',a1,'a2=',a2,'a3=',a3,'slack=',ss,'present=',present,'total=',paper)


# print('line_count',line_count)
print('Answer to puzzle',paper)
