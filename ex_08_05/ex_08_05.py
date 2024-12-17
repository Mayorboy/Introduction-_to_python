name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

words = line.split()

#read line by line
for line in name:
    line = line.rstrip()
    if not line.startswith('From') : continue
   
        
    for word in words:
        

            
           counts[word]= counts.get(word,0) + 1

print(counts)
        