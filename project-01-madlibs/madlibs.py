# mad libs project
#EXTRA 1: Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.
#EXTRA 2: Add some replacements that are unique, that is, the first time you see them you select on randomly but then you keep reusing that replacement.
#EXTRA 3: Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.

#first, let's establish the parts of speech and their respective lists

adjectiveList=["joyous", "fun", "breezy", "hot", "cold", "loud", "quiet", "peaceful", "chaotic"]
nounList=["river", "lake", "mountain", "hotel", "beach", "fire department", "ditch", "raveen", "valley"]
verb_ing_List=["hiking", "crying", "laughing", "hanggliding", "coding", "swimming", "hurling", "running"]
nameList=["Tommy", "Jessie", "Lora", "Michael Jackson", "Drake", "Josh", "Betsy"]

#next, let's open the data file

#, read it, and split it into words so it's easy to iterate through the text and substitute the parts of speech into the mad libs story.

f = open('madlibsstory.txt')
storywords = f.read()
print (storywords)

#substituting randomized parts of speech into the mad libs story

import random