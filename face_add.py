import cv2    #import opencv module
cam = cv2.VideoCapture(0)   # Capturing video in build in camera. If webcam type 1
cam.set(2, 640)    # set video width
cam.set(4, 480)    # set video height
face_detector = cv2.CascadeClassifier('C:\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while True:
    ret, img = cam.read()   # Reading video frame by frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #converting it to grayscale
    faces = face_detector.detectMultiScale(gray, 1.3, 5)    # detecting multiple face and creating a list
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Extracting the face from faces coordinates
        count += 1
        # Save the captured image into the faces  folder

        cv2.imwrite("Your path" + str(face_id) + '.' + str(count) + ".jpg",
                    gray[y:y + h, x:x + w])

    k = cv2.waitKey(100) & 0xff      # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 35:    # Take 35 face sample and stop video
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
