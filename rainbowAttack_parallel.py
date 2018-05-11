import time,json
from joblib import Parallel, delayed
import multiprocessing

num_cores = multiprocessing.cpu_count()

rainbow = open("dictionary_rainbow.csv","r")
passwordsfile = open("shadowFile.csv","r")
rainbowDict = {}

for line in rainbow:
    split = line.split()
    rainbowDict[split[1]] = split[0]

passwords = passwordsfile.readlines()
rainbow.close()
passwordsfile.close()

userTuples = {}
discovered = {}

print "passwords:", len(passwords)
print "cores:", num_cores
 
startTime = time.time()
startClock = time.clock()

def checkHash(line):
    __split = line.split()
    if __split[1] in rainbowDict:
	print "cracked:",__split[0],rainbowDict[__split[1]]

Parallel(n_jobs=num_cores)(delayed(checkHash)(line) for line in passwords)

"""
for line in passwords:
    split = line.split()
    if split[1] in rainbowDict:
        print "cracked:", split[0]], rainbowDict[split[1]]
"""
totalTime = (time.time() - startTime)
totalClock = (time.clock() - startClock)
print totalTime,"seconds"
print totalClock,"clock"


#crackedPassFile = open("crackedAccounts.txt","w+")
#for user in discovered:
#	crackedPassFile.write(user + " " + discovered[user] + "\n")
#crackedPassFile.close()
