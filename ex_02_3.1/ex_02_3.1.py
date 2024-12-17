sh = input("Enter Hours:")
fh = float(sh)
sr = input("Enter rate:")
fr = float (sr)
if fh > 40:
    reg= fh * fr
    otp= (fh - 40) * (fr * 0.5)
    gp = reg + otp
else:  
     reg= fh * fr
print (gp)