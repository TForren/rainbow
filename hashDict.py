import md5,time
import hashlib

def stretchPass(password, salt, r):
	x = "0"
	for i in range(0,r):
		x = hashlib.sha256(x+password+salt).hexdigest()
	return x

outputfile = open("dictionary_rainbow.csv","w+")
for line in open("words.txt","r"):
    hexstr = stretchPass(line.strip(),"saltysalt",7)
    outputfile.write(line.strip() + " " + hexstr + "\n")

outputfile.close()
