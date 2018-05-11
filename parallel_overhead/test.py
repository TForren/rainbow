import time
from joblib import Parallel, delayed
import multiprocessing

num_cores = 1
input_list = range(0,1000)
result = []
def func(i):
	return i * i 

startTime = time.time()
startClock = time.clock()
result = Parallel(n_jobs=num_cores)(delayed(func)(i) for i in input_list)
totalTime = (time.time() - startTime)
totalClock = (time.clock() - startClock)
print "total Time joblib:",totalTime
print "total clock joblib:",totalClock


startTime = time.time()
startClock = time.clock()
result = [(i * i) for i in input_list]
totalTime = (time.time() - startTime)
totalClock = (time.clock() - startClock)
print "total time serial:", totalTime
print "total clock serial", totalClock
