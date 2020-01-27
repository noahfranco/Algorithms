#!/usr/bin/python

import argparse

def find_max_profit(prices):

   min_price = prices[0]
   max_price = prices[1]
   max_profit = max_price - min_price
   for i in range(1, len(prices)):
     cur_price = prices[i]
     max_profit  = max(cur_price - min_price, max_profit)
     min_price = min(cur_price,  min_price)
   return max_profit

# print(find_max_profit([1, 2, 4, 5, 3, 8, 9, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  # pseudocode

  # step one: write a if statement to compare two index and if there is less then two index return
  # step two: write a for loop with the index and range of length and price
  # step three: