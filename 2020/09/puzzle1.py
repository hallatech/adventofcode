print('Day 9: Encoding Error - puzzle 1')

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

numbers = [] # acting as a queue
number_set = 0
# max = 5 # for example_set
max = 25 # for input
# check_sum = 25
found = False
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        num = int(line.split('\n')[0])
        line_count += 1
        #  check for sum value in queue
        if line_count > max:
            found = False
            for i in range(len(numbers)):
                for j in range(len(numbers)-1):
                    j += 1
                    # print(i,j,numbers[i], '+', numbers[j],'=',num)
                    if numbers[i] + numbers[j] == num:
                        # print('Found:',numbers[i], '+', numbers[j], '=',num)
                        found = True
                        break
                if found:
                    break
            if not found:
                answer = num
                break
        # propagate queue
        if number_set < max:
            number_set += 1
            numbers.insert(0,num) # queue number
        else:
            numbers.pop()
            numbers.insert(0,num) # queue number
        # print(numbers)


# print('line_count',line_count)
print('Answer to puzzle',answer)
