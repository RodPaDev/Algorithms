#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}

def eating_cookies(n, cache=cache):
  if n in cache:
    return cache[n]
  else:
    if n < 0:
      cache[n] = 0
      return 0
    elif n <= 1:
      cache[n] = 1
      return 1
    else:
      result = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
      cache[n] = result
      return result

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')