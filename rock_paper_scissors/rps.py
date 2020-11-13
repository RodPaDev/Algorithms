#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possible_plays = ["rock", "paper", "scissors"]
  result = []
  def play_round(rounds, in_result = []):
    if rounds == 0:
      result.append(in_result)
      return

    for play in possible_plays:
      play_round(rounds - 1, in_result + [play])

  play_round(n)
  return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')