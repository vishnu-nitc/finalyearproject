import numpy as np
import cv2
img = cv2.imread('10_left.jpeg')

#cv2.waitKey(0);
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

px = img2[100,100]
k = img2.shape
l = img2.size


print px
print k
print l
t=0
t2=0
t3=0
t4=0
flag3=0
for x in range(k[0]-1,0,-1):
	for y in range(k[1]-1,0,-1):
		if img2[x,y] != 0:
		
			t= x
			
			
			break
			
print t,t2
cv2.line(img2,(0,t),(4751,t),(255),5)
#cv2.line(img2,(4600,0),(4600,4439),(255),5)


'''for y in range(k[1]-1,0,-1):
	for x in range(k[0]-1,0,-1):
		if img2[x,y] != 0:
		
			t2= y
			
			
			break
cv2.line(img2,(t2,0),(t2,3167),(255),5)'''

'''for y in range(0,k[1]-1,1):
	for x in range(k[0]-1,0,-1):
		if img2[x,y] != 0:
			t3=y
			for 
				break
print t3			
cv2.line(img2,(t3,0),(t3,3167),(255),5)
for x in range(0,k[0]-1,1):
	for y in range(0,k[1]-1,1):
		if img2[x,y] != 0:
		
			t= x
			
			
			break
			
print t,t2
cv2.line(img2,(0,t),(4751,t),(255),5)'''
#cv2.imshow('image',img2);
#cv2.waitKey(0);
#cv2.imwrite('test.jpeg',black)
cv2.imwrite('filename2.jpeg',img2)
