import cv2 as cv

img=cv.imread("C:\\Users\\Administrator\\Documents\\Griffin_XIIA\\XIIA\\Week 3.3 - OpenCV\\patrick.png")
# img=cv.imread("patrick.png")

# img=cv.imread("original.avif")

cv.imshow(img,10) #img menjadi parameter

cv.waitKey(0)
cv.destroyAllWindows()