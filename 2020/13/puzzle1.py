print('Day 13: Shuttle Search - puzzle 1')

import copy

# input_file = "example_set"
input_file = "input"

def create_time_table(buses,timestamp):
  time_table = []

  # get max bus number
  max = 0
  for b in buses:
    if int(b) > max:
      max = int(b)

  i = 0
  # for every minute until starting timestamp plus the highest bus number + 1
  while i <= (timestamp + max + 1):
    # print(i,timestamp)
    schedule = {}
    for b in buses:
      # print(b)
      schedule[b] = '.'
    time_table.append(schedule)
    i += 1

  # set bus departures
  bn = []
  for k in time_table[0]:
    bn.append(k)

  for n in bn:
    for i in range(len(time_table)):
      if ((i+1) % int(n)) == 0:
        time_table[i+1][n] = 'D'

  return time_table

def print_time_table(time_table):
  for i in range(len(time_table)):
    # print bus header
    bn = []
    if i == 0:
      for k in time_table[i]:
        bn.append(k)

      b = '     '.join(bn)
      print(f'time   {b}')
    else:
      bl = []
      for k in time_table[i]:
        bl.append(time_table[i][k])

      b = '     '.join(bl)
      print(f'{i}     {b}')

def get_next_bus(time_table,timestamp):
  bus = 0
  time = 0
  for i in range(len(time_table)):
    if i < timestamp:
      continue
    else:
      for k in time_table[i]:
        if time_table[i][k] == 'D':
          bus = int(k)
          time = i
          break
    if bus > 0:
      break
  return bus, time


def main():

  earliest_time=0
  answer = 0
  buses = []

  with open(input_file,"r") as f:
      lines = f.readlines()
      # last = lines[-1]

      for l in range(len(lines)):
        line = lines[l].split('\n')[0]
        # print(l,line)
        if l == 0:
          earliest_time = int(line)
        else:
          sl = line.split(',')
          for i in sl:
            if i != 'x':
              buses.append(i)
        # print(lines[l])

  print(buses)
  print(earliest_time)

  time_table = create_time_table(buses,earliest_time)
  print_time_table(time_table)
  bus = get_next_bus(time_table,earliest_time)
  print(f'bus={bus[0]}, timestamp={bus[1]}, earliest_time={earliest_time}, wait={bus[1] - earliest_time}')
  print(f'Answer to puzzle: {(bus[1] - earliest_time) * bus[0]}')


if __name__ == '__main__':
  main()
