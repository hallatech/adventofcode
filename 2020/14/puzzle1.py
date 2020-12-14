print('Day 14: Docking Data - puzzle 1')

import copy

# input_file = "example_set"
input_file = "input"


def decimal_to_binary(n):
  return(format(n,'036b'))

def binary_to_decimal(b):
  return int(b,2)

def mask_it(mask, n):
  masked = []
  for i in n:
    masked.append(i)

  for i in range(len(mask)):
    if mask[i] != 'X':
      if mask[i] == '0':
        masked[i] = '0'
      elif mask[i] == '1':
        masked[i] = '1'
      print(f'i={i},mask[i]={mask[i]},n[i]={n[i]},masked[i]={masked[i]}')

  masked = ''.join(masked)
  print(f'n=     {n}')
  print(f'mask=  {mask}')
  print(f'masked={masked}')

  return masked

def main():

  addresses = {}
  mask = ''

  with open(input_file,"r") as f:
      lines = f.readlines()
      for line in lines:
        line = line.split('\n')[0]
        sl = line.split(' ')
        if sl[0] == 'mask':
          mask = sl[2]
          print(f'new mask={sl[2]}')
        else:
          print(f'mem val={sl[2]}')
          key = sl[0].split('[')[1].split(']')[0]
          val = sl[2]
          bval = decimal_to_binary(int(val))
          print(bval)
          print(mask)
          # print(f'{bval:036}')
          m = mask_it(mask,bval)
          print(m)
          dval = binary_to_decimal((m))
          print(dval)
          addresses[key] = int(dval)

  sum = 0
  for k in addresses:
    sum += addresses[k]

  print(addresses)
  print(mask)
  print(f'Answer to puzzle: {sum}')


if __name__ == '__main__':
  main()
