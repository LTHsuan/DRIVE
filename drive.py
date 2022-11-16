# -*- coding: utf-8 -*-
"""DRIVE

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tt05tWkO0SHTQ7fvg5nYQoisnrBoORJ5
"""

!nvidia-smi

! rm -rf ./*
! git clone https://github.com/s910702s910702/DRIVE.git
! mv DRIVE/* ./
! rm -rf DRIVE
! mkdir data/result


! pip3 install imagecodecs

!python3 main.py

!nvidia-smi

import os
base_path = './data/result'
result_list = os.listdir(base_path)
result_list.sort()
print(result_list)

import cv2
from google.colab.patches import cv2_imshow

for result_path in result_list:
    img = cv2.imread(base_path + '/' + result_path)
    cv2_imshow(img)