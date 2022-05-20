from skimage.metrics import structural_similarity as ssim
import argparse
import imutils
import cv2

img_original = cv2.imread("/content/img1") #Carreguem imatge original
img_compress = cv2.imread("/content/img2") #Carreguem imatge comprimida


gray_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY) #Convertim les imatges a blanc i negre
gray_compress = cv2.cvtColor(img_compress, cv2.COLOR_BGR2GRAY) #Convertim les imatges a blanc i negre

#Calcyl de la mètrica SSIM
(score, diff) = ssim(gray_original, gray_compress, full=True)
diff = (diff * 255).astype("uint8")

#Extreiem per pantalla el valor
print("El valo del SSIM: {}".format(score))
