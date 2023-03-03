import pytesseract 
from PIL import Image
import os
from ArabicOcr import arabicocr
#folder_dir = "/Users/mohamed/Documents/ML/whisper/extractsubs-opencv/frame0-00-01.07.jpg"
#for img_file in os.listdir(folder_dir):
#    img = Image.open()
#    ocr_results = pytesseract.image_to_string(img)
#    print(ocr_results)

f = "frame0:00:15.00.jpg"
#img = Image.open(f)
#custom_oem_psm_config = r'--psm 6'
#pytesseract.image_to_string(f, config=custom_oem_psm_config)

#ocr_test = pytesseract.image_to_data(img,lang ='eng')


#print(pytesseract.get_languages())
#print(ocr_test)

#### Arabicocr  


out_image='out.jpg'
results=arabicocr.arabic_ocr(f,out_image)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)
with open ('file.txt','w',encoding='utf-8')as myfile:
		myfile.write(str(words))
import cv2
img = cv2.imread('out.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow("arabic ocr",img)
cv2.waitKey(0)
