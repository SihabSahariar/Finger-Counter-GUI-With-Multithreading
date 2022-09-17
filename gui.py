# Sihab Sahariar

from PyQt5 import QtGui, QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import time
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
new_frame_time = 0
prev_frame_time = 0
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray,int)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        self._run_flag = True
        self.cap = cv2.VideoCapture(0)
        with mp_hands.Hands(
          min_detection_confidence=0.5,
          min_tracking_confidence=0.5,
          max_num_hands=2) as hands :

          while self.cap.isOpened() and self._run_flag:

            success,image = self.cap.read()
            if not success :
              print("Skipping empty frame !")
              continue
            
            image = cv2.flip(image,1)

            results = hands.process(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))

            hand = str(results.multi_handedness)

            if 'Right' in hand :
              whathand = 'Hand : Right'
            elif 'Left' in hand :
              whathand = 'Hand : Left'
            else :
              whathand = 'Hand : -'
            
            image.flags.writeable = True
            imageHeight, imageWidth, _ = image.shape
            
            gesture = 'Gesture : -'    
            number = 0

            if results.multi_hand_landmarks :
              for hand_landmarks in results.multi_hand_landmarks :
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(16,31,235), thickness=4, circle_radius=3,), # Land Mark
                mp_drawing.DrawingSpec(color=(52,235,155), thickness=2)) # Land Connections
                
                
                normalizedLandmark = hand_landmarks.landmark[4]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Thumb_Tip_x = pixelCoordinatesLandmark[0]           
                Thumb_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[6]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Pip_x = pixelCoordinatesLandmark[0]           
                Index_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[10]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Pip_x = pixelCoordinatesLandmark[0]           
                Middle_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[14]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Pip_x = pixelCoordinatesLandmark[0]           
                Ring_Pip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[18]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Pip_x = pixelCoordinatesLandmark[0]           
                Pinky_Pip_y = pixelCoordinatesLandmark[1]
                #--------------------------------------------------
                normalizedLandmark = hand_landmarks.landmark[5]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Mcp_x = pixelCoordinatesLandmark[0]           
                Index_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[9]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Mcp_x = pixelCoordinatesLandmark[0]           
                Middle_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[13]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Mcp_x = pixelCoordinatesLandmark[0]           
                Ring_Mcp_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[17]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Mcp_x = pixelCoordinatesLandmark[0]           
                Pinky_Mcp_y = pixelCoordinatesLandmark[1]

                #------------------------------------
                normalizedLandmark = hand_landmarks.landmark[3]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Thumb_Ip_x = pixelCoordinatesLandmark[0]           
                Thumb_Ip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[8]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Index_Tip_x = pixelCoordinatesLandmark[0]           
                Index_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[12]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Middle_Tip_x = pixelCoordinatesLandmark[0]           
                Middle_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[16]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Ring_Tip_x = pixelCoordinatesLandmark[0]           
                Ring_Tip_y = pixelCoordinatesLandmark[1]

                normalizedLandmark = hand_landmarks.landmark[20]# Point No.
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
                Pinky_Tip_x = pixelCoordinatesLandmark[0]           
                Pinky_Tip_y = pixelCoordinatesLandmark[1]

                thmb_indx_diff = Thumb_Ip_x-Index_Mcp_x

                if Index_Pip_y < Middle_Tip_y and Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y :
                    if Index_Tip_y < Middle_Pip_y and Index_Tip_y < Ring_Pip_y and Index_Tip_y < Pinky_Pip_y :
                        gesture = 'Gesture : One' 
                        number  = 1  

                if Index_Pip_y < Ring_Tip_y and Index_Pip_y < Pinky_Tip_y :
                    if Middle_Tip_y < Ring_Pip_y and Middle_Tip_y < Pinky_Pip_y :
                        gesture = 'Gesture : Two'  
                        number = 2

                if Index_Pip_y < Pinky_Tip_y and Middle_Pip_y < Pinky_Tip_y and Ring_Pip_y < Pinky_Tip_y  :
                    if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y :
                        if Index_Tip_y < Thumb_Tip_y and Middle_Tip_y < Thumb_Tip_y and Ring_Tip_y < Thumb_Tip_y :
                            gesture = 'Gesture : Three'   
                            number = 3

                if Index_Pip_y < Thumb_Tip_y and Middle_Pip_y < Thumb_Tip_y and Ring_Pip_y < Thumb_Tip_y  :
                    if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y :
                        gesture = 'Gesture : Four' 
                        number = 4

                if thmb_indx_diff < -15 :
                    if Index_Tip_y < Index_Pip_y and Middle_Tip_y < Middle_Pip_y and Ring_Tip_y < Ring_Pip_y and Pinky_Tip_y < Pinky_Pip_y :
                        gesture = 'Gesture : Five'
                        number = 5

            cv2.rectangle(image,(5,5),(320,110),(0,170,240),-1)
            cv2.putText(image,gesture,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)         
            self.change_pixmap_signal.emit(image,number)
        # shut down capture system
        self.cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(816, 630)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1101, 111))
        self.frame.setStyleSheet("background-color:rgb(10,20,40);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(-10, 110, 1101, 691))
        self.frame_2.setStyleSheet("background-color:rgb(100,200,240);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 10, 500, 500))
        self.label.setStyleSheet("background-color:rgb(200,200,200);\n"
"border:1px solid white;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ss_video = QtWidgets.QPushButton(self.frame_2)
        self.ss_video.setGeometry(QtCore.QRect(530, 460, 291, 51))
        self.ss_video.setStyleSheet("QPushButton{\n"
"background-color:rgb(20,40,100);\n"
"color:white;\n"
"border:1px solid white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(20,40,50);\n"
"color:white;\n"
"border:1px solid white;\n"
"}")
        self.ss_video.setObjectName("ss_video")
        self.cnt = QtWidgets.QLabel(self.frame_2)
        self.cnt.setGeometry(QtCore.QRect(530, 100, 281, 211))
        font = QtGui.QFont()
        font.setPointSize(43)
        self.cnt.setFont(font)
        self.cnt.setStyleSheet("color:white;")
        self.cnt.setAlignment(QtCore.Qt.AlignCenter)
        self.cnt.setObjectName("cnt")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Finger Counter By Sihab Sahariar")
        self.label_2.setText(_translate("Form", "Finger Counter v1.0"))
        self.ss_video.setText(_translate("Form", "Start video"))
        self.cnt.setText(_translate("Form", "0"))
        self.thread = VideoThread()
        self.ss_video.clicked.connect(self.ClickStartVideo)

    # Activates when Start/Stop video button is clicked to Start (ss_video
    def ClickStartVideo(self):
        # Change label color to light blue
        self.ss_video.clicked.disconnect(self.ClickStartVideo)
        # Change button to stop
        self.ss_video.setText('Stop video')
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)

        # start the thread
        self.thread.start()
        self.ss_video.clicked.connect(self.thread.stop)  # Stop the video if button clicked
        self.ss_video.clicked.connect(self.ClickStopVideo)

    # Activates when Start/Stop video button is clicked to Stop (ss_video)
    def ClickStopVideo(self):
        self.thread.change_pixmap_signal.disconnect()
        self.ss_video.setText('Start video')
        self.ss_video.clicked.disconnect(self.ClickStopVideo)
        self.ss_video.clicked.disconnect(self.thread.stop)
        self.ss_video.clicked.connect(self.ClickStartVideo)

    def update_image(self, cv_img,val):
        qt_img = self.convert_cv_qt(cv_img)
        self.label.setPixmap(qt_img)
        self.cnt.setText(str(val))

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        #p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        p = convert_to_Qt_format.scaled(500, 500, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

