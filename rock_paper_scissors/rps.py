#!/usr/bin/python

import sys


def rock_paper_scissors(n):

  permutations = []

  posible_plays = ["rock", "paper", "scissors"]


  def recursive_case(plays_left, result=[]):
       if plays_left == 0:
          permutations.append(result)
          return False

       for i in posible_plays:
          recursive_case(plays_left -1, result + [i])
  recursive_case(n, [])
  return permutations


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')


 # pseudocodehttps://www.youtube.com/watch?v=ckK92JcyV1Y

 # create two variable named cur_action and result