#tuple
tuple1 = ('Derek', 35, 'Pittsburgh', 'PA')

print tuple1[2]

#changing the string into tuple
tuple2 = tuple('abcd')

print tuple2
print tuple2[:2]

#list
list1 = ['vivek', 26, 'lucknow', 'UP']
list2 = [1,2,3,4,5,6,7,8,9,0]
#referencing the last value
print list1[-1]

#print the last three
print list1[-3:]

#print the firdt three
print list1[:3]

#[starting index: last index: skip]
print list2[0:10:2]
print list2[1:10:2]

#converting string into list
list3 = list('vivek')
print list3

#adding more elements to list

list3[5:] = ' naik'
print list3

#print list as string
print ''.join(list3)
print ','.join(list3)

#replacing the value at index 2
list2[2] = 13
print list2

#deleting a value
del list2[2]
print list2

#appending the value at end of the list
list2.append(11)
print list2

#removing value from the list using element name
list2.remove(11)
print list2

#removing value from the list using index
list2.remove(list2[3])
print list2

#sort the list
list3.sort()
print list3

#multidimensional list

list4 = [list1,list2,list3]
print list4
print list4[2][1]
