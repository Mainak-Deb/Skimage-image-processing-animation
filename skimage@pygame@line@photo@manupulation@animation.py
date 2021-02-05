import time,math,random
import pygame,sys
from pygame.locals import *
import math
from skimage import io

img1=io.imread("python image processing/netaji3.jpg")

k=((len(img1)*len(img1[1]))/10000)**(.5)

rx=len(img1)/k
ry=len(img1[1])/k

r=int(len(img1)/rx)
c=int(len(img1[1])/ry)

screenlenth=800
dis=screenlenth/100

screenlenth=800

pygame.init()
screen=pygame.display.set_mode((int(dis*ry),int(dis*rx)))
pygame.display.set_caption("PHOTO MANUPULATION 2")
maxj=[]
maxi=0

for i in range(int(c/2),len(img1),c):
    maxj.append(0)
mitt=0
sitt=0

sp=2

running=True
while running:
    screen.fill((255,255,255))       
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    maxj[int(mitt)]=int(r/2)+int(r*int(sitt))
    
    for i in range(int(c/2),len(img1)-2,c):
        for j in range(int(r/2),maxj[int((i-int(c/2))/c)],r):
            if((j<len(img1[1])-4)):
                colour=(((img1[i][j][0])*0.3)+((img1[i][j][0])*0.59)+((img1[i][j][0])*0.11))
                pygame.draw.line(screen,(0,0,0),(int(dis*((j-int(c/2))/c)),int(dis*((i-int(r/2))/r))),(int(dis*(((j-int(c/2))/c)+1)),int(dis*(((i-int(r/2))/r)))),(int((dis)*((255-colour)/255))))
                
    if(mitt<len(maxj)-1):
        if(maxj[int(mitt)]<len(img1[1])-4):
              sitt=sitt+sp
        else:
            sitt=0
            mitt=mitt+1
        sp=sp+.04
    pygame.display.update()                
