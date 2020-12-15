print('Day 15: Rambunctious Recitation - puzzle 2')

# input = [0,3,6]
input = [2,0,1,7,4,14,18]

def main():

  print(input)
  turn = 0
  spoken = 0
  numbers = {}
  turns = []
  while turn < 30000000:
    if turn < len(input):
      spoken = input[turn]
      if numbers.get(spoken) == None:
        numbers[spoken] = 1
    else:
      # print(f'turn={turn+1},last spoken={spoken},times spoken={numbers[spoken]}')
      if numbers.get(spoken) == 1:
        spoken = 0
        numbers[spoken] = numbers[spoken] + 1
      else:
        i = len(turns)-1
        last_found = False
        last = 0
        before = 0
        while i > -1:
          # print(i,last, before,last_found,turns[i], spoken)
          if not last_found:
            if turns[i] == spoken:
              last = i+1
              last_found = True
          else:
            if turns[i] == spoken:
              before = i+1
              break
          i -= 1
        spoken = last - before
        # print(i,last,before,spoken)
        if numbers.get(spoken) == None:
          numbers[spoken] = 1
        else:
          numbers[spoken] = numbers[spoken] + 1


    turns.append(spoken)
    # print(f'turn={turn+1},spoken={spoken},turns={turns}')
    turn += 1
    print(turn)

  print(numbers)
  print(turns)

  print(f'Answer to puzzle: {spoken}')


if __name__ == '__main__':
  main()
