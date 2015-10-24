import calculate

height = 0.0
print"Welcome to your BMI calclulator!!"
print"Would you like to enter your weight in (K)ilogram or (p)ound"
weight_type = raw_input("> ")
weight = float(raw_input("Your weight: "))
print"Would you like to enter your height in (m)eter or (f)eet and inches or (I)nches"
height_type = raw_input("> ").upper()

if height_type == 'M':
    height = float(raw_input("Your height in m: "))
    calc = calculate.Calculate(height,weight,weight_type)
elif height_type == 'F':
    feet_height = int(raw_input("Your height in (feet only): "))
    inch_height = int(raw_input("Your height in (inches): "))
else:
    inch_height = int(raw_input("Your height in (inches): "))
    

        
#height = float(raw_input("Your height in m: "))

