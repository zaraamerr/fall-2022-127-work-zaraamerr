#pirate speak project // solo
#extra 1: Store your translations in a file named pirate.dat the file should have lines in the form “word:translation.”

import re #helps us split text into words and punctuation

i= open('input.txt') #input
idata= i.read().lower() #reads input and converts whole text to lowercase
iwords= re.findall(r"[\w']+|[.,!?;]", idata) #splits input into individual words and punctuation

#EXTRA 1 BELOW
pirate={} #empty dict
p=open('pirate.dat') 
pdata= p.read() #read data
pwords=pdata.split("\n") #parse thru data 

for i in pwords: #iterate thru the data
  index= i.rfind(":") #find the colon
  pirate[i[0:index]]=i[index+1:] 

new_words=[] #empty list to store new story in
for word in iwords: #iterate thru words in story
  if word in pirate: #if a word in the story matches with a word in the pirate dictionary, append new value from pirate dict to story
    new_words.append(pirate[word])
  else: #if not, append original word
    new_words.append(word)

new_text= ' '.join(new_words)
print (new_text) #new story

#capitalization/punctuation extra
#punc: ['.',',','!', '?', ";"] #establish punctuation to look out for
#for word in iwords:
  #if word.endswith(punc): #if a word has a punctuation mark after it
    