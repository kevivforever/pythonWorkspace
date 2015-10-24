import math
def main():
    num = int(raw_input("Enter a number between 1 to 50: "))
    if num and num < 50:
        pii = round(math.pi,num)
        print pii
    else:
        main()
    
if __name__ == '__main__': main()
