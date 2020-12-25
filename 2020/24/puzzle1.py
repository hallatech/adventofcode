#! /usr/bin/env python3

print('Day 24: Lobby Layout - puzzle 1')
# Assume a x,y co-ord system where the x is normal west|east
#  but y runs diagonal sw/ne so start(0,0) + ne 1 is (0,1) and nw 1 is ()

# input_file = "example"
input_file = "input"

def get_data():
  file_data = open(input_file).read().splitlines()
  data = []
  for line in file_data:
    data.append(line.rstrip())

  return data

def parse_tile(tile,x,y):
  if len(tile) > 0:
    print(tile[0],tile[0:2])
    if tile[0] in ['w','e']:
      if tile[0] == 'w':
        x -= 1
        print('west',x,y)
      else:
        x += 1
        print('east',x,y)
      return parse_tile(tile[1:],x,y)
    elif tile[0:2] in ['sw','se','nw','ne']:
      if tile[0:2] == 'sw':
        y -= 1
        print('southwest',x,y)
      elif tile[0:2] == 'se':
        x += 1
        y -= 1
        print('southeast',x,y)
      elif tile[0:2] == 'nw':
        y += 1
        x -= 1
        print('northwest',x,y)
      else:
        y += 1
        print('northeast',x,y)
      return parse_tile(tile[2:],x,y)
  else:
    return x, y



def flip_tiles(data):
  tiles = []
  for tile in data:
    print(tile)
    x,y = 0,0
    x, y = parse_tile(tile,0,0)
    found = False
    for t in tiles:
      if t['x'] == x and t['y'] == y:
        t['flips'] += 1
        found = True

    if not found:
      tiles.append({'x':x, 'y':y, 'flips':1})

  print(tiles)
  return tiles

def main():
  data = get_data()
  tiles = flip_tiles(data)
  black = 0
  for tile in tiles:
    print(tile)
    if tile['flips'] % 2 != 0:
      black += 1

  print(f'Answer to puzzle 1: {black}')

if __name__ == '__main__':
  main()
