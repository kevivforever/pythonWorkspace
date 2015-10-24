list1 = [4,5,6]
stringEx = "random String"

print 4 in list1
print 3 in list1
print "String" in stringEx
print "string" in stringEx


list2 = [0,1,2]
list3 = ['vivek','akansha','Shruti']
list4 = [25,22,21]
list5 = range(1,31)

for i in list2:
    print '%s is %d' % (list3[i],list4[i])

for i in range(1,31):
    print i

for i in list5:
    if (i%2) == 0:
        continue
    elif i == 25:
        break
    else:
        print i
