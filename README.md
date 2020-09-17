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
 pip install numpy
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
Run the script few times, each to capture one single id
Make sure to enter the user input id in integers starting from 1, 2 and so on...

We will get to name them later..! 
Now lets move on to **Phase-2** ....
## Data Trainer
<fig3>
<img src = "images/phase2.png" alt = "missing" />
 </fig3><br>
 
Running the python script [face_trainer.py](face_trainer.py)


Make sure you take the current path of the picture you saved earlier in Data Gathering. 
At the end you should the number of faces trained equal to the faces you captured in [face_add.py](face_add.py)

As a result, a file named "trainer.yml" will be saved in the path you entered.

Note: Everytime you run [face_add.py](face_add.py), you have to run [face_trainer.py](face_trainer.py) also to implement the changes

Now, Lets move on to the final phase for Face Recognition, **Phase-3**

## Face Recognizer
<fig4>
<img src = "images/phase3.png" alt = "missing" />
 </fig4><br>
 
Now, we have reached the final phase of our project. Here, we will capture a fresh face on our camera and if this person had his face captured and trained before, our recognizer will make a "prediction" returning its id and an index, shown how confident the recognizer is with this match.

Lets run the final python script [face_recog.py](face_recog.py)...

Here, we created a name list which has names indexed according to the userid you added in [face_add.py](face_add.py)

If the recognizer could predict a face, we put a text over the image with the probable id and how much is the "probability" in % that the match is correct ("probability" = 100 - confidence index).Note that the confidence index will return "zero" if it will be cosidered a perfect match.

If not, an "unknow" label is put on the face, image is uploaded to your cloudinary account and then sent to your whatsapp number.

We can't send the image directly from our local machine, that's why we had to upload it on the cloud so that it could have an URL...

Thats it for this project....


Thank You 

Vansh

### Credits
* Thank You @aroramanish2009 for giving me the project
* Also thanks to @mjrovai for his blog on [real-time face recognition](ackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826)
