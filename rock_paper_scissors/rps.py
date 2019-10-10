#!/usr/bin/python

import sys
import itertools

# recursion
# whatever n is, is the amount of "plays" (meaning combinations that could occur given the amount of plays)
# define a list of all rock paper scissors plays
plays = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
  print(n)
  #list creates a list of the whatever is passed in through prepending with list
  test = list(itertools.permutations(plays, n))  #plays is the iterable
  # n is the recursive amount of permutations
  return list(list(x) for x in test) #why is this list of list not being a list of lists?
  pass 

print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

#from cs22_help chan
    """
    [“rock”]
    [“rock”, “rock”]
        [“rock”, “rock”, “rock”]
            --> go as many layers as you want
        [“rock”, “rock”, “paper”]
            --> go as many layers as you want
        [“rock”, “rock”, “scissors”]
            --> go as many layers as you want
    [“rock”, “paper”]
        [“rock”, “paper”, “rock”]
        [“rock”, “paper”, “paper”]
        [“rock”, “paper”, “scissors”]
    [“rock”, “scissors”]
        [“rock”, “scissors”, “rock”]
        [“rock”, “scissors”, “paper”]
        [“rock”, “scissors”, “scissors”]
[“paper”]
    …etc
[“scissors”]
    …etc
"""