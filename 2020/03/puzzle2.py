print('Day 3, puzzle 2 - how many trees hit in the traversal?')

# input_file = "example_set"
input_file = "input"

slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
print(slopes)

multiplier_total=1

for slope in slopes:
    across = slope[0]
    down = slope[1]
    lines_down = 0
    posx = 0
    trees_hit = 0
    line_num = 0
    with open(input_file,"r") as f:
        x_end_move = False
        y_end_move = False
        hit_tree = False
        # print(' ',end='')
        for line in f:
            line_num += 1
            marker='O'
            if y_end_move:
                if line[posx] == '#':
                    trees_hit += 1
                    marker='X'
                    hit_tree = True

                y_end_move = False
                x_end_move = False
            # print('before: ',line_num, posx, len(line), y_end_move, hit_tree)
                line = line[:posx] + marker + line[posx+1:]

            # print(line)

            if not x_end_move:
                posx = posx + across
                x_end_move = True

            # print('after: ',line_num, posx, len(line), y_end_move, hit_tree)
            if posx >= len(line)-1:
                posx = posx - len(line) + 1
            hit_tree = False

            lines_down += 1
            if lines_down % down == 0:
                lines_down = 0
                y_end_move = True

            # print('final: ',line_num, posx, len(line), y_end_move, hit_tree, across, down, lines_down)
    print('trees hit =',trees_hit)
    multiplier_total *= trees_hit

print('final multiplier_total:',multiplier_total)
