# Face Recognition
Hi this is a project where we learn how to create a basic face recognition program using Python and OpenCV
## Objective of The Project
To recognize the face in the camera and name it. Also, if the face is unknown send a text alert with the image to your mobile via Whatsapp
## Hardware needed
* Laptop with inbuilt camera or a webcam
## Software Required
* Python with OpenCV, numpy, os and  pillow libraries installed 
## 3 Phases
 To create the face recognition program, we need to work on 3 different phases which are:
 1. Face detection and gathering data
 2. Training the recognizer
 3. Recognizing the face

<fig1>
<figcaption text-align: "center"> Block Diagram of given phases: </figcaption>
<img src = "images/FaceRecogBlock.png" alt = "missing" />
  </fig1><br>
 ## Installing Libraries
 ### Opencv
 In your command prompt you need to type the following command:
 ```
 pip install opencv_python
 pip install opencv_contrib
 ```
 ### Other libraries
 Other libraries to install are:
 ```
 pip install os
 pip install pillow
 pip install twilio
 pip install cloudinary
 ```
 
 You need to create an account on [twilio](https://www.twilio.com/) and on [cloudinary](https://cloudinary.com/)
 
 Now, you can learn about the phases of face recognition on the blog by [Ramiz Raza](https://www.superdatascience.com/blogs/opencv-face-recognition)

Give this a go!!
 Saying that lets move on to **Phase-1** 
 ## Data Gathering
 <fig2>
<img src = "images/phase1.png" alt = "missing" />
  </fig2><br>

Lets run the first python file [face_add.py](face_add.py)


Running the following program, we will add 25 images of one face to gather enough data to recognize the face.
Make sure to enter the user input id in integers starting from 1, 2 and so on...

We will get to name them later..! 
