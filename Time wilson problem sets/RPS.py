import random
max_points = 0

def decide_winner(h_input,c_input):
    if h_input == c_input:
        return 'A draw!'
    elif h_input == 'R':
        if c_input == 'S':
            return 'human'
        else:
            return 'computer'
    elif h_input == 'S':
        if c_input == 'R':
            return 'computer'
        else:
            return 'human'
    else: 
        if c_input == 'R':
            return 'human'
        else:
            return 'computer'
    
def play_game():
    valid_choices = {'R':'Rock','P':'Paper','S':'Scissors'}
    human_key = raw_input("Choose (R)ock, (P)aper, or (S)cissors? ")
    if human_key and human_key.upper() in valid_choices:
        human_input = valid_choices.get(human_key.upper())
        computer_key = random.choice(valid_choices.keys())
        computer_input  = valid_choices.get(computer_key)
        winner = decide_winner(human_key.upper(),computer_key)
            
        print "Human: %s       Computer: %s       winner: %s" % (valid_choices.get(human_key.upper()),valid_choices.get(computer_key),winner)
        return winner
    else:
        print "invalid choice. Select again"
        play_game()

def validate_points(points):

    global max_points
    if points and points.isdigit():
        max_points = int(points)
    else:
        points = raw_input("How many points are required for a win? ")
        validate_points(points)
        
def main():
    computer_score = 0
    human_score = 0
    global max_points
    found_winner = False
    print("Welcome to Rock, Paper, Scissors!")
    points = raw_input("How many points are required for a win? ")

    validate_points(points)   
        
    while(not found_winner):
        print max_points
        if computer_score == max_points or human_score == max_points:
            found_winner = True
            print ("Final Score: Human %d    Computer %d") % (human_score,computer_score)
        else:
            print("Score: Human %d    computer %d" % (human_score,computer_score))
            winner = play_game()
            if winner == 'computer':
                computer_score += 1
            else:
                if winner == 'human':
                    human_score +=1
                
if __name__ == '__main__': main()
