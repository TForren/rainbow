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

passwordChunks = [] 
chunkSize = (len(passwords) / num_cores)
for i in range(0,num_cores):
    passwordChunks.append(passwords[chunkSize*i:chunkSize*(i+1)])


print "passwords:", len(passwords)
print "cores:", num_cores

"""DEP"""
def checkHash(line):
    __split = line.split()
    if __split[1] in rainbowDict:
	print "cracked:",__split[0],rainbowDict[__split[1]]

def checkChunk(chunk):
    for __line in chunk:
	__split = __line.split()
	if __split[1] in rainbowDict:
		True
		#print "cracked:",__split[0],rainbowDict[__split[1]]

startTime = time.time()
startClock = time.clock()

Parallel(n_jobs=num_cores)(delayed(checkChunk)(chunk) for chunk in passwordChunks)

totalTime = (time.time() - startTime)
totalClock = (time.clock() - startClock)
print totalTime,"seconds"
print totalClock,"clock"

#crackedPassFile = open("crackedAccounts.txt","w+")
#for user in discovered:
#	crackedPassFile.write(user + " " + discovered[user] + "\n")
#crackedPassFile.close()
