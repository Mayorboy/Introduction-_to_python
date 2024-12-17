# Use words.txt as the file name

fname = input("Enter file name: ")
fh = open("words.txt")
print(fh)

for lines in fh:
    lx= lines.rstrip()
    print(lx.upper())