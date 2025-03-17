"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal) :
  seen = {}
  
  for index, value in enumerate(nums) :
    find_num = goal - value
    if find_num in seen:
      return [seen[find_num], index]
    else :
      seen[value] = index
  
  return None


nums = [4, 5, 6, 2]
goal = 8
print(find_first_sum(nums, goal))