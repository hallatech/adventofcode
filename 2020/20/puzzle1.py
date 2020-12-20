#! /usr/bin/env python3

print('Day 20: Jurassic Jigsaw - puzzle 1')

from tile import Tile

# input_file = "example"
input_file = "input"

def get_tiles():
  file_data = open(input_file).read().splitlines()
  tiles = {}
  id = 0
  data = []
  row = 0
  for line in file_data:
    if len(line) < 1:
      rows = data
      t = Tile(id,rows)
      tiles[id] = t
      continue
    elif line.__contains__('Tile'):
      id = int(line.split(' ')[1][:-1])
      data = []
    else:
      data.append(line)
  rows = data
  t = Tile(id,rows)
  tiles[id] = t

  return tiles

def find_neighbours(tiles):
  for id in tiles:
    tile = tiles[id]
    ttest = 0
    while ttest <= 4:
      if ttest in [1,2,3]:
        tile.rotate()
      elif ttest == 4:
        tile.rotate()
        tile.flip()

      for t_id in tiles:
        t = tiles[t_id]
        if t.id == tile.id:
          continue
        test = 0
        while test < 4:
          if test in [1,2,3]:
            t.rotate()
          elif test == 4:
            t.flip()

          if tile.get_left() == t.get_right():
            tile.left.add(t.id)
          if tile.get_right() == t.get_left():
            tile.right.add(t.id)
          if tile.get_top() == t.get_bottom():
            tile.above.add(t.id)
          if tile.get_bottom() == t.get_top():
            tile.below.add(t.id)
          test += 1
      ttest += 1
    u = set()
    for s in [tile.above, tile.below, tile.left, tile.right]:
      for i in s:
        u.add(i)
    tile.surrounded_sides = len(u)

def get_tiles_with_sides(tiles,no_of_surrounded_sides):
  result = []
  for id in tiles:
    if tiles[id].surrounded_sides == no_of_surrounded_sides:
        result.append(id)
  return result

def get_corners(tiles):
  return get_tiles_with_sides(tiles,2)

def main():
  tiles = get_tiles()
  print(f'No of tiles: {len(tiles)}')
  find_neighbours(tiles)
  for id in tiles:
    tile = tiles[id]
    print(tile.id,
          'max len side:',
          max(len(tile.above),len(tile.right),len(tile.below),len(tile.left)),
          'surrounded sides:',tile.surrounded_sides,
          tile.above,tile.right,tile.below,tile.left,)

  answer = 1
  for i in get_corners(tiles):
    answer *= i
  print(f'Answer to puzzle 1: {answer}')

if __name__ == '__main__':
  main()
