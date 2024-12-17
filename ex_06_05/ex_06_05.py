text = "X-DSPAM-Confidence:    0.8475"
position= text.find (":")
print(position) 
blankposition = text.find (" ",position)
print(blankposition)
host= text[position + 1 : blankposition]
print(host)
#convert to float value