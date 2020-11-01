#!/usr/bin/env python2
import numpy as np
import cv2 as cv
from statistics import mean
from statistics import stdev
from scipy import stats
print(cv.__version__)
from matplotlib import pyplot as plt

weight      = 2
threshold   = 0
purity      = 0.1
changeLevel = 0.00000015
count       = 0

#cap = cv.VideoCapture('video1.mp4')
cap = cv.VideoCapture('video2.mp4')

#ControlImg = cv.imread('ControlImg.png')

print("Starting")
print(' ')
    
while(cap.isOpened() and (count<100)):
  ret, frame = cap.read()
  if (count == 0):
    ControlImg = frame
    
  TestImg = frame
  
  print(count)
  count += 1;

  color = ('b','g','r')
  for i,col in enumerate(color):

    if col == 'b':
      b_hist_control = cv.calcHist([ControlImg],[i],None,[256],[0,256])
      b_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256])
    if col == 'g':
      g_hist_control = cv.calcHist([ControlImg],[i],None,[256],[0,256])
      g_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256])
    if col == 'r':
      r_hist_control = cv.calcHist([ControlImg],[i],None,[256],[0,256])
      r_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256])
      
  plt.figure(0)
  plt.plot(b_hist_control,color = 'b')
  plt.plot(g_hist_control,color = 'g')
  plt.plot(r_hist_control,color = 'r')
  plt.xlim([0,256])

  plt.savefig('HistControlImg.png')

  plt.figure(1)
  plt.plot(b_hist_test,color = 'b')
  plt.plot(g_hist_test,color = 'g')
  plt.plot(r_hist_test,color = 'r')
  plt.xlim([0,256])

  plt.savefig('HistTestImg.png')

  controlRedPixel   = np.zeros(256);
  controlGreenPixel = np.zeros(256);
  controlBluePixel  = np.zeros(256);
  testRedPixel   = np.zeros(256);
  testGreenPixel = np.zeros(256);
  testBluePixel  = np.zeros(256);

  for x in range(0, 256):
    # Control
    if b_hist_control[x] > threshold:
      controlBluePixel[x] = b_hist_control[x]*x**weight
    if g_hist_control[x] > threshold:
      controlGreenPixel[x] = g_hist_control[x]*x**weight
    if r_hist_control[x] > threshold:
      controlRedPixel[x] = r_hist_control[x]*x**weight
    
    # test
    if b_hist_test[x] > threshold:
      testBluePixel[x] = b_hist_test[x]*x**weight
    if g_hist_test[x] > threshold:
      testGreenPixel[x] = g_hist_test[x]*x**weight
    if r_hist_test[x] > threshold:
      testRedPixel[x] = r_hist_test[x]*x**weight
      
  # Control Percentages
  controlPixelSum = sum(controlRedPixel)+sum(controlBluePixel)+sum(controlGreenPixel)
  controlRedPixelPercent = sum(controlRedPixel) / controlPixelSum * 100
  controlGreenPixelPercent = sum(controlGreenPixel) / controlPixelSum * 100
  controlBluePixelPercent = sum(controlBluePixel) / controlPixelSum * 100
  # Test Percentages
  testPixelSum = sum(testRedPixel)+sum(testBluePixel)+sum(testGreenPixel)
  testRedPixelPercent = sum(testRedPixel) / testPixelSum * 100
  testGreenPixelPercent = sum(testGreenPixel) / testPixelSum * 100
  testBluePixelPercent = sum(testBluePixel) / testPixelSum * 100


  redks = stats.ks_2samp(controlRedPixel,testRedPixel)
  greenks = stats.ks_2samp(controlGreenPixel,testGreenPixel)
  blueks = stats.ks_2samp(controlBluePixel,testBluePixel)

  # p > 0.05 ~ good
  print(redks[1])
  print(greenks[1])
  print(blueks[1])
  
  if (redks[1]<purity):
    print("Error")
  elif (greenks[1]<purity):
    print("Error")
  elif (blueks[1]<purity):
    print("Error")
  else:
    print("Success")
  
  print(" ")

  if ((redks[1]<changeLevel) and (greenks[1]<changeLevel) and (blueks[1]<changeLevel)):
    print("-----------------")
    print("Changing level!")
    print("-----------------")
    print(" ")
    ControlImg = frame
    cv.imwrite('ChangeLevel.png',frame)
    

  
cap.release()
cv.destroyAllWindows()
