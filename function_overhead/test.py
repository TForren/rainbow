import time


rainbowDict = {"dictionaryword":"correspondinghash"}

testline = "user1 correspondinghash"

def checkHash(line):
	__split = line.split()
	if __split[1] in rainbowDict:
		print "cracked",__split[0],rainbowDict[__split[1]]

startTime = time.time()
split = testline.split()
if split[1] in rainbowDict:
	print "cracked",__split[0],rainbowDict[__split[1]]
totalTimeNonFunc = (time.time() - startTime)
print "non function time:",totalTimeNonFunc

startTime = time.time()
checkHash(testline)
totalTimeFunc = (time.time() - startTime)
print "function time:",totalTimeFunc
print "difference:",totalTimeFunc - totalTimeNonFunc
