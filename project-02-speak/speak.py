#pirate speak project-- solo

from pirate import english_to_pirate #import translations

f= open('input.txt') #open story
text= f.read() #store the story into variable 'text'
englishwords= text.split() #split text into individual words

new_words=[] #empty list

for word in englishwords: #iterate thru list of words
  if word in english_to_pirate: #check if word is in pirate dictionary
    new_words.append(english_to_pirate[word]) #if TRUE append the value for the key to new word list
  else: 
    new_words.append(word) #if FALSE append original word

new_text= ' '. join(new_words)
print (new_text)


