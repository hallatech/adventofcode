print('Day 10: Adapter Array- puzzle 1')

# input_file = "example_set"
# input_file = "example_set2"
input_file = "input"

line_count = 0
answer = 0

highest = 0
outlet=0

jd1 = 0
jd2 = 0
jd3 = 0

alist = []
slist = []

# found = False
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        num = int(line.split('\n')[0])
        alist.append(num)
        if num > highest:
            highest = num

        line_count += 1

alist.sort()
print(alist)

for n in range(len(alist)):
    if n == 0:
        if alist[n] == 1:
          jd1 += 1
        if alist[n] == 2:
          jd2 += 1
    if n > 0:
        if alist[n] - alist[n-1] == 1:
          jd1 += 1
    if n > 0 and n < len(alist)-1:
        if alist[n+1] - alist[n] == 2:
          jd2 += 1
    if n < len(alist)-1:
        if alist[n+1] - alist[n] == 3:
          jd3 += 1

# for highest adapter
jd3 += 1

print('jd1',jd1)
print('jd2',jd2)
print('jd3',jd3)
print('highest=',highest)
print('rating',highest+3)
# print('line_count',line_count)
print('Answer to puzzle',jd1 * jd3)
