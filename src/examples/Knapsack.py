from SpAlgo import Knapsack

# this is the knapsack algorithm.

# color code to make the output look stoning
ORANGE_COLOR = '\033[94m'

# code of make the text bold
BOLD_START = '\033[1m'

# code of making text to go back to the normal
NORM = '\033[0m'

# example of weight and value of items
items_weight = [15, 10, 3, 7, 2]
items_value = [30, 25, 2, 6, 0.5]

# define a capacity for knapsack
capacity = 48


""" 
    passing information to the "Knapsack" class:
      * first item must be `capacity`
      * second item must be `weight list`
      * third item must be `value list`
      
      OPTIONAL CHOICES =>
            1. is_crumbly: if items could be crumbled you can make it True to feel the knapsack full.
            2. infinite_item: if there is infinite count of each items make it True.
"""
knapsack = Knapsack(capacity, items_weight, items_value, is_crumbly=True, infinite_item=True)

# getting filled pack of items
pack = knapsack.getPack()

"""
    pack contains a list of items in type of dict that contains `weight` and `value` like this:
      [
      {'weight': ...,
       'value': ...},
        ...]
"""
# get total value of the pack
total_value = knapsack.getTotalValue()

# get used weight of pack
used_weight = knapsack.getUsedWeight()

# get wasted weight or empty space of pack
wasted_weight = knapsack.getWastedWeight()

# get information about crumbled item in pack
crumbled_item = knapsack.getCrumbledItem()

"""
      crumbled item info is a dict that contains `weight` and `value` which are crumbled values and
      `original_weight` and `original_value` which are original value of the item:
            {
            'weight': ...,
            'value': ...,
            'original_weight': ...,
            'original_value': ...,
             }
"""

# we print to see the result
print('--------- Knapsack Algorithm ---------')

# printing the data
print('final Pack', '->', BOLD_START, pack, NORM)

# printing the result
print('The total value of pack is', BOLD_START + ORANGE_COLOR,
      total_value, NORM, 'and used weight of pack is', BOLD_START + ORANGE_COLOR,
      used_weight, NORM, 'and pack\'s empty space is', BOLD_START + ORANGE_COLOR,
      wasted_weight, NORM, '\nthe crumbled item in pack ->', BOLD_START + ORANGE_COLOR,
      crumbled_item, NORM)