#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = prices[1] - prices[0]
  min_price = prices[0]

  i = 1
  while i < len(prices):
    if (prices[i] - min_price) > max_profit:
      max_profit = prices[i] - min_price
    if prices[i] < min_price:
      min_price = prices[i]
    i += 1

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))