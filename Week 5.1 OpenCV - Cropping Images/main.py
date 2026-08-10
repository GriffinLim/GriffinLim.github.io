import cv2 as cv

x_start=20
x_end=450

y_start=350
y_end=775

img=cv.imread("task.png")

crooping_img=img[x_start:x_end,y_start:y_end]

cv.imshow("anjingCrop",crooping_img)


cv.waitKey(0)
cv.destroyAllWindows()