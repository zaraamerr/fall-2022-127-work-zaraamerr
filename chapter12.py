#exercise 1: Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. 

sentence= input("Enter a sentence: ")
sentence= sentence.lower()
alphabet= "abcdefghijklmnopqrstuvwxyz"
letter={}
for char in sentence:
  if char in alphabet:
    letter[char]= letter[char]+1
  else: 
    letter[char]=1

keys= letter.keys()
for char in sorted(keys):
  print (char,letter[char])