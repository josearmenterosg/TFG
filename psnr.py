from math import log10, sqrt
import cv2
import numpy as np

def PSNR(img_original, img_compressed):
	mse = np.mean((img_original - img_compressed) ** 2); print(mse) # Imprimim per pantalla el valor de MSE
	if(mse == 0): # Si MSE es 0, significa que no hi ha soroll en la senyal
		return 100 # Retornem un valor per tancar l'execucio
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse))
	return psnr

def main():
	img_original = cv2.imread("/content/img1")
	img_compressed = cv2.imread("/content/img2", 1)
	value = PSNR(img_original, img_compressed)
	print(f"El valor del PSNR es {value} dB")
  
if __name__ == "__main__":
	main()
