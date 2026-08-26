import cv2 as cv

poster=cv.imread("white.jpg")

posterL,posterT,_=poster.shape

thickness=200
x=170
y=30


cv.rectangle(poster,(0,0),(posterL,100),(0,0,255),thickness)

font=cv.FONT_HERSHEY_COMPLEX

title="PERATURAN/TATA TERTIB"
title2="LABORATORIUM"
title3="KOMPUTER & BAHASA"


text1="1.Mengenakan pakaian yang rapi dan sopan"
text2="2.Tidak diperkenankan membawa makanan dan minuman"
text3="3.Tidak mengoperasikan komputer dan alat-alat elektronik lainnya tanpa seijin"
text31="pengelola laboratorium"
text4="4.Dilarang meminjam barang-barang dan alat-alat elektronik tanpa seijin"
text5="5.Dilarang membuang sampah sembarangan"
text6="6.Menjaga kebersihan dan kerapian ruangan laboratorium"
text7="7.Dilarang berpindah-pindah tempat kecuali seijin pengelola laboratorium"
text8="8.Volume suara standar / tidak menimbulkan suara gaduh / tidak ribut"

cv.putText(poster,title,(x,y),font,1,(0,255,255),10,cv.LINE_AA)
cv.putText(poster,title2,(x+70,y+50),font,1,(0,255,255),10,cv.LINE_AA)
cv.putText(poster,title3,(x+40,y+100),font,1,(0,255,255),10,cv.LINE_AA)

cv.putText(poster,text1,(0,y+200),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text2,(0,y+220),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text3,(0,y+240),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text31,(0,y+260),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text4,(0,y+280),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text31,(0,y+300),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text5,(0,y+320),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text6,(0,y+340),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text7,(0,y+360),font,0.6,(0,0,0),10,cv.LINE_AA)
cv.putText(poster,text8,(0,y+380),font,0.6,(0,0,0),10,cv.LINE_AA)

cv.imshow("poster",poster)


cv.waitKey(0)
cv.destroyAllWindows()