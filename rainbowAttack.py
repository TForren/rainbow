import time

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

for line in passwords:
    split = line.split()
    if split[1] in rainbowDict:
        discovered[split[0]] = rainbowDict[split[1]]

print len(discovered)
