import time,hashlib

def stretchPass(password, salt, r):
	x = "0"
	for i in range(0,r):
		x = hashlib.sha256(x+password+salt).hexdigest()
	return x

outputfile = open("passwords_sha256.csv","w+")
for line in open("passwords_plain.txt","r"):
	outputfile.write(stretchPass(line.strip(),"saltysalt",7) + "\n")

outputfile.close()
