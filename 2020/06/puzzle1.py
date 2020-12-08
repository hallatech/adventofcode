print('Day 6, puzzle 1 - custom customs')

# input_file = "example_set"
input_file = "input"

sum_of_counts=0
new_group = True
no_of_groups = 0
answers = set()
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if len(line) == 1:
            new_group = True
        else:
            new_group = False
            for i in line:
                if i != '\n':
                    answers.add(i)
            print(answers)

        if (line is last) or new_group:
            no_of_groups += 1
            sum_of_counts += len(answers)
            print('Group yes count',len(answers))
            answers = set()

print('No of groups:',no_of_groups)
print('Sum of counts:',sum_of_counts)
