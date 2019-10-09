#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # max profit so far by default is going to be the first buy
  # you're able to make.
  max_profit_so_far = prices[1] - prices[0]
  # for x in prices:
  #   print(x)
  # need to begin a loop to iterate through prices
  for i in range(len(prices)):
    print(f"prices: outer {prices[i]}")
    #begin second loop to begin calculations
    for j in range(i + 1, len(prices)): # offset by one for new loop
      print(f"prices: inner i {prices[i]}, inner j {prices[j]}")
      #seems like nested loops are confusing.
print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))