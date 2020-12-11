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

# for r in rows:
#   print(r)

print()
max_len = len(rows[0])-1
max_row = len(rows)-1

def get_north(row, seat):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while r > 0:
    r -= 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_south(row, seat, max_row):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while r < max_row:
    r += 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_east(row, seat, max_len):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while s < max_len:
    s += 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_west(row, seat):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while s > 0:
    s -= 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_southeast(row, seat, max_len, max_row):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while (s < max_len) and (r < max_row):
    r += 1
    s += 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_southwest(row, seat, max_row):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while s > 0 and (r < max_row):
    r += 1
    s -= 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_northwest(row, seat):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while s > 0 and r > 0:
    r -= 1
    s -= 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_northeast(row, seat, max_len):
  global rowscopy
  result = '.'
  s = seat
  r = row
  while s < max_len and r > 0:
    r -= 1
    s += 1
    if rowscopy[r][s] == '.':
      continue
    else:
      result = rowscopy[r][s]
      break
  return result

def get_seats(row, seat):
  global rowscopy, max_len, max_row
  seats = []
  # first row
  if row == 0:
    if seat == 0:
      seats.append(get_east(row, seat, max_len))
      seats.append(get_south(row, seat, max_row))
      seats.append(get_southeast(row, seat, max_len, max_row))
    elif seat == max_len:
      seats.append(get_west(row, seat))
      seats.append(get_south(row, seat, max_row))
      seats.append(get_southwest(row, seat, max_row))
    else:
      seats.append(get_east(row, seat, max_len))
      seats.append(get_south(row, seat, max_row))
      seats.append(get_southeast(row, seat, max_len, max_row))
      seats.append(get_west(row, seat))
      seats.append(get_southwest(row, seat, max_row))
  # last row
  elif row == max_row:
    if seat == 0:
      seats.append(get_north(row,seat))
      seats.append(get_east(row, seat, max_len))
      seats.append(get_northeast(row, seat, max_len))
    elif seat == max_len:
      seats.append(get_north(row,seat))
      seats.append(get_west(row,seat))
      seats.append(get_northwest(row, seat))
    else:
      seats.append(get_north(row,seat))
      seats.append(get_west(row,seat))
      seats.append(get_northwest(row, seat))
      seats.append(get_east(row,seat,max_len))
      seats.append(get_northeast(row, seat, max_len))
  # second row to second last row
  else:
    # first seat
    if seat == 0:
      seats.append(get_north(row,seat))
      seats.append(get_east(row,seat,max_len))
      seats.append(get_northeast(row, seat, max_len))
      seats.append(get_south(row, seat, max_row))
      seats.append(get_southeast(row, seat, max_len, max_row))
    #  last seat
    elif seat == max_len:
      seats.append(get_north(row,seat))
      seats.append(get_northwest(row, seat))
      seats.append(get_west(row,seat))
      seats.append(get_southwest(row, seat, max_row))
      seats.append(get_south(row, seat, max_row))
    # any seat not on borders
    else:
      seats.append(get_north(row,seat))
      seats.append(get_northwest(row, seat))
      seats.append(get_west(row,seat))
      seats.append(get_southwest(row, seat, max_row))
      seats.append(get_south(row, seat, max_row))
      seats.append(get_southeast(row, seat, max_len, max_row))
      seats.append(get_east(row,seat,max_len))
      seats.append(get_northeast(row, seat, max_len))

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
    done = True
    break

  changes = 0
  rowscopy = copy.deepcopy(rows)
  # print('\nrowscopy2:')
  # for r in rowscopy:
  #   print(r)
  # print()

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
    done = True


occupied = 0
for row in range(len(rows)):
  for seat in range(len(rows[row])):
    if rows[row][seat] == '#':
      occupied += 1

# for r in rows:
#   print(r)

print()

print('Answer to puzzle 1',occupied)

print('Answer to puzzle 2',occupied)
