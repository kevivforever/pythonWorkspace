dict1 = {"Name":'vivek',"Age": 26,"Height": "5'8", "Weight": 70}

print dict1

#fetching the value of particular key
print dict1.get("Height")

#printing all key value pair
print dict1.items()

#removes the value from dictionary
dict1.pop("Weight")
print dict1
