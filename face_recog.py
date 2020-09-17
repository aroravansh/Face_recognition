import cv2
import cloudinary.uploader
from twilio.rest import Client


def uploadimg():  # Uploading image of unknown person to cloud
    cloudinary.config(cloud_name='Your_cloud_name',
                      api_key='Your_api_key',
                      api_secret='Your_api_aut_secret_key')
    cloudinary.uploader.upload('C:\\Users\\Param Arora\\Downloads\\Unknown.1.jpg',  # where you saved the image
                               folder='face_recog',  # folder created in cloud
                               use_filename=True,
                               unique_filename=False)
    print('Image successfully uploaded..')


def sendmsg():  # Sending message to your mobile numb with image of unknown person
    account_sid = 'your_acc_id'
    auth_token = 'your_auth_key'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Hi! There is this unknown person at your camera....',
        # Copy the url of the image you saved in face_recog once without sending message
        media_url='Copied url of the image from cloudinary',
        from_='whatsapp:+14155238886',  # Given in your twilio account
        to='whatsapp:+919268686388'  # your numb or where you want to send the text
    )
    print(message.sid)  # will print your id to show message sent successfully


count = 0
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:\\docx\\trainer\\trainer.yml')   # path of file created in face_trainer.py
cascadePath = "C:\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
# initiate id counter
id1 = 0
# names related to ids: example ==> Vansh: id=1,  etc
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
            id1 = names[id1]  # displaying the name of the person
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id1 = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            count += 1    # To break out of loop
            cv2.imwrite("C:\\Users\\Param Arora\\Downloads\\unknown" + '.' + str(count) + ".jpg",
                        img)  # write the path where u want to save, it should have permissions to write
            print('Image saved')
            print('Wait saving image to cloud....')
            uploadimg()
            print('Now sending message to your whatsapp number....')
            sendmsg()

        cv2.putText(img, str(id1), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    if count == 1:  # To break once you get 1 message on your whatsapp
        break

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
