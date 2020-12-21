#! /usr/bin/env python3

print('Day 21: Allergen Assessment - puzzle 1')

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
          # print('init:',a,fi)
        fi = fi.intersection(f['i'])
        # print(a,f['a'])
        # print('food:',a,fi)
    print('Final:',a,fi)
    fa[a] = fi

  print(fa,'\n')
  for k in fa.keys():
    # print('\n',1,k)
    fi = set()
    if len(fa[k]) > 1:
      # print(2,k)
      fi = fa[k]
      for k2 in fa.keys():
        # print(1.2,k2)
        if len(fa[k2]) == 1:
          # print(1.32,k2,fi,fa[k2])
          fi = fi.difference(fa[k2])
      #     print(1.42,k2,fi,fa[k2])

      #   # if len(fa[k2]) > 1 and k2 != k:
      #   #   print(1.31,k2,fi,fa[k2])
      #   #   fi = fi.intersection(fa[k2])
      #   #   print(1.41,k2,fi,fa[k2])
      #   # elif len(fa[k2]) == 1 and k2 != k:
      #   #   print(1.32,k2,fi,fa[k2])
      #   #   fi = fi.difference(fa[k2])
      #   #   print(1.42,k2,fi,fa[k2])

      # print(1.5,fa[k],fi)
      fa[k] = fi
      # print(1.5,fa[k],fi)

  print('\nFinal fa:',fa)
  fa_list = []
  for v in fa.values():
    # print(1,v)
    for a in v:
      # print(2,a,v)
      fa_list.append(a)
  print('allergerns:',fa_list)

  # ingredients = []
  count = 0
  for f in food:
    # print(f['i'])
    for i in f['i']:
      print(1,i,fa_list)
      if i not in fa_list:
        print(2,i,count,fa_list)
        count += 1
        print(3,i,count,fa_list)

  print(f'Answer to puzzle 1: {count}')

if __name__ == '__main__':
  main()
