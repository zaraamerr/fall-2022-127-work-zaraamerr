#pirate speak project -- SOLO
#extra 1: Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”

import re #helps split text into words and punctuation

i= open('input.txt') #open input
idata= i.read() #reads input and converts all text to lowercase
iwords= re.findall(r"[\w']+|[.,!?;]", idata) #splits input into individual words and punctuation

#EXTRA 1 BELOW
pirate={} #empty dict
p=open('pirate.dat') 
pdata= p.read() #read data
pwords=pdata.split("\n") #parse thru data

for i in pwords: #iterate thru the data
  index= i.rfind(":") #set the index as the placement of the colon
  pirate[i[0:index]]=i[index+1:] #put words into dict

#uses dict to translate input from english to pirate speak:
  new_words=[] #empty list to store new input in
  for word in iwords: #iterate thru words in input
    if word in pirate: #if a word in the input matches with a word in the pirate dictionary, append new value from pirate dict to new input
      new_words.append(pirate[word])
    else: #if not, append original word
      new_words.append(word)
new_text= ' '.join(new_words)

print("ORIGINAL TEXT: ", idata)
print("TRANSLATED TEXT:", new_text)