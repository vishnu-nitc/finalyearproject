import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('10_left_gray.jpeg')
#edges = cv2.Canny(img,100,200)
a1=np.matrix('5 -3 -3; 5 0 -3; 5 -3 -3')
a2=np.matrix('-3 -3 5; -3 0 5; -3 -3 5')
a3=np.matrix('-3 -3 -3; 5 0 -3; 5 5 -3')
a4=np.matrix('-3 5 5; -3 0 5; -3 -3 -3')
a5=np.matrix('-3 -3 -3; -3 0 -3; 5 5 5')
a6=np.matrix('5 5 5; -3 0 -3; -3 -3 -3')
a7=np.matrix('-3 -3 -3; -3 0 5; -3 5 5')
a8=np.matrix('5 5 -3; 5 0 -3; -3 -3 -3')

dst1=cv2.filter2D(img,-1,a1)
dst2=cv2.filter2D(img,-1,a2)
dst3=cv2.filter2D(img,-1,a3)
dst4=cv2.filter2D(img,-1,a4)
dst5=cv2.filter2D(img,-1,a5)
dst6=cv2.filter2D(img,-1,a6)
dst7=cv2.filter2D(img,-1,a7)
dst8=cv2.filter2D(img,-1,a8)
S = img.shape
bv=np.zeros((S[0],S[1]))
temp = np.zeros(8)

for i in xrange(0,S[0]-1):
	for j in xrange(0,S[1]-1):
		temp[0]=dst1[i][j]
		temp[1]=dst2[i][j]
		temp[2]=dst3[i][j]
		temp[3]=dst4[i][j]
		temp[4]=dst5[i][j]
		temp[5]=dst6[i][j]
		temp[6]=dst7[i][j]
		temp[7]=dst8[i][j]
		if np.amax(temp) > 10:
			bv[i][j]= np.amax(temp)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(bv)
plt.title('Averaging'), plt.xticks([]), plt.yticks([])
plt.show()
