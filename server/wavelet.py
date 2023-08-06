import numpy as np
import pywt
import cv2

def w2d(img,mode='haar',level=1):
  # convert to grey
  imArray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
  # convert to float
  imArray=np.float32(imArray)
  imArray/=255
  #compute cofficients
  coffec=pywt.wavedec2(imArray,mode,level=level)

  #process cofficients
  coffe_H=list(coffec)
  coffe_H[0]*=0;

  # reconstuction
  imArray_H=pywt.waverec2(coffe_H,mode)
  imArray_H*=255;
  imArray_H=np.uint8(imArray_H)
  return imArray
