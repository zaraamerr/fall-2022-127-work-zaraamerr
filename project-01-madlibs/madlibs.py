# mad libs project
#EXTRA 1: Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
#EXTRA 2: Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
#EXTRA 3: Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.

#first, let's establish the parts of speech and their respective lists

adjectives=["exciting", "fun", "boring", "breezy", "hot", "cold", "loud", "quiet", "peaceful", "chaotic"]
nouns=["river", "lake", "mountain", "hotel", "beach", "fire department", "ditch", "raveen", "valley"]
verbs=["hiking", "crying", "laughing", "hanggliding", "coding", "swimming", "hurling", "running"]
names=["Tommy", "Jessie", "Lora", "Michael Jackson", "Drake", "Josh", "Betsy"]

#next, let's open the data file
f = open('madlibsstory.txt')
#read the file
data = f.read()
#split it into words
storyContent = data.split()

#then, create variables that hold the value of randomized parts of speech

import random

randadjectives= random.choice(adjectives)
randnouns= random.choice(nouns)
randverbs= random.choice(verbs)
randnames= random.choice(names)

#then, replace the placeholders with the randomly selected parts of speech from the lists

storyContent= [item.replace("<name>", randnames) for item in storyContent]
storyContent= [item.replace("<adjective>", randadjectives) for item in storyContent]
storyContent= [item.replace("<noun>", randnouns) for item in storyContent]
storyContent= [item.replace("<verb-ing>", randverbs) for item in storyContent]

print(storyContent)