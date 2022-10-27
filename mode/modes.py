def findLargest(l):
    current_large = l[0]
    for item in l[1:]:
        if item > current_large:
            current_large = item
    return current_large
#test function
l=[8,6,-4, 56]
result=findLargest(l)
print ("This is the largest number", result)

def freq(l,v):
  frequency=0
  for item in l:
    if item==v:
      frequency= frequency+1
  return frequency

#test the function
l= [1,1,1,1,1,1,1,4,4,4,4,3,3,3,2,2,2,2,5,5,5,1,1,1,1,1,4,4,4,4]
result= freq(l,5)
print(result)

result= freq(l,1)
print(result)