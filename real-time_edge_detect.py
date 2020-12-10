# import the necessary packages
import numpy as np
import cv2

#CANNY EDGE DETECTION FUNCTION
def canny(image, sigma=0.35):
    #handles computing the median of the pixel intensities in the image.
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    #lower  and upper  are our integer thresholds for the step: Apply thresholding using a lower and upper boundary on the gradient values. 
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged

#set the scale of the camera window and size of rames
def rescale_frame(frame, percent):
    #frame width and hight to resize the window
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

#OPEN THE CAMERA IN DEVICE 1 (DEVICE 0 IS INBUILT WECAM BY DEFAULT)
cap = cv2.VideoCapture(0)

while True:

    #get frame by frame from the camera
    ret, frame = cap.read()
    frame = rescale_frame(frame , 90)
    #convert a fram to gray scale fro reduce the unwanted infomation like clors,etc.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #set the gaussian blur filter
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # apply Canny edge detection using automatically determined threshold
    edges = canny(blurred)
    # Display an original image
    cv2.imshow('Original_stream', frame)

    # finds edges in the input image image and
    # marks them in the output map edges
    #edges = cv2.Canny(frame, 100, 200)

    # Display edges in a frame
    cv2.imshow('Canny_edges', edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
