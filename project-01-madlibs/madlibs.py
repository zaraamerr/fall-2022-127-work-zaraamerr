# mad libs project !!!
#EXTRA 1: Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
#EXTRA 2: Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.

#parts of speech

present_verbs=["mixes", "pours", "launches", "hurls", "sips", "gobbles"]
verbs=["eat", "sleep on", "destroy", "love", "run", "stomp on"]
verbs_ending_in_ing=["baking", "constructing", "stomping on", "laughing at", "fighting"]
nouns=["salt", "sugar", "shoe", "broccoli", "computer", "skyscraper", "paint", "pan"]
plural_nouns=["eggs", "phones", "books", "houses", "cups", "tablesp", "friends", "siblings"]
character_names=["Paulina", "Fatima", "Remi", "Mr.Rogers", "Bugs Rabbit"]
adjectives=["awesome", "delicious", "horrific", "lovely", "speedy", "beautiful","necessary", "useless", "silly", "goofy", "goopy", "watery" ]

#open the data file, read it, and split it into words so it's easy to iterate through the text and substitute the parts of speech into the text

f = open('madlibsstory.txt')
storywords = f.read()
print (storywords)

#substituting randomized parts of speech into the mad libs story

import random

def substitute(story, present_verbs, verbs, verbs_ing, nouns, plural_nouns, character_names, adjectives):
  #make the character's name a constant in the story
  character= random.choice(character_names)
  story= story.replace('<CHARACTER>', character)
  storywords= story.split()
  for i in storywords:
  # now the other parts of speech
    if i.find("<ADJECTIVE>"): #find <ADJECTIVE>
      storywords[(storywords.index(i))]= random.choice(plural_nouns)#sub <ADJECTIVE> with an adjective from the list
    if i.find ("<PLRLNOUN>"): #find <PLRLNOUN>
      storywords[(storywords.index(i))]= random.choice(plural_nouns) #sub <PLRLNOUN> with a plural noun from the list
    if i.find ("<NOUN>"): #find <NOUN>
      storywords[(storywords.index(i))]= random.choice(nouns) #sub <NOUN> with a noun from the list
    if i.find ("<VERB-ING>"): #find <VERB-ING>
      storywords[(storywords.index(i))]= random.choice(verbs_ending_in_ing) #sub <VERB-ING> with a verb ending in -ing from the list
    if i.find ("<VERB>"): #find <VERB>
      storywords[(storywords.index(i))]= random.choice(verbs) #sub <VERB> with a verb from the list
    if i.find ("<PRSNTVERB>"): #find <PRSNTVERB>
      storywords[(storywords.index(i))]= random.choice(present_verbs) #sub <PRSNTVERB> with a present verb from the list
      return "".join(story)

print (substitute(storywords,present_verbs,verbs, verbs_ending_in_ing, nouns, plural_nouns, character_names, adjectives))
    
    