print('Day 12: Rain Risk - puzzle 1')

import copy

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

pos = {'x':0,'y':0}
facing = 'E'

with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
      r = line.split('\n')[0]

      d = r[0]
      u = int(r[1:])

      print('current move',d,u)

      if d == 'F':
        if facing == 'E':
          pos['x'] += u
        elif facing == 'W':
          pos['x'] -= u
        elif facing == 'N':
          pos['y'] += u
        else:
          pos['y'] -= u
      elif d in ['L','R']:
        print('new rotation.s',facing,d)
        if d == 'L':
          if facing == 'N':
            if u == 90:
              facing = 'W'
            elif u == 180:
              facing = 'S'
            elif u == 270:
              facing = 'E'
          elif facing == 'S':
            if u == 90:
              facing = 'E'
            elif u == 180:
              facing = 'N'
            elif u == 270:
              facing = 'W'
          elif facing == 'E':
            if u == 90:
              facing = 'N'
            elif u == 180:
              facing = 'W'
            elif u == 270:
              facing = 'S'
          else:
            if u == 90:
              facing = 'S'
            elif u == 180:
              facing = 'E'
            elif u == 270:
              facing = 'N'
        else:
          if facing == 'N':
            if u == 90:
              facing = 'E'
            elif u == 180:
              facing = 'S'
            elif u == 270:
              facing = 'W'
          elif facing == 'S':
            if u == 90:
              facing = 'W'
            elif u == 180:
              facing = 'N'
            elif u == 270:
              facing = 'E'
          elif facing == 'E':
            if u == 90:
              facing = 'S'
            elif u == 180:
              facing = 'W'
            elif u == 270:
              facing = 'N'
          else:
            if u == 90:
              facing = 'N'
            elif u == 180:
              facing = 'E'
            elif u == 270:
              facing = 'S'
        print('new rotation.e',facing,d)
      elif d in ['N','S','E','W']:
        print('new loc.e',facing,d)
        if d == 'E':
          pos['x'] += u
        if d == 'W':
          pos['x'] -= u
        if d == 'N':
          pos['y'] += u
        if d == 'S':
          pos['y'] -= u

      print(pos,facing)


print('Answer to puzzle',abs(pos['x']) + abs(pos['y']))
