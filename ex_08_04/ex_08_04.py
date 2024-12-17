fname = input("Enter file name: ")
fh = open(fname)
lst = list()

#loop over lines with for loop and split
for line in fh: 
    words = line.split()
    
#loop through splitted words    
    for word in words:
            
            if word not in lst :
                
                lst.append(word)
                 
        
lst.sort()
print(lst)
