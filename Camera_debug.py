import numpy as np
import cv2 as cv
#########Start setup###########
cap = cv.VideoCapture(0) #Open Camera device number 0 (if there's multiple camera connected to the raspberry pi, you could change the index)
if not cap.isOpened(): # if there's no camera detected print and error and close the program
    print("Cannot open camera")
    exit()
#########End setup###########
##########Start Loop###########
while True: # to always capture an image as the void loop
    # Capture frame-by-frame (explain it as void loop in arduino)
    ret, frame = cap.read() # ret is a variable that gives us an idea about the quality of the frame
    # if frame is read correctly ret is True
    if not ret: # if it's not good print an error
        print("Can't receive frame (stream end?). Exiting ...")
        break  #break is used to leave the loop
    # Display the resulting frame
    cv.imshow('frame', frame) # shows us the frame in a window names frame
    if cv.waitKey(1) == ord('q'): # if we hit the "q" button the program leaves the loop
        break
##########End Loop#############
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
