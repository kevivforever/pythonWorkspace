
def main():
    height = float(raw_input("Your height in m: "))
    print height
    weight = float(raw_input("Your weight in kg: "))
    print weight

    print "Your BMI is %f" % (weight/(height**2))
    
if __name__ == '__main__': main()
