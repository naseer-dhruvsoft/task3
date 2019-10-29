import argparse
import imutils
import numpy
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image")
args = vars(ap.parse_args())

# Loading the input image
image = cv2.imread(args["image"])
# image2 = cv2.imread(args["image"])
cv2.imshow("Actual_image", image)
cv2.waitKey(0)


# converting to grayscale image
gray_img =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale_image", gray_img)
cv2.waitKey(0)
# applying threshold to grayscale image
threshold_img = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Threshold", threshold_img)
cv2.waitKey(0)
# contours to threshold
cnts = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output_img = threshold_img.copy()
# loop over the contours
i = 0
for c in cnts:
	if cv2.contourArea(c) > 100:
		print(cv2.contourArea(c))
		i=i+1
		cv2.drawContours(image, [c], -1, (0,0, 255), 5)
# cv2.drawContours(image2, cnts, -1, (0,0,255),1)
cv2.imshow("Contours Naseer", image)
print("Number of objects found: ",i)
cv2.imshow("Contours", output_img)
cv2.waitKey(0)


