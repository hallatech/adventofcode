print('Day 6, puzzle 2 - custom customs')

# input_file = "example_set"
input_file = "input"

sum_of_counts=0
new_group = True
no_of_groups = 0
answers = {}
all_answers = set()
group_count = 0
all_answer_count = 0
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]
    for line in lines:
        if len(line) == 1:
            new_group = True
        else:
            new_group = False
            group_count += 1
            for i in line:
                if i != '\n':
                    if i in answers:
                        answers[i] = answers[i] + 1
                    else:
                        answers[i] = 1
            print(answers)

        if (line is last) or new_group:
            no_of_groups += 1
            for k in answers:
                if answers[k] == group_count:
                    all_answer_count += 1
                    sum_of_counts += 1

            print('Group count',group_count)
            print('Group yes count',len(answers))
            print('Group all_yes count',all_answer_count)
            answers.clear()
            group_count = 0
            all_answer_count = 0

print('No of groups:',no_of_groups)
print('Sum of counts:',sum_of_counts)
