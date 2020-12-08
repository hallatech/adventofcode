print('Day 7, puzzle 1 - Handy Haversacks')

# input_file = "example_set"
input_file = "input"

num_bag_colors = 0
line_count = 0
bags = set()
bags_containing_other_bags = {}

def find_gold(key):
    global bags_containing_other_bags

    if len(bags_containing_other_bags[key]) == 0:
        print('no bags - False')
        return False
    elif bags_containing_other_bags[key].__contains__('shiny gold'):
        print('found gold - True')
        return True
    else:
        for i in bags_containing_other_bags[key]:
            print('finding deeper - ', i)
            if find_gold(i):
                return True



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
                    bags_containing_other_bags[bag_color] = set()
                else:
                    bag_color2 = phrase.split()[5] + ' ' +phrase.split()[6]
                    bags_containing_other_bags[bag_color] = set()
                    bags_containing_other_bags[bag_color].add(bag_color2)
            else:
                bag_color2 = phrase.split()[1] + ' ' +phrase.split()[2]
                bags_containing_other_bags[bag_color].add(bag_color2)


print('line_count',line_count)
print('bag colors',bags)
print('bag color count',len(bags))
print('bags_containing_other_bags',bags_containing_other_bags)
print('the number of bag colors:',num_bag_colors)

# holds shiny gold directly
can_hold_shiny_gold = 0
for k in bags_containing_other_bags:
    for i in bags_containing_other_bags[k]:
        if i == 'shiny gold':
            can_hold_shiny_gold += 1

print('can_hold_shiny_gold directly',can_hold_shiny_gold)

# find the max depth
can_hold_shiny_gold = 0
for k in bags_containing_other_bags:
    print('\nsearching',k,'for shiny gold')
    if find_gold(k):
        print('path from', k, 'leads to shiny gold')
        can_hold_shiny_gold += 1

print('No of bag paths leading to shiny gold',can_hold_shiny_gold)
