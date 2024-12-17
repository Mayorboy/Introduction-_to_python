name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhandle = open(name)

count = dict()
 
#read line by line
for line in fhandle:
   
    line = line.rstrip()
    
 
#set conditionals which starts with From containing the hour

    if not line.startswith('From ') : continue
        
#Split words
    
    words = line.split()
    
    #Extract hours only.
    
    time = words[5]
       
    #Further splitting of time for hours
    
    hour = time.split(':')  
    
    #For hours only
    hrs = hour[0]    
        
 #count hrs
        
    
    
   