#Write a function to find the smallest value in a list find smallest in a list of items

def find_smallest(l):
    current_small = l[0]
    for item in l[1:]:
        if item < current_small:
            current_small = item
    return current_small
#test function
l=[8,6,-4]
result=find_smallest(l)
print ("This is the smallest number", result)
#Write a function that returns a new list that contains all the odd items in the original list

#empty lists
list=[]
new_list=[]
#get all odd nums
def odds (list):
  for num in list:
    if num % 2 !=0:
      new_list.append(num)
  return new_list
#test function
new_list= odds(list=[4,5,6,8,9])
print (new_list)
      

#Write a function that takes a string and returns a new string where all the words are capitalized.

string= ""
def capitalize_string (string):
  string=string.upper()
  return string
string= capitalize_string("computer")
print (string)
string= capitalize_string("coding")
print (string)

#Write a function that takes a string and returns a new string with every word that's longer than 5 characters turned into uppercase

string= ""
def capitalize_string_5 (string):
  if (len(string))>5:
    string=string.upper()
    return string
  elif (len(string))<5:
    return string
string= capitalize_string_5("computer")
print (string)
string= capitalize_string_5("code")
print (string)

#Write a function that takes a list of numbers and returns a new list with each item squared

def square_list(l):
    result = []
    for item in l:
        result.append(item*item)
    return result



#Write a function that takes two lists of numbers and returns a new list where each item is the corresponding value of the original lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]

#chapter 10 # 10, 11, 12