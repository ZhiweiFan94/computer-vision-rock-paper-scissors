# #%%
# import cv2
# from keras.models import load_model
# import numpy as np
# model = load_model('keras_model.h5')
# cap = cv2.VideoCapture(0)
# data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# while True: 

#     ret, frame = cap.read()
#     mirrored_frame = cv2.flip(frame, 1)
#     resized_frame = cv2.resize(mirrored_frame, (224, 224), interpolation = cv2.INTER_AREA)
#     image_np = np.array(resized_frame)
#     normalized_image = (image_np.astype(np.float32) / 127.5) - 1 # Normalize the image
#     data[0] = normalized_image
#     prediction = model.predict(data)
#     cv2.imshow('frame', mirrored_frame)
#     # Press q to close the window
#     print(prediction)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
            
# # After the loop release the cap object
# cap.release()
# # Destroy all the windows
# cv2.destroyAllWindows()
# %%

from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model1
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()