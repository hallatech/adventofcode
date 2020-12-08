print('Day 2: I Was Told There Would Be No Math - puzzle 2')

# input_file = "example"
input_file = "input"

line_count = 0
paper = 0
ribbon = 0

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

        # ribbon
        r = 0
        if (l < h and w < h) or (l < h and w == h):
            r = l+l+w+w
        elif (w < l and h < l) or (w < l and h == l):
            r = w+w+h+h
        elif (h < w and l < w) or (h < w and l == w):
            r = l+l+h+h
        elif ( l == h and h == w):
            r = l+l+h+h
        else:
            print('l=',l,'w=',w,'h=',h,'a1=',a1,'a2=',a2,'a3=',a3,'slack=',ss,'present=',present,'total=',paper,'r=',r,'b=',b,'ribbon=',r+b,'tot. ribbon',ribbon)
        # bow
        b = l*w*h

        ribbon = ribbon + r + b

        # print('l=',l,'w=',w,'h=',h,'a1=',a1,'a2=',a2,'a3=',a3,'slack=',ss,'present=',present,'total=',paper,'r=',r,'b=',b,'ribbon=',r+b,'tot. ribbon',ribbon)

print('Answer to puzzle',ribbon)
