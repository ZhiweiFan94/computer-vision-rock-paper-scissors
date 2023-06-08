# Computer Vision RPS

## milestone 1-3:
- install the environment and the Tensorflow module following the instructions
- one should notice the python environment in VScode is not autoly switched to the one you create, therefore, we may manually give the path to the python we will use. This is essential otherwise the installed module cannot run.




## milestone 4:
- create a new python file and create four methods named get_computer, get_user ,get_winner, and play. The 'play' function should contain the other three inside. 
- Test the program and make sure it runs well.


## milestone 5:
### Inside the while loop which opens the camera:
- I add a condition to decide which timing to select the gesture from the user (every 3 seconds)
- Inside the condition, we can call the function to ask computer to randomly make a selection and compare the user's gesture recoginized by the learning model
- In terms of the returns, considering the final demands that we need to end the game following the 'reach 3 wins' condition, the info of who wins should be recorded.

### About the comparision functions:
- Just copy paste the manual section and make the user input to camera-based format.

### Comments:
- The Teach machine model is not very ideal. I have insert training shots more than 500 pictures, but it seems the recognition probability is still low for such a simple task, especially when hand is slightly away or close to the camera. 