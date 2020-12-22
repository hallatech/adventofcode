#! /usr/bin/env python3

print('Day 22: Crab Combat - puzzle 2')

import copy

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

def get_cards_as_string(cards):
  s = ''
  for card in cards:
    s += f'{card},'

  return s[:-1]


def play_round(game, round, p1_cards, p2_cards, previous):
  print('Game:',game,'Round:',round, p1_cards,p2_cards)
  game_over = False
  play1 = p1_cards[0]
  play2 = p2_cards[0]

  s1 = get_cards_as_string(p1_cards)
  s2 = get_cards_as_string(p2_cards)
  # Special case to stop recursion
  m1 = False
  m2 = False
  for i in previous['p1']:
    if i == s1:
      m1 = True
  for i in previous['p2']:
    if i == s2:
      m2 = True
  if m1 and m2:
    print('Game over!')
    game_over = True
    return game_over, round, p1_cards, p2_cards, previous
  else:
    previous['p1'].add(s1)
    previous['p2'].add(s2)

  if len(p1_cards[1:]) >= play1 and len(p2_cards[1:]) >= play2:
    print('Playing a sub-game to determine the winner...')
    sub_game_over, p1c, p2c = play_game(game + 1, copy.copy(p1_cards[1:play1+1]), copy.copy(p2_cards[1:play2+1]))
    if sub_game_over or len(p1c) > 0:
      play1 = 1
      play2 = 0
    else:
      play1 = 0
      play2 = 1

  if play1 > play2:
    c = p1_cards.pop(0)
    p1_cards.append(c)
    c = p2_cards.pop(0)
    p1_cards.append(c)
  else:
    c = p2_cards.pop(0)
    p2_cards.append(c)
    c = p1_cards.pop(0)
    p2_cards.append(c)
  return game_over, round, p1_cards, p2_cards, previous

def play_game(game, p1_cards, p2_cards):
  round = 1
  previous = {'p1': set(), 'p2': set()}
  game_over = False
  while len(p1_cards) > 0 and len(p2_cards) > 0:
    game_over, round, p1_cards, p2_cards, previous = play_round(game, round, p1_cards, p2_cards, previous)
    if game_over:
      break
    round += 1
  return game_over, p1_cards, p2_cards

def get_score(cards):
  count = 0
  length = len(cards)
  for card in cards:
    count += card * length
    length -= 1
  return count

def main():
  p1_cards, p2_cards = get_cards()
  game_over, p1_cards, p2_cards = play_game(1, p1_cards, p2_cards)

  score = 0
  print(game_over, p1_cards, p2_cards)
  if game_over or len(p1_cards) > 0:
    score = get_score(p1_cards)
  else:
    score = get_score(p2_cards)

  print(f'Answer to puzzle 1: {score}')

if __name__ == '__main__':
  main()
