import cv2 as cv

img=cv.imread("german.jpg")

BlackWhiteImg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

text="Griffin Limantara XIIA"
font=cv.FONT_HERSHEY_COMPLEX

xText=200
yText=100

cv.putText(BlackWhiteImg,text,(xText,yText),font,1,(0,0,0),10,cv.LINE_AA)

y_start=10
y_end=510

x_start=60
x_end=600


CropImg=BlackWhiteImg[y_start:y_end,
                      x_start:x_end]
NewFileName="Hasil_edit.jpg"
cv.imwrite(NewFileName,CropImg)

cv.imshow("Hasil",CropImg)
print(f"New File Name:{NewFileName}")


cv.waitKey(0)
cv.destroyAllWindows()