import cv2 as cv

image=cv.imread("german.jpg")

BlackWhiteImage=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
GaussianBlur=cv.GaussianBlur(image,(5,5),0)


cv.imshow("Original",image)
cv.imshow("Filtered",BlackWhiteImage)
cv.imshow("Filtered (BW)",GaussianBlur)

print(image)
cv.waitKey(0)
cv.destroyAllWindows()