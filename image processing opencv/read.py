import cv2 as cv

# Reading images
# img = cv.imread('Resources/Images/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)


# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4') # 0 param - web camera, 1 param - first camera connected
while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        cv.imshow('Video', frame)
    else:
        break

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

