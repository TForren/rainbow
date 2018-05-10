import random

userCount = 1000000

shadowfile = open("shadowFile.csv","w+")
passwordsfile = open("passwords_sha256.csv","r")

basename = "user"
passwords = passwordsfile.readlines()

for i in range(0,userCount):
	username = basename + str(i)
	shadowfile.write(username + " " + random.choice(passwords))	

passwordsfile.close()
shadowfile.close()
