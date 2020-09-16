import cv2
# import requests
url = "https://www.fast2sms.com/dev/bulk"
count = 0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\\docx\\trainer\\trainer.yml')
cascadePath = "C:\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
# initiate id counter
id1 = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Vansh', 'Ronaldo', 'Mom', 'x', 'y', 'z']
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id1, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        # Check if confidence is less them 100 ==> "0" is perfect match
        if confidence < 100:
            id1 = names[id1]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id1 = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            '''payload = "sender_id=FSTSMS&message='Hi u have an unknown at camera'&language=english&
                     route=p&numbers=9268686388"
            headers = {
                'authorization': "y4rDf56iYdobSgpU2P7j3uLIhznlQXOHeEJTGxqW91cwsAFKv8uWln4iXe1dOINQbVBs6vtfhHmoy87R",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            break'''
            cv2.imwrite("C:\\Users\\Param Arora\\Downloads\\lol" + '.' + str(count) + ".jpg",
                        img)
            count += 1
            print('Image saved')
        cv2.putText(img, str(id1), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    if count == 2:
        break

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
