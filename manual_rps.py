import random
def play():
    """
    Simple logic of comparing win, lose, tie for RPS game
    Users are asked to make a choice from ['Rock','Paper','Scissors']
    """
    RPS_choices = ['Rock','Paper','Scissors']
    computer_choice = random.choice(RPS_choices)
    user_choice = input('Your choice: ')
    win_rule = {
        'Rock':'Scissors',
        'Scissors':'Paper',
        'Paper':'rock'
    }
    if user_choice not in RPS_choices:
        print('Invalid choice!')
    elif user_choice == computer_choice:
        print(f'It is a tie! Robot is {computer_choice}')
    elif win_rule[user_choice] == computer_choice:
        print(f'You won! Robot is {computer_choice}')
    else:
        print(f'You lost! Robot is {computer_choice}')
#play a game!
play()
