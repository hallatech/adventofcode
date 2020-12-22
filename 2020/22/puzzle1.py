#! /usr/bin/env python3

print('Day 22: Crab Combat - puzzle 1')

# input_file_p1 = "example_p1"
# input_file_p2 = "example_p2"
input_file_p1 = "input_p1"
input_file_p2 = "input_p2"

def get_cards():
  file_data = open(input_file_p1).read().splitlines()
  p1_cards = []
  for line in file_data:
    p1_cards.append(int(line))

  file_data = open(input_file_p2).read().splitlines()
  p2_cards = []
  for line in file_data:
    p2_cards.append(int(line))

  return p1_cards, p2_cards


def play_round(p1_cards, p2_cards):
  if p1_cards[0] > p2_cards[0]:
    c = p1_cards.pop(0)
    p1_cards.append(c)
    c = p2_cards.pop(0)
    p1_cards.append(c)
  elif p2_cards[0] > p1_cards[0]:
    c = p2_cards.pop(0)
    p2_cards.append(c)
    c = p1_cards.pop(0)
    p2_cards.append(c)
  return p1_cards, p2_cards

def get_score(cards):
  count = 0
  length = len(cards)
  for card in cards:
    count += card * length
    length -= 1
  return count

def main():
  p1_cards, p2_cards = get_cards()
  print(p1_cards,p2_cards)
  round = 1
  while len(p1_cards) > 0 and len(p2_cards) > 0:
    p1_cards, p2_cards = play_round(p1_cards, p2_cards)
    print(round, p1_cards,p2_cards)
    round += 1

  score = 0
  if len(p1_cards) > 0:
    score = get_score(p1_cards)
  else:
    score = get_score(p2_cards)

  print(f'Answer to puzzle 1: {score}')

if __name__ == '__main__':
  main()
