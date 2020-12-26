#! /usr/bin/env python3

print('Day 25: Combo breaker - puzzle 1')

# cpk = 5764801
# dpk = 17807724
cpk = 9033205
dpk = 9281649

def main():

  BASE = 7
  MOD = 20201227
  l = 1
  while pow(BASE, l, MOD) != cpk:
    l += 1
  print('card loop size',l)
  print('key',pow(dpk, l, MOD))

  l = 1
  while pow(BASE, l, MOD) != dpk:
    l += 1
  print('door loop size',l)
  print('key',pow(cpk, l, MOD))

if __name__ == '__main__':
  main()
