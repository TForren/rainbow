import time
x = 0
def inner(i):
    global x
    x = x + i
    
def outer_1():
    for i in range(100000): 
        inner(i)


startTime = time.time()
startClock = time.clock()
outer_1()
totalTimeNonFunc = (time.time() - startTime)
totalClockNonFunc = (time.clock() - startClock)
print "non function time:",totalTimeNonFunc
print "non function clock:",totalClockNonFunc

x = 0
def aggregate(list):
    global x
    for i in list:
        x = x + i

def outer_2():
    aggregate(range(100000))


startTime = time.time()
startClock = time.clock()
outer_2()
totalTimeFunc = (time.time() - startTime)
totalClockFunc = (time.clock() - startClock)
print "function time:",totalTimeFunc
print "function clock:",totalClockFunc
print "difference in wall:",totalTimeFunc - totalTimeNonFunc
print "difference in clock:",totalClockNonFunc - totalClockFunc
