#! /usr/bin/env python3

print('Day 19: Monster Messages - puzzle 1')

import copy

# rules_file = "example_rules"
# messages_file = "example_messages"
rules_file = "input_rules"
messages_file = "input_messages"

def get_rules():
  rules = {}
  with open(rules_file,"r") as f:
    lines = f.readlines()
    for line in lines:
      line = line.split('\n')[0]
      print(line)
      key = int(line.split(':')[0])
      vals = line.split(':')[1][1:]
      if vals.__contains__('a'):
        rules[key] = 'a'
      elif vals.__contains__('b'):
        rules[key] = 'b'
      elif vals.__contains__('|'):
        vls = []
        for i in vals.split('|'):
          vl = []
          for v in i.split(' '):
            if v != '':
              vl.append(int(v))
          vls.append(vl)
        rules[key] = vls
      else:
        vl = []
        for v in vals.split(' '):
          vl.append(int(v))
        rules[key] = vl

  return rules

def get_patterns(rules, next, patterns):
  new_patterns = []
  rule = rules[next]
  # print(f'\nget_pattern: next={next},rule={rule},len(patterns)={len(patterns)}')
  if rule == 'a' or rule == 'b':
    if len(patterns) == 0:
      new_patterns.append(rule)
    elif len(patterns) == 1:
      new_patterns.append(patterns[0] + rule)
    else:
      for i in range(len(patterns)):
        p = patterns[i] + rule
        new_patterns.append(p)
  elif isinstance(rule[0],int):
    new_patterns = copy.deepcopy((patterns))
    for i in rule:
      new_patterns = get_patterns(rules, i, new_patterns)
  else:
    new_left_patterns = copy.deepcopy((patterns))
    new_right_patterns = copy.deepcopy((patterns))
    # print(f'double list case {rule}, {patterns},nlp={new_left_patterns},nrp={new_right_patterns}')
    for i in rule[0]:
      new_left_patterns = get_patterns(rules, i, new_left_patterns)
    for i in rule[1]:
      new_right_patterns = get_patterns(rules, i, new_right_patterns)
    new_patterns = new_left_patterns + new_right_patterns
    # print('end double list case new_patterns',new_patterns)

  # print(f'returning new patterns:{new_patterns},next={next}, {patterns}, len(patterns)={len(patterns)},rule={rule}')
  return new_patterns

def match_rule(message, patterns):
  matched = False
  for pattern in patterns:
    if pattern == message:
      matched = True
  return matched

def process_messages(patterns):
  valid_count = 0
  with open(messages_file,"r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
    # for msg in lines:
      msg = lines[i]
      msg = msg.split('\n')[0]
      # print(i,msg)
      if match_rule(msg,patterns):
        valid_count += 1
        print(f'{i}:{msg}: valid')
      else:
        print(f'{i}:{msg}: failed rule check')

  return valid_count

def main():
  count = 0
  rules = get_rules()
  print(f'rules={rules}')
  patterns = get_patterns(rules,0,[])
  # print(f'patterns={patterns}') # very large for the input so don't print it !
  count = process_messages(patterns)
  print(f'Answer to puzzle: {count}')

if __name__ == '__main__':
  main()
