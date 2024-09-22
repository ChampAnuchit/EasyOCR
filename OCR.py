import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

#read img
img = "C:/Users/admin/Desktop/easy_ocr/images.png"

imgcv2 = cv2.imread(img)

#text detector
render = easyocr.Reader(['th'], gpu=False)
text = render.readtext(img)

threshold = 0.5

for i,v in enumerate(text):
    print(v)

    bbox, txt, score = v

    if score > threshold:
        cv2.rectangle(imgcv2,bbox[0],bbox[2],(0,255,0),5)
        cv2.putText(imgcv2,txt,bbox[0],cv2.FONT_HERSHEY_SIMPLEX,0.65,(255,0,0),2)

plt.imshow(cv2.cvtColor(imgcv2,cv2.COLOR_BGR2RGB))
plt.show()