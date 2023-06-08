#%% task1 --milestone 4
import random


def get_computer_choice():
    return random.choice(['Rock','Paper','Scissors'])

def get_user_choice():
    user_choice = input('Your choice: ')
    return user_choice

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'Rock' and user_choice =='Scissors') or (computer_choice == 'Paper' and user_choice =='Rock') or (computer_choice == 'Scissors' and user_choice =='Paper'):
        print('You lost')
    elif (user_choice == 'Rock' and computer_choice =='Scissors') or (user_choice == 'Paper' and computer_choice =='Rock') or (user_choice == 'Scissors' and computer_choice =='Paper'):
        print('You win')
    else:
        print('It is a tie!')

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)


play()
# %%
