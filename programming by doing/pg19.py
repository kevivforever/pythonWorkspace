def main():
    first_num = float(raw_input("What is your first number?"))
    second_num = float(raw_input("What is your second number?"))
    third_num = float(raw_input("What is your third number?"))
    total = first_num + second_num + third_num
    print ("( %s + %s + %s ) / 2 is ... %s") % (str(first_num),str(second_num),str(third_num),str(total))


if __name__ == '__main__': main()
