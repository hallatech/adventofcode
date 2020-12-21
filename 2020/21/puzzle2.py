#! /usr/bin/env python3

print('Day 21: Allergen Assessment - puzzle 2')

# input_file = "example"
input_file = "input"

def get_data():
  file_data = open(input_file).read().splitlines()
  food = []
  all_allergens = set()
  for line in file_data:
    allergens = set()
    ingredients = set()
    all = ((line.split('(')[1])[8:])[:-1]
    if all.__contains__(','):
      for a in all.split(','):
        allergens.add(a[1:])
        all_allergens.add(a[1:])
    else:
      allergens.add(all[1:])
      all_allergens.add(all[1:])

    ings = (line.split(' (')[0]).split(' ')
    for i in ings:
      ingredients.add(i)

    print(all)
    food.append({'i':ingredients, 'a':allergens})

  return food, all_allergens


def main():
  food,all_allergens = get_data()
  print(food)
  print(all_allergens)
  fa = {}
  for a in all_allergens:
    fi = set()
    for f in food:
      if a in f['a']:
        if len(fi) == 0:
          for i in f['i']:
            fi.add(i)
        fi = fi.intersection(f['i'])
    print('Final:',a,fi)
    fa[a] = fi

  print('\nAfter filter:',fa,'\n')
  while True:
    changes = 0
    for k in fa.keys():
      if len(fa[k]) == 1:
        for k2 in fa.keys():
          if k != k2 and len(fa[k2]) > 1:
            fa[k2] = fa[k2].difference(fa[k])
            changes += 1
    if changes == 0:
      break

  print('\nFinal fa:',fa)
  fa_list = []
  for v in fa.values():
    for a in v:
      fa_list.append(a)
  print('allergens:',fa_list)

  count = 0
  for f in food:
    for i in f['i']:
      if i not in fa_list:
        count += 1

  print(f'Answer to puzzle 1: {count}')

  clist = ''
  for k in sorted(fa.keys()):
    print(k,fa[k])
    for i in fa[k]:
      clist += i + ','

  print(f'Answer to puzzle 2: {clist[:-1]}')

if __name__ == '__main__':
  main()
