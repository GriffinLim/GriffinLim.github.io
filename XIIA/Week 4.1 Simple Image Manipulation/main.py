import cv2 as cv

image=cv.imread("anjing.png")

# BlackWhiteImage=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# GaussianBlur=cv.GaussianBlur(image,(5,5),0)


cv.imshow(image,6)
# cv.imshow("Filtered",BlackWhiteImage)
# cv.imshow("Filtered (BW)",GaussianBlur)


cv.waitKey(0)
cv.destroyAllWindows()