from random import randint

random_number = (randint(0,100))
number_of_guesses = 0
#print random_number

def ask_for_input(message):
    global number_of_guesses
    number_of_guesses += 1
    #print "guess number: %d" % number_of_guesses
    print_message = "%s. Try again: " % message
    u_input = input(print_message)
    check_input(u_input,number_of_guesses)
    
def check_input(user_input,guess_count):
    if user_input and user_input.isdigit():
        int_input = int(user_input)
        if int_input > random_number:
            ask_for_input("Too high")
        elif int_input < random_number:
            ask_for_input("Too Low")
        else:
            print ("Congratulations! You got it in %d guesses" % (guess_count))
    else:
        ask_for_input("Not a valid number")
        
def main():
    
    print ("Time to play a guessing game.")
    global number_of_guesses
    number_of_guesses += 1
    #print "guess number: %d" % number_of_guesses
    user_input = input("Enter a valid number between 1 and 100: ")
    
    check_input(user_input,number_of_guesses)

if __name__ == '__main__': main()
