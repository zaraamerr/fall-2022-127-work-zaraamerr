#exercise 4 chapter 10

import random

def average (numlist):
  """
  parameters: numlist
  returns: avg of nums

  """
  total= 0
  for num in numlist:
    total= total + num
    result = total/len(numlist)
    return result

#exercise 6 chapter 10

xs=[]
for i in range (3):
  xs.append(random.randint(0,50))
def sum_of_squares(xs):
  sum_of_squares=0
  for i in (xs):
    squared= i*i
    sum_of_squares += squared
    return sum_of_squares

print (sum_of_squares(xs))
