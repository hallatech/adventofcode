print('Day 3, puzzle 1 - how many trees hit in the traversal?')

# input_file = "example_set"
input_file = "input"

trees_hit = 0
posx = 0
line_num = 0

with open(input_file,"r") as f:
    end_move = False
    hit_tree = False
    print(' ',end='')
    for line in f:
        line_num += 1
        marker='O'
        if end_move:
            if line[posx] == '#':
                trees_hit += 1
                marker='X'
                hit_tree = True

            end_move = False
        # print('before: ',line_num, posx, len(line), end_move, hit_tree)
        line = line[:posx] + marker + line[posx+1:]
        print(line)
        posx = posx + 3
        # print('after: ',line_num, posx, len(line), end_move, hit_tree)
        if posx >= len(line)-1:
            posx = posx - len(line) + 1
        end_move = True
        hit_tree = False

print('trees hit =',trees_hit)
