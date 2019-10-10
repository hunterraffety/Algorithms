#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # we need to compare the values of the matching keys
  # in each dictionary that is coming into the function
  # by looking through each corresponding pair of keys
  # and evaluating the values to see if there are enough
  # ingredients supplied as is required for the recipe.
  # logic:
  # if there are enough ingredients, how many batches
  # can they make? Think about what if you have enough to
  # make two batches worth of one ingredient but not of
  # another.
  # recipe_requirements = set(recipe.values())
  # ingredients_requirements = set(ingredients.values())
  # test = set(recipe_requirements).intersection(set(ingredients_requirements))
  # for i in recipe_requirements:
  #   print(i)
  # for j in ingredients_requirements:
  #   print(j)
  # for k in test:
  #   pass
  #   # print(k)
  # pass
  batches = 0

  for key, value in recipe.items():
    print(key, value)
    if key in ingredients:
      print(ingredients[key], value)
      #i am able to see both values in the recipe and ingredients now. at this point 
  # these are not in the same order

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))