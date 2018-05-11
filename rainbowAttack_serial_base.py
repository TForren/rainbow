import time,json

rainbow = open("dictionary_rainbow.csv","r")
passwordsfile = open("shadowFile.csv","r")
rainbowDict = {}

for line in rainbow:
    split = line.split()
    rainbowDict[split[1]] = split[0]

passwords = passwordsfile.readlines()

rainbow.close()
passwordsfile.close()

discovered = {}

print len(passwords), "passwords read in"
startTime = time.time()

for line in passwords:
    split = line.split()
    if split[1] in rainbowDict:
        discovered[split[0]] = rainbowDict[split[1]]
totalTime = (time.time() - startTime)
print len(discovered),"discovered"
print totalTime,"seconds"

"""
crackedPassFile = open("crackedAccounts.txt","w+")
for user in discovered:
	crackedPassFile.write(user + " " + discovered[user] + "\n")
crackedPassFile.close()
"""
