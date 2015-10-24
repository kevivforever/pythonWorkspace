from types import *
def convert(temp,convt_to_type):
    conversion_type = convt_to_type.upper()
    if conversion_type == 'F':
        temp_in_feh = (9.0/5.0)*(temp + 32)
        print str(temp) + " C = " + str(temp_in_feh) + conversion_type
    else:
        temp_in_cel = (5.0/9.0)*(temp - 32)
        print str(temp) + " " + " F = " + str(temp_in_cel) + conversion_type
    
def checktype(temp,convert_type):
    #if temp and isinstance(temp,int):
    #if temp and type(temp) is IntType:
    if temp and type(temp) == int:
        convert(temp,convert_type)
    else:
        temp = raw_input("Wront temp! Enter the temperature again: ")
        checktype(temp,convert_type)

print "Temperature converter"
temp = int(raw_input("Enter a temperature: "))
convert_type = raw_input("Convert to (F)ahrenheit or (C)elsius? ")
checktype(temp,convert_type)
