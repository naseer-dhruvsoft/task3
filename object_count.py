import imutils
import numpy as np
import cv2
import boto3

# Loading the input image
def count_of_objects():
  source_image_url = "https://task3bucket.s3.ap-south-1.amazonaws.com/solar_system.jpg"
  # source_image_url = "https://task3bucket.s3.ap-south-1.amazonaws.com/google_logo.jpg"
  image = imutils.url_to_image(source_image_url)

  # resizing the given image
  adjusted_img = cv2.resize(image, (1000, 1000), cv2.INTER_LINEAR ) 
  # cv2.imshow("Resized_Image", adjusted_img)
  # cv2.waitKey(0)

  # # converting to grayscale image
  gray_img =  cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2GRAY)
  # cv2.imshow("Grayscale_image", gray_img)
  # cv2.waitKey(0)
  # applying threshold to grayscale image
  threshold_img = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)[1]
  # cv2.imshow("Threshold", threshold_img)
  # cv2.waitKey(0)
  # contours to threshold
  cnts = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  cnts = imutils.grab_contours(cnts)
  output_img = threshold_img.copy()
  # loop over the contours
  i = 0
  # name = 'Google Logo'
  name = 'Solar_System'
  for c in cnts:
    if cv2.contourArea(c) > 640:
      # print(cv2.contourArea(c))
      i=i+1
      cv2.drawContours(adjusted_img, [c], -1, (0,0, 255), 5)
  mydict = {
    "Image_Name": name,
    "Count": i
  }
  return mydict
