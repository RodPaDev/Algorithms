#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  results = []
  if len(recipe) != len(ingredients):
    return 0

  for key in recipe.keys():
    results.append(ingredients[key] / recipe[key])

  min_batch = min(results)

  if min_batch < 1:
    return 0
  else:
    return math.floor(min_batch)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 10 }
  ingredients = { 'milk': 198, 'butter': 52, 'flour': 10 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))