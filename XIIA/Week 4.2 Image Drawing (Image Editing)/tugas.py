import cv2 as cv

img_gibran=cv.imread("gibran.webp")
img_prabowo=cv.imread("Wowo.jpg")

tinggiGibran,lebarGibran,_=img_gibran.shape
tinggiWowo,lebarWowo,_=img_prabowo.shape

thickness=50

cv.rectangle(img_gibran,(0,0),(lebarGibran,tinggiGibran),(255,255,255),thickness)
cv.rectangle(img_prabowo,(0,0),(lebarWowo,tinggiWowo),(255,255,255),thickness)

textGib="Gibran Rakabuming Raka"
textWowo="Prabowo Subianto"

font=cv.FONT_HERSHEY_SIMPLEX

cv.putText(img_gibran,textGib,(20,tinggiGibran-12),font,0.5,(0,0,0),10,cv.LINE_AA)
cv.putText(img_prabowo,textWowo,(20,tinggiWowo-12),font,0.5,(0,0,0),10,cv.LINE_AA)

cv.imshow("Prabowo",img_prabowo)
cv.imshow("Gibran",img_gibran)

cv.waitKey(0)
cv.destroyAllWindows()