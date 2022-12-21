import face_recognition
import numpy as np
import csv
import os
import glob
import datetime
import datetime
import cv2

video_capture=cv2.VideoCapture(0)

elon_image=face_recognition.load_image_file("elon musk.jpg")
elon_encoding=face_recognition.face_encoding(elon_image)[0]

jeff_image=face_recognition.load_image_file("jeff bezos.jpg")
jeff_encoding=face_recognition.face_encoding(jeff_image)[0]