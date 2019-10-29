import argparse
import imutils
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image")
args = vars(ap.parse_args())

# Loading the input image
image = cv2.imread(args["image"])
cv2.imshow("Actual_image", image)
cv2.waitKey(0)
# image2 = cv2.imread(args["image"])
# height = 1000
# width = 1000
# dimensions = (height, width)

# resizing the given image
adjusted_img = cv2.resize(image, (1000, 1000), cv2.INTER_LINEAR ) 
cv2.imshow("Resized_Image", adjusted_img)
cv2.waitKey(0)

# # converting to grayscale image
gray_img =  cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale_image", gray_img)
cv2.waitKey(0)
# applying threshold to grayscale image
threshold_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 299, 0)
cv2.imshow("Threshold", threshold_img)
cv2.waitKey(0)
# contours to threshold
cnts = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
output_img = threshold_img.copy()
# loop over the contours
i = 0
for c in cnts:
	if cv2.contourArea(c) > 6800:
		print(cv2.contourArea(c))
		i=i+1
		cv2.drawContours(adjusted_img, [c], -1, (0,0, 255), 5)
    # #get the min enclosing circle
    # (x, y), radius = cv2.minEnclosingCircle(c)
    # # convert all values to int
    # center = (int(x), int(y))
    # radius = int(radius)
    # # draw the circle in blue
    # img = cv2.circle(image, center, radius, (255, 0, 0), 2)
    # if radius > 24:
    #     # print(cv2.minEnclosingCircle(c))
    #     i=i+1   
print(i)
# cv2.drawContours(image, cnts, -1, (0, 255, 0), 1)
cv2.imshow("contours", adjusted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()