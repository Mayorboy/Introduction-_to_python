import re
hand= open ("actual-data.txt")
list_of_ints = []
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    
    for num in x:
            
            if num not in list_of_ints :
                
                list_of_ints.append(int(num))
print(sum(list_of_ints))
                 
