import math
import random

#abs
print "abs function outputs"
print "abs(-45) : ", abs(-45)
print "abs(-45.17) : ", abs(-45.17)
print "abs(100.12) : ", abs(100.12)
print "abs(100.72) : ", abs(100.72)
print "abs(119L) : ", abs(119L)
print "abs(math.pi) : ", abs(math.pi)
print 119L

#cmp()
print"------------------------------------------"
print "cmp function outputs"
print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(100, 100) : ", cmp(100, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)

#ceil
print"------------------------------------------"
print "ceil function outputs"
print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(119L) : ", math.ceil(119L)
print "math.ceil(math.pi) : ", math.ceil(math.pi)

#floor
print"------------------------------------------"
print "floor function outputs"
print "math.floor(-45.17) : ", math.floor(-45.17)
print "math.floor(100.12) : ", math.floor(100.12)
print "math.floor(100.72) : ", math.floor(100.72)
print "math.floor(119L) : ", math.floor(119L)
print "math.floor(math.pi) : ", math.floor(math.pi)

#exp()
print"------------------------------------------"
print "exp function outputs"
print "math.exp(-45.17) : ", math.exp(-45.17)
print "math.exp(100.12) : ", math.exp(100.12)
print "math.exp(100.72) : ", math.exp(100.72)
print "math.exp(119L) : ", math.exp(119L)
print "math.exp(math.pi) : ", math.exp(math.pi)

#fabs()
print"------------------------------------------"
print "fabs function outputs"
print "math.fabs(-45) : ", math.fabs(-45)
print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)

#log()
print"------------------------------------------"
print "log function outputs"
#print "math.log(-100.12) : ", math.log(-100.12)
print "math.log(100.12) : ", math.log(100.12)
print "math.log(100.72) : ", math.log(100.72)
print "math.log(119L) : ", math.log(119L)
print "math.log(math.pi) : ", math.log(math.pi)

#modf()
print"------------------------------------------"
print "modf function outputs"
print "math.modf(100.12) : ", math.modf(100.12)
print "math.modf(100.72) : ", math.modf(100.72)
print "math.modf(119L) : ", math.modf(119L)
print "math.modf(math.pi) : ", math.modf(math.pi)

#pow()
print"------------------------------------------"
print "pow function outputs"
print "math.pow(100, 2) : ", math.pow(100, 2)
print "math.pow(100, -2) : ", math.pow(100, -2)
print "math.pow(2, 4) : ", math.pow(2, 4)
print "math.pow(3, 0) : ", math.pow(3, 0)

#round()
print"------------------------------------------"
print "round function outputs"
print "round(80.23456, 2) : ", round(80.23456, 2)
print "round(100.000056, 3) : ", round(100.000056, 3)
print "round(-100.000056, 3) : ", round(-100.000056, 3)

#sqrt()
print"------------------------------------------"
print "sqrt function outputs"
print "math.sqrt(100) : ", math.sqrt(100)
print "math.sqrt(7) : ", math.sqrt(7)
print "math.sqrt(math.pi) : ", math.sqrt(math.pi)

#choice()
print"------------------------------------------"
print "choice function outputs"
print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')

#randrange()
print"------------------------------------------"
print "randrange function outputs"
# Select an even number in 100 <= number < 1000
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)
# Select another number in 100 <= number < 1000
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)

#random()
print"------------------------------------------"
print "random function outputs"
# First random number
print "random() : ", random.random()
# Second random number
print "random() : ", random.random()

#seed()
print"------------------------------------------"
print "seed function outputs"
print "Random number with seed 10 : ", random.random()
print "Random number with seed 10 : ", random.random()
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
print "Random number with seed 10 : ", random.random()
print "Random number with seed 10 : ", random.random()
# It will generate same random number
random.seed( 20 )
print "Random number with seed 20 : ", random.random()
# It will generate same random number
random.seed( 30 )
print "Random number with seed 30 : ", random.random()

#shuffle()
print"------------------------------------------"
print "shuffle function outputs"
list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list
random.shuffle(list)
print "Reshuffled list : ",  list

#uniform()
print"------------------------------------------"
print "uniform function outputs"
print "Random Float uniform(5, 10) : ",  random.uniform(5, 10)
print "Random Float uniform(7, 14) : ",  random.uniform(7, 14)
