#! /usr/bin/env python3

import re

print('Day 18: Operation Order - puzzle 1')

# input_file = "example_set"
input_file = "input"

class Foo():
  def __init__(self, val):
      self.val = val

  # Previously '*' converted to '-', now re-evaluate as '*'
  def __sub__(self,operand):
    return Foo(self.val * operand.val)
  # Add evaluate as '+' as normal
  def __add__(self,operand):
    return Foo(self.val + operand.val)

def get_data():
  file_data = open(input_file).read().splitlines()
  data = []
  for line in file_data:
    data.append(line.rstrip())

  return data

def process(line):
  print(line,'=',eval(line))
  # Use regex to substitute each number with the Foo class wrapping the number
  # the Foo(\1) \1 is a reference to the group of the match. In this case only 1
  # so group = 1 i.e. \1. See https://docs.python.org/2/library/re.html
  line = re.sub(r'(\b[0-9]+\b)',r'Foo(\1)',line)
  #  Use regex to substitute '*' with '-' so it has the same precedence as '+'
  line = re.sub(r'\*','-',line)
  result = eval(line)
  print(line,'=',result.val)
  return result.val

def main():
  input = get_data()
  sum = 0
  for line in input:
    sum += process(line)

  print(f'Answer to puzzle: {sum}')


if __name__ == '__main__':
  main()
