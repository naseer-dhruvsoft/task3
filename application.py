import argparse
import imutils
import numpy as np
import cv2
from flask import Flask

application =  Flask(__name__)
@application.route('/')
def count_of_objects():
  image = cv2.imread("google_logo.jpg")

  # resizing the given image
  adjusted_img = cv2.resize(image, (1000, 1000), cv2.INTER_LINEAR )

  # # converting to grayscale image
  gray_img =  cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2GRAY)

  # applying threshold to grayscale image
  threshold_img = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)[1]

  # contours to threshold
  cnts = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  cnts = imutils.grab_contours(cnts)
  output_img = threshold_img.copy()

  # loop over the contours
  i = 0
  for c in cnts:
    if cv2.contourArea(c) > 640:
      i=i+1
      cv2.drawContours(adjusted_img, [c], -1, (0,0, 255), 5)  
  return "<h2>The number of objects found in the given image are: %d </h2>" %i

if __name__ == '__main__':
    application.run()
