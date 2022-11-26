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
    counter =0 #the counter variable
    ret, frame = cap.read() # ret is a variable that gives us an idea about the quality of the frame
    # if frame is read correctly ret is True
    if not ret: # if it's not good print an error
        print("Can't receive frame (stream end?). Exiting ...")
        break  #break is used to leave the loop
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # Convert BGR to HSV
    # define range of blue color in HSV
    lower_red = np.array([0,50,50]) #lower means the lower"limit" of the color in our case 0 : red in HSV goes from a7mer daken :(0,50,50)
    # 100% means 255.
    upper_red = np.array([15,255,255]) #upper means the up "limit" of the color in our case 15 : red in HSV goes to orangé fate7 (15,255,255)
    # Threshold the HSV image to get only red colors
    mask = cv.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    #we gonna find the closed contours in the mask resulted from color detection : contours vaiable contains all the contours we need
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours: #for each contour we find
    	if(cv.contourArea(cnt)>3000): # if it's big enough to be a cherry
    		#we gonna draw all the useful contours on the original frame
    		cv.drawContours(frame, [cnt], 0, (0,255,0), 3)
    		counter=counter+1 # the counter should increment
    # Display the resulting frame
    print(counter) #print the number of cherries found
    cv.imshow('frame', frame) # shows us the frame in a window named frame
    cv.imshow('mask',mask)  # shows us the mask (the pixels that are red are white) in a window named mask
    cv.imshow('result',res)  # shows us the result of "AND" operation (the pixels that are red are white) in a window named res
    if cv.waitKey(1) == ord('q'): # if we hit the "q" button the program leaves the loop
        break
##########End Loop#############
# When everything done, release the capture
cap.release()
cv.destroyAllWindows() # close all windows
