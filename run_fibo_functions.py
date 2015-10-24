from timeit import Timer
from fibo_functions import *

t1 = Timer("fib(10)","from fibo_functions import fib")

for i in range(1,41):
	s = "fib(" + str(i) + ")"
	t1 = Timer(s,"from fibo_functions import fib")
	time1 = t1.timeit(3)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from fibo_functions import fibi")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))



t3 = Timer("fib(10)","from fibo_functions import fib")

for i in range(1,41):
	s = "fibm(" + str(i) + ")"
	t3 = Timer(s,"from fibo_functions import fibm")
	time3 = t3.timeit(3)
	s = "fibi(" + str(i) + ")"
	t4 = Timer(s,"from fibo_functions import fibi")
	time4 = t4.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time3, time4, time3/time4))
