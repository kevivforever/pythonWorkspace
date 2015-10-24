import math

#prints the pi value to 15 decimal points
print '%.15f' %(math.pi)
print '%20f'%(math.pi)
print '%20.15f'%(math.pi)
print '%-25.15f is the value of pi'% (math.pi)

precisionPi = int(raw_input("How precise should pi be: "))
print 'Pi = %.*f' % (precisionPi, math.pi)
