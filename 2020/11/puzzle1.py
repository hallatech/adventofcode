print('Day 11: Seating System - puzzle 1')

import copy

# input_file = "example_set"
input_file = "input"

line_count = 0
answer = 0

rows = []
# found = False
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
  seats = []
  if row == 0:
    if seat == 0:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row][seat+1])
        seats.append(rowscopy[row+1][seat])
        seats.append(rowscopy[row+1][seat+1])
    elif seat == len(rowscopy[row])-1:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row][seat-1])
        seats.append(rowscopy[row+1][seat])
        seats.append(rowscopy[row+1][seat-1])
    else:
      seats.append(rowscopy[row][seat-1])
      seats.append(rowscopy[row][seat+1])
      seats.append(rowscopy[row+1][seat-1])
      seats.append(rowscopy[row+1][seat])
      seats.append(rowscopy[row+1][seat+1])

  elif row == len(rowscopy)-1:
    if seat == 0:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row-1][seat])
        seats.append(rowscopy[row-1][seat+1])
        seats.append(rowscopy[row][seat+1])
    elif seat == len(rowscopy[row])-1:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row][seat-1])
        seats.append(rowscopy[row-1][seat-1])
        seats.append(rowscopy[row-1][seat])
    else:
      seats.append(rowscopy[row-1][seat-1])
      seats.append(rowscopy[row-1][seat])
      seats.append(rowscopy[row-1][seat+1])
      seats.append(rowscopy[row][seat-1])
      seats.append(rowscopy[row][seat+1])
  else:
    if seat == 0:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row-1][seat])
        seats.append(rowscopy[row-1][seat+1])
        seats.append(rowscopy[row][seat+1])
        seats.append(rowscopy[row+1][seat])
        seats.append(rowscopy[row+1][seat+1])
    elif seat == len(rowscopy[row])-1:
      # if rowscopy[row][seat] == 'L':
        seats.append(rowscopy[row][seat-1])
        seats.append(rowscopy[row-1][seat-1])
        seats.append(rowscopy[row-1][seat])
        seats.append(rowscopy[row+1][seat])
        seats.append(rowscopy[row+1][seat-1])
    else:
      seats.append(rowscopy[row-1][seat-1])
      seats.append(rowscopy[row-1][seat])
      seats.append(rowscopy[row-1][seat+1])
      seats.append(rowscopy[row][seat-1])
      seats.append(rowscopy[row][seat+1])
      seats.append(rowscopy[row+1][seat-1])
      seats.append(rowscopy[row+1][seat])
      seats.append(rowscopy[row+1][seat+1])

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
  return True if count >= 4 else False

done = False
while not done:
  changes = 0
  rowscopy = copy.deepcopy(rows)
  print('\nrowscopy1:')
  for r in rowscopy:
    print(r)
  print()

  print('can occupy ?')
  for row in range(len(rowscopy)):
    for seat in range(len(rowscopy[row])):
      seats = []
      if rowscopy[row][seat] == 'L':
        seats = get_seats(row,seat)
        # print(seats)
        if can_occupy_seat(seats):
          changes += 1
          rows[row][seat] = '#'

  print('\nrows:')
  for r in rows:
    print(r)

  if changes == 0:
    print('no more can occupy changes',changes)
    done = True
    break

  changes = 0
  rowscopy = copy.deepcopy(rows)
  print('\nrowscopy2:')
  for r in rowscopy:
    print(r)
  print()

  print('can empty?')
  for row in range(len(rowscopy)):
    for seat in range(len(rowscopy[row])):
      seats = []
      if rowscopy[row][seat] == '#':
        seats = get_seats(row,seat)
        # print(seats)
        if can_empty_seat(seats):
          changes += 1
          rows[row][seat] = 'L'

  print('\nrows:')
  print()
  for r in rows:
    print(r)
  if changes == 0:
    print('no more can empty changes',changes)
    done = True


occupied = 0
for row in range(len(rows)):
  for seat in range(len(rows[row])):
    if rows[row][seat] == '#':
      occupied += 1

print('Answer to puzzle',occupied)
