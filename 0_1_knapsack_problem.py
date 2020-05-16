#Load required modules
import numpy as np
from __future__ import division

#Generaing input
values = [50,10,5,70,90,79,50,80,70]
weight = [300,50,30,350,365,150,150,195,400]
names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Greedy approach

def greedy(values, weight, names, capacity):
  """Returns a greedy solution

  Args:
  values: Values of items
  weights: Weights of items
  names: Names of items
  capacity: Max capacity of knapsack

  Returns:
  Best greedy solution
  """
  greedy_input_array = [[i,j,k] for i,j,k in zip(values, weight, names)]
  greedy_input_array = sorted(greedy_input_array, key=lambda greedy_input_array_entry: greedy_input_array_entry[0], reverse=True)
  greedy_value = []
  greedy_weight = []
  greedy_names = []
  for i in range(len(values)):
    if sum(greedy_weight) <= capacity:
      greedy_value.append(greedy_input_array[i][0])
      greedy_weight.append(greedy_input_array[i][1])
      greedy_names.append(greedy_input_array[i][2])
    else:
      pass
  out = [greedy_value, greedy_weight, greedy_names]
  out_value = sum(out[0])
  return(out_value)

greedy(values, weight, names, 500)

#Therefore, with the greedy approach 170 is the best value we obtain.

# Brute Force Approach
"""

def brute_force(values, weight, names, capacity, cardinality):
  """Evaluates all options and returns a solution

  Args:
  values: Values of items
  weights: Weights of items
  names: Names of items
  capacity: Max capacity of knapsack
  cardinality: size of the array

  Returns:
  Brute force solution
  """

  if cardinality == 0 or capacity == 0:
    return 0
  if (weight[cardinality - 1] > capacity):
    return brute_force(values, weight, names, capacity, cardinality-1)
  else:
    return max(values[cardinality-1] + brute_force(values, weight, names, capacity - weight[cardinality-1], cardinality-1),
               brute_force(values, weight, names, capacity, cardinality-1))

brute_force(values, weight, names, 500, 9)

#Therefore, with the brute force approach 209 is the best value we obtain.

# Dynammic Programming approach
"""
