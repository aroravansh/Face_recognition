import cv2
import numpy as np
from PIL import Image
import os
# Path for face image database
path = 'C:\\Users\\Param Arora\\Downloads\\faces'
recognizer = cv2.face.LBPHFaceRecognizer_create()  #LBPH (LOCAL BINARY PATTERNS HISTOGRAMS) Face Recognizer is  included in the OpenCV package.
detector = cv2.CascadeClassifier("C:\\Python\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")


# function to get the images and label data
def get_images_and_labels(paths):
    image_paths = [os.path.join(paths, f) for f in os.listdir(paths)]  # To go through each image
    face_samples = []
    ids = []
    for image_path in image_paths:
        pil_img = Image.open(image_path).convert('L')   # convert it to grayscale
        img_numpy = np.array(pil_img, 'uint8')
        id2 = int(os.path.split(image_path)[-1].split(".")[0])  # Getting images of a user to be appended together 
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id2)
    return face_samples, ids


print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces1, id1 = get_images_and_labels(path)
recognizer.train(faces1, np.array(id1))
# Save the model into trainer/trainer.yml
recognizer.write('C:\\docx\\trainer\\trainer.yml')
# Print the number of faces trained and end program
print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(id1))))
