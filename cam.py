import cv2 as cv
cap = cv.VideoCapture(1)

#webcam not is opened 
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()
while True:
    ret, frame = cap.read()

    # Display
    cv.imshow('Webcam', frame)

    # Wait for 1ms and check if 'q' key is pressed to stop the cam
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv.destroyAllWindows()