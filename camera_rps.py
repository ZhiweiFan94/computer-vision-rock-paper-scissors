import cv2
import time
import random
import numpy as np
from keras.models import load_model


def get_prediction(prediction):
    """
    Get prediction from gestures with highest probability
    """
    guess_idx = np.argmax(prediction[0])
    input_list = ['Rock', 'Paper', 'Scissors', 'Nothing']
    user_input = input_list[guess_idx]
    return user_input
 
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_winner(computer_choice, user_choice):
    """
    Compare the choices and return the winner of the game
    """
    RPS_choices = ['Rock', 'Paper', 'Scissors']
    win_rule = {
        'Rock':'Scissors',
        'Scissors':'Paper',
        'Paper':'rock'
    }
    if user_choice not in RPS_choices:
        return 'Nothing'
    elif user_choice == computer_choice:
        return 'It is a tie!'
    elif win_rule[user_choice] == computer_choice:
        return 'You won'
    else:
        return 'You lost'

def play(prediction):
    """
    Start the RPS game
    """
    computer_choice = get_computer_choice()
    user_choice = get_prediction(prediction)
    outcome = get_winner(computer_choice, user_choice)
    return computer_choice, user_choice, outcome 

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

start_time = time.time()
countdown = 3  # Countdown time in seconds
show_hand = False

#%% initialise the game 
computer_wins = 0
user_wins = 0
result = 0

#play the game until certain condition is met: when one side firstly becomes winner 3 times
while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image
    prediction = model.predict(data)

    cv2.putText(frame, f"Computer wins: {computer_wins} ", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"You win: {user_wins}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    elapsed_time = time.time() - start_time

    if elapsed_time >= countdown: #set time gap of 3 seconds to capture the users gesture
        computer, user, result = play(prediction)
        print(f'You chose {user} and computer chooses {computer}, so {result}')     
        if result == 'You win':
            user_wins += 1
        elif result == 'You lost':
            computer_wins += 1      
        start_time = time.time()

    if user_wins == 3:
        print('You reaches 3 wins firstly, congrats!')
        break
    if computer_wins == 3:
        print('Computer reaches 3 wins firstly, try again.')
        break
    if cv2.waitKey(1) & 0xFF == ord('q'): #use key 'q' to exit the game
        break

cap.release()
cv2.destroyAllWindows() 
