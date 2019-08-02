import cv2
import numpy as np

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("dataSet1/"+Id +str(sampleNum) + ".jpg",gray[y:y+h,x:x+w])
        
cv2.imshow('frame',img)
     

img.release()

