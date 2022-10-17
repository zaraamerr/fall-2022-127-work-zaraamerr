# mad libs project !!!

#parts of speech: you can do either just nouns as a category or divide the nouns category into subcategories like plural nouns, singular nouns, proper nouns, etc. it doesn't matter so much if the tense or the usage of the speech doesn't make sense grammatically within the story, as long as the code works.

#past verbs:
#present verbs:
#future verbs:
#singular nouns:
#plural nouns:
#proper nouns:
#adjectives:
#adverbs:
#animals:


#open data file: open()
#read the entire data file: .read()
#read text line by line: .readline()

f = open('madlibsstory.txt')
data = f.read()
words_from_data = data.split()
lines_from_data = data.split('\n')

print (words_from_data)
print(lines_from_data)

f.close()
f = open('madlibsstory.txt')
lines = f.readlines()
print (lines)
# we can strip out the newlines from
# lines

# adding a line without a newline
# just to show
lines.append("This line has no newline")
stripped = []
for line in lines:
    stripped.append(line.strip())
print (lines)