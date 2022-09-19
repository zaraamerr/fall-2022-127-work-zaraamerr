def initialize(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "F. Last"
    """
    result = ""
    # isolate, uppercase and add first init to result
    first = name[0]
    first = first.upper()
    result = result + first + "."

    # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    result = result + ' ' + last
    return result

# test Initialize
result= initialize("james bond")
print("james bond -->", result)

def bondify(name):
    """
    input: a string in the form "first last"
    return:string in the form "Last, First Last"
    """
    result=""
   # find the place where the first and last name are separated by a space
    location= name.find(' ')
   #establish and capitalize the first name
    first= name[0:location]
    first= first.capitalize()
   #establish and capitalize the last name
    last= name[location+1:].capitalize()
   #add first and last name to the result in the form last, first, last
    result= last + "," + " "+ first + " " + last
    return result

#test bondify
result= bondify("james bond")
print ("james bond -->", result)

def piglatin(word):
  """
  input: a string representing a word
  returns: a new string w/ the word in piglatin

  Rules:
  if the first letter is a consonant, move it 
  from the start to the end and add "ay" so
  "hello" becomes "ellohay"

  If the first letter is a vowel, just add "yay"
  to the end.

  try to handle uppercase words
  """
 # establish vowels and consonants
  vowels= ('A', 'E', 'I','O','U', 'Y')
  consonants=('B','C','D','F','G','H','J','K','L','M','N','P''Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z')
  
  result=""

  firstletter= word[0]
  firstletter= firstletter.upper()

  if firstletter in consonants:
    removefirstletter= word[1:len(word)]
    result= removefirstletter + firstletter + "ay"
    return result
  elif firstletter in vowels:
    result= word + "way"
    return result
 
# test piglatin

result= piglatin("cheese")
print ("cheese -->", result)