print('Day 11: Seating System - puzzle 2')

import copy

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

rows = []
with open(input_file,"r") as f:
    lines = f.readlines()
    last = lines[-1]

    for line in lines:
      r = line.split('\n')[0]
      row = []
      for i in r:
        row.append(i)
      rows.append(row)

for r in rows:
  print(r)

print()


def get_seats(row, seat):
  global rowscopy
  max_len = len(rowscopy[row])-1
  max_row = len(rowscopy)-1
  seats = []
  # first row
  if row == 0:
    if seat == 0:
      s = seat
      r = row
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

      s = seat
      r = row
      while (s < max_len) and (r < max_row):
        r += 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

    elif seat == max_len:

      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

      s = seat
      r = row
      while s > 0 and (r < max_row):
        r += 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

    else:
      # East
      r = row
      s = seat
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # South
      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SE
      r = row
      s = seat
      while (s < max_len) and (r < max_row):
        r += 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # West
      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SW
      s = seat
      r = row
      while s > 0 and (r < max_row):
        r += 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
  # last row
  elif row == max_row:
    if seat == 0:
      # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # east
      s = seat
      r = row
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NE
      s = seat
      r = row
      while s < max_len and r > 0:
        r -= 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
    elif seat == max_len:
      # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # west
      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NW
      s = seat
      r = row
      while s > 0 and r > 0:
        r -= 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
    else:
      # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # west
      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NW
      s = seat
      r = row
      while s > 0 and r > 0:
        r -= 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # east
      s = seat
      r = row
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NE
      s = seat
      r = row
      while s < max_len and r > 0:
        r -= 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
  # second row to second last row
  else:
    # first seat
    if seat == 0:
      # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # east
      s = seat
      r = row
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NE
      s = seat
      r = row
      while s < max_len and r > 0:
        r -= 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # South
      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SE
      r = row
      s = seat
      while (s < max_len) and (r < max_row):
        r += 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
    #  last seat
    elif seat == max_len:
      # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NW
      s = seat
      r = row
      while s > 0 and r > 0:
        r -= 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # west
      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SW
      s = seat
      r = row
      while s > 0 and (r < max_row):
        r += 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # South
      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
    # any seat not on borders
    else:
     # north
      s = seat
      r = row
      while r > 0:
        r -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NW
      s = seat
      r = row
      while s > 0 and r > 0:
        r -= 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # west
      s = seat
      r = row
      while s > 0:
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SW
      s = seat
      r = row
      while s > 0 and (r < max_row):
        r += 1
        s -= 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # South
      s = seat
      r = row
      while r < max_row:
        r += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # SE
      r = row
      s = seat
      while (s < max_len) and (r < max_row):
        r += 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # east
      s = seat
      r = row
      while s < max_len:
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break
      # NE
      s = seat
      r = row
      while s < max_len and r > 0:
        r -= 1
        s += 1
        if rowscopy[r][s] == '.':
          continue
        else:
          seats.append(rowscopy[r][s])
          break

  # print(row,seat,seats)
  return seats



def can_occupy_seat(seats):
  count = 0
  for s in seats:
      if s == '#':
        count += 1
  return False if count > 0 else True

def can_empty_seat(seats):
  count = 0
  for s in seats:
      if s == '#':
        count += 1
  return True if count >= 5 else False

done = False
while not done:
  changes = 0
  rowscopy = copy.deepcopy(rows)
  # print('\nrowscopy1:')
  # for r in rowscopy:
  #   print(r)
  # print()

  # print('can occupy ?')
  for row in range(len(rowscopy)):
    for seat in range(len(rowscopy[row])):
      seats = []
      if rowscopy[row][seat] == 'L':
        seats = get_seats(row,seat)
        # print(seats)
        if can_occupy_seat(seats):
          changes += 1
          rows[row][seat] = '#'

  # print('\nrows:')
  # for r in rows:
  #   print(r)

  if changes == 0:
    # print('no more can occupy changes',changes)
    done = True
    break

  changes = 0
  rowscopy = copy.deepcopy(rows)
  # print('\nrowscopy2:')
  # for r in rowscopy:
  #   print(r)
  # print()

  # print('can empty?')
  for row in range(len(rowscopy)):
    for seat in range(len(rowscopy[row])):
      seats = []
      if rowscopy[row][seat] == '#':
        seats = get_seats(row,seat)
        # print(seats)
        if can_empty_seat(seats):
          changes += 1
          rows[row][seat] = 'L'

  # print('\nrows:')
  # print()
  # for r in rows:
  #   print(r)
  if changes == 0:
    # print('no more can empty changes',changes)
    done = True


occupied = 0
for row in range(len(rows)):
  for seat in range(len(rows[row])):
    if rows[row][seat] == '#':
      occupied += 1

for r in rows:
  print(r)

print()

print('Answer to puzzle 1',occupied)

print('Answer to puzzle 2',occupied)
