import time


rainbowDict = {"dictionaryword":"correspondinghash"}

testline = "user1 correspondinghash"
startTime = time.time()
startClock = time.clock()
split = testline.split()
if split[1] in rainbowDict:
	print "cracked",__split[0],rainbowDict[__split[1]]
totalTimeNonFunc = (time.time() - startTime)
totalClockNonFunc = (time.clock() - startClock)
print "non function time:",totalTimeNonFunc
print "non function clock:",totalClockNonFunc

def checkHash(line):
	__split = line.split()
	if __split[1] in rainbowDict:
		print "cracked",__split[0],rainbowDict[__split[1]]

startTime = time.time()
startClock = time.clock()
checkHash(testline)
totalTimeFunc = (time.time() - startTime)
totalClockFunc = (time.clock() - startClock)

print "function time:",totalTimeFunc
print "function clock:",totalClockFunc
print "difference in wall:",totalTimeFunc - totalTimeNonFunc
print "difference in clock:",totalClockNonFunc - totalClockFunc
