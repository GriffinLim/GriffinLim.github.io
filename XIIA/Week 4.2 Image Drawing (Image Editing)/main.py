import cv2 as cv

img=cv.imread("MJ.jpg")

tinggi,lebar, _ = img.shape
print(f"info:Lebar:{lebar}px,Tinggi:{tinggi}px")

#Rectangle
cv.rectangle(img,(0,0),(lebar,500),(0,0,0),10)

#Save THe image as a new file
newFileName="newImg.png"
cv.imwrite(newFileName,img)
print(f"Image saved as {newFileName}")

#Text
text="King of Pop"
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,text,(200,450),font,1,(0,0,0),2,cv.LINE_AA)

cv.imshow("Michael Jackson",img)

cv.waitKey(0)
cv.destroyAllWindows()