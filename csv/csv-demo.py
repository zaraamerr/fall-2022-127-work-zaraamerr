f= open ('demo.csv')
for line in f.readlines():
  print (line)
  line= line.strip()
  print(line.split(","))