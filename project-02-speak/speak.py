#pirate speak project // solo
#extra 1: 

i= open('input.txt') #input
idata= i.read().lower() #reads input and converts whole text to lowercase
iwords= idata.split() #splits input into individual words
punctuation= ['.', ',','!', '?', ';'] 

english_to_pirate={"hi": "ahoy",
"buddy": "matey",
"my": "me",
"traveling": "sailing",
"to": "ta",
"the": "th’",
"ocean": "high seas",
"with": "wit’",
"friends": "hearties",
"yeah": "aye",
"guys": "scurvey dogs",
"are": "be",
"looking": "lookin’",
"for": "fer",
"treasure": "booty",
"don’t know": "dinna",
"where": "whar",
"you": "ye",
"she": "that winsome lass",
"of": "o’",
"dinner": "grub",
"drinks": "claps of thunder",
"until": "‘til",
"drunk": "three sheets to the wind",
"cafeteria": "swill dungeon",
"sea": "briney deep"
}                  


new_words=[]
for word in iwords:
  if word in english_to_pirate:
    new_words.append(english_to_pirate[word])
  else:
    new_words.append(word)

new_text= ' '.join(new_words)
print (new_text)
  