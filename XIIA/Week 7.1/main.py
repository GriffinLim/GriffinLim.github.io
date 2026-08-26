import cv2 as cv

img=cv.imread("imagees.jpg")

img_black_white=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("real",img)

cv.imshow("BlackANdWhite",img_black_white)

cv.waitKey(0)
cv.destroyAllWindows()