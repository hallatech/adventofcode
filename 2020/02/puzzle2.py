print('Day 2, puzzle 2 - password format check positions')

# input_file = "example_set"
input_file = "input"

count_matches = 0

with open(input_file,"r") as f:
    for line in f:
        words = line.split()
        min = int(words[0].split('-')[0])
        max = int(words[0].split('-')[1])
        letter = words[1][0]
        password = words[2]
        if (password[min-1] == letter or password[max-1] == letter) and password[min-1] != password[max-1]:
            count_matches+=1

print('password pattern matches =',count_matches)
