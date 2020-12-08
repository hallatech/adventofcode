print('Day 7, puzzle 2 - Handy Haversacks bag count')

# input_file = "example_set"
# input_file = "example_set2"
input_file = "input"

num_bag_colors = 0
line_count = 0
bags = set()
bags_containing_other_bags = {}

def count_bags(key, current_count, key_count):
    global bags_containing_other_bags

    # print('Enter with key=',key,'current_count',current_count,'key_count=',key_count)
    if len(bags_containing_other_bags[key]) == 0:
        return key_count
    else:
        level_count = 0
        depth_count = 0
        for i in bags_containing_other_bags[key]:
            depth_count = depth_count + count_bags(i,current_count,bags_containing_other_bags[key][i])

        level_count = current_count + (depth_count * key_count) + key_count
        # print(key,'returning: depth_count',depth_count,'current_count',current_count,'key_count',key_count,'=',level_count)
        return level_count


with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
        line_count += 1
        # print(line)
        phrases = line.split(',')
        for phrase in phrases:
            # print(phrase)
            if phrase.__contains__('contain'):
                bag_color = phrase.split()[0] + ' ' +phrase.split()[1]
                bags.add(bag_color)
                if phrase.__contains__('no other'):
                    bags_containing_other_bags[bag_color] = {}
                else:
                    bag_color2 = phrase.split()[5] + ' ' +phrase.split()[6]
                    bag_count = int(phrase.split()[4])
                    bags_containing_other_bags[bag_color] = {}
                    bags_containing_other_bags[bag_color][bag_color2] = bag_count
            else:
                bag_color2 = phrase.split()[1] + ' ' +phrase.split()[2]
                bag_count = int(phrase.split()[0])
                # bags_containing_other_bags[bag_color].add(bag_color2)
                bags_containing_other_bags[bag_color][bag_color2] = bag_count


# print('line_count',line_count)
# print('bag colors',bags)
# print('bag color count',len(bags))
# print('bags_containing_other_bags',bags_containing_other_bags)
# print('the number of bag colors:',num_bag_colors)

no_of_bags_in_gold = count_bags('shiny gold',0,1) - 1

print('No of bag paths fitting into a shiny gold',no_of_bags_in_gold)
