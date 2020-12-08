print('Day 2, puzzle 1 - password format check')

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
        out = {x : password.count(x) for x in set(password)}
        if letter in out:
            if out[letter] >= min and out[letter] <= max:
                count_matches+=1

print('password pattern matches =',count_matches)
