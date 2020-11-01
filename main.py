# Importing packages
#!/usr/bin/env python2
import numpy as np
import cv2   as cv
from statistics import mean
from statistics import stdev
from scipy      import stats
from matplotlib import pyplot as plt
print(cv.__version__)

#Input
cap         = cv.VideoCapture('./Working Videos/N123TwoToTwoToTwoBase.mp4') # Input of the baseline images
inputFeed   = cv.VideoCapture('./Working Videos/N1TwoToTwoToTwo.mp4') # Input feed
baseNames   = ['Bad blueberries','Legit blueberries','Wild berries','Not mixed grapes','Warm autumn','Not mixed grapes as well, but the other kind of grapes','Grape mix','Psychedelic berries','Psychedelic waterfall'] # Names of the objects
weight      = 2 # How much more should high intensity pixels count (Standard 2)
threshold   = 50 # To limit the disturbance of noise (0 If no noise)
intCutOff   = 0 # Cut off intensity values below the value. Can't be 0 if negative weight
changeLevel = 3 # Amount of successes or discards needed in a row to change state

# For testing / plotting
pValues = False # Choosing whether to show p-values or not
threshPlot  = True # Choosing whether to get histograms
threshNum   = 1 # Choosing which frame to get a histogram of (is 1-indexed)
threshBase  = 0 # Choosing which baseline image to plot the histogram of (is 0-indexed)
VideoName = "CornPeas.mp4" 
resultString = list([])
printOutput = True
printPercentages = True
printNumber = True

# Dont touch
count         = 0
purity        = 0.05 # At what limit to stop recycling (the p-value at which we reject that both images are from the same distribution, standard=0.05)
baselength    = int(cap.get(cv.CAP_PROP_FRAME_COUNT)) # Determining the amount of baseline images
baseHist      = np.zeros((baselength,3,256)) # Pre allocating space for baseline images
checkMatrix   = np.zeros((baselength,changeLevel))+1000
successVector = np.zeros(baselength)+1000
inputLength = int(inputFeed.get(cv.CAP_PROP_FRAME_COUNT)) # Input feed lenth

# Processing baseline images
while(cap.isOpened() and (count<baselength)):
  ret, baselineImg = cap.read()

  # Creating histograms for each color for each baseline image
  color = ('b','g','r')
  for i,col in enumerate(color):
    if col == 'b':
      baseHist[count,0] = cv.calcHist([baselineImg],[i],None,[256],[0,256]).transpose()
    if col == 'g':
      baseHist[count,1] = cv.calcHist([baselineImg],[i],None,[256],[0,256]).transpose()
    if col == 'r':
      baseHist[count,2] = cv.calcHist([baselineImg],[i],None,[256],[0,256]).transpose()

  count += 1

cap.release()
cv.destroyAllWindows()

# Pre allocating space
baselineRedPixel   = np.zeros((baselength,256));
baselineGreenPixel = np.zeros((baselength,256));
baselineBluePixel  = np.zeros((baselength,256));
redks   = np.zeros((baselength,2));
greenks = np.zeros((baselength,2));
blueks  = np.zeros((baselength,2));

# Limiting the baseline images with a threshold and adding a weight by intensity
for i in range (0, baselength):
  for x in range(intCutOff, 256):
    if baseHist[i,0,x] > threshold:
      baselineBluePixel[i,x] = baseHist[i,0,x]*x**weight
    if baseHist[i,1,x] > threshold:
      baselineGreenPixel[i,x] = baseHist[i,1,x]*x**weight
    if baseHist[i,2,x] > threshold:
      baselineRedPixel[i,x] = baseHist[i,2,x]*x**weight

# Trash classifying
cap = inputFeed   # Input feed

count = 0
    
while(cap.isOpened() and (count<inputLength)):
  ret, frame = cap.read()    
  TestImg = frame
  
  count += 1;
  if ((count-changeLevel+1>0) and (printOutput == True) and (printNumber == True)):
    print(count-changeLevel+1)  # Only for testing, delete afterwards
  
  # Creating histograms for each color for the current test image
  color = ('b','g','r')
  for i,col in enumerate(color):
    if col == 'b':
      b_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256])
    if col == 'g':
      g_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256])
    if col == 'r':
      r_hist_test = cv.calcHist([TestImg],[i],None,[256],[0,256]) 
  
  # Threshold testing, plotting histograms to evaluate noise levels
  if ((threshPlot == True) and (count ==  threshNum)):
    plt.figure(1)
    plt.xlabel('Intensity')
    plt.ylabel('Pixels')
    plt.xlim([intCutOff,256])
    plt.plot(b_hist_test,color = 'b',label='Blue channel')
    plt.plot(g_hist_test,color = 'g',label='Green channel')
    plt.plot(r_hist_test,color = 'r', label='Red channel')
    ymax_b_test = max(b_hist_test[intCutOff:256])
    ymax_g_test = max(g_hist_test[intCutOff:256])
    ymax_r_test = max(r_hist_test[intCutOff:256])
    plt.ylim([0,max([ymax_b_test,ymax_g_test,ymax_r_test])+10])
    plt.axhline(y=threshold, color='y', linestyle='-',label='Threshold (=%d)' % threshold)
    TplotTitle = 'Histogram of '+ VideoName +' frame %d' % threshNum
    plt.title(TplotTitle)
    plt.legend();
    plt.savefig('HistTestImg.png')
    cv.imwrite("testFrame%d.jpg" % count, frame)
    
    plt.figure(2)
    plt.title("Histogram of baseframe")
    plt.xlabel('Intensity')
    plt.ylabel('Pixels')
    plt.xlim([intCutOff,256])
    plt.plot(baseHist[threshBase,0],color = 'b',label='Blue channel')
    plt.plot(baseHist[threshBase,1],color = 'g',label='Green channel')
    plt.plot(baseHist[threshBase,2],color = 'r',label='Red channel')
    ymax_b_base = max(baseHist[threshBase,0][intCutOff:256])
    ymax_g_base = max(baseHist[threshBase,1][intCutOff:256])
    ymax_r_base = max(baseHist[threshBase,2][intCutOff:256])
    plt.ylim([0,max([ymax_b_base,ymax_g_base,ymax_r_base])+10])
    plt.axhline(y=threshold, color='y', linestyle='-',label='Threshold (=%d)' % threshold)
    plt.legend();
    plt.savefig('HistBaseImg.png')

  # Pre allocating space
  testRedPixel   = np.zeros(256);
  testGreenPixel = np.zeros(256);
  testBluePixel  = np.zeros(256);

  # Limiting the current test image with a threshold and adding a weight by intensity
  for x in range(intCutOff, 256):    
    if b_hist_test[x] > threshold:
      testBluePixel[x] = b_hist_test[x]*x**weight
    if g_hist_test[x] > threshold:
      testGreenPixel[x] = g_hist_test[x]*x**weight
    if r_hist_test[x] > threshold:
      testRedPixel[x] = r_hist_test[x]*x**weight

  # Using a 2-sample Kolmogorov-Smirnov test to compare the baseline images with the current test image for each color
  for i in range(0,baselength):
    redks[i]   = stats.ks_2samp(baselineRedPixel[i],testRedPixel)
    greenks[i] = stats.ks_2samp(baselineGreenPixel[i],testGreenPixel)
    blueks[i]  = stats.ks_2samp(baselineBluePixel[i],testBluePixel)
  p=0
  for i in range(0,baselength):
    if (pValues == True):
      print(redks[i,1])
      print(greenks[i,1])
      print(blueks[i,1])
      
    if ((redks[i,1]>purity) and (greenks[i,1]>purity) and (blueks[i,1]>purity)):
      for j in range(0,changeLevel):
        if (j==changeLevel-1):
          checkMatrix[i,j] = 1
        else:
          checkMatrix[i,j] = checkMatrix[i,j+1]
    else:
      for j in range(0,changeLevel):
        if (j==changeLevel-1):
          checkMatrix[i,j] = 0
        else:
          checkMatrix[i,j] = checkMatrix[i,j+1]
    if (sum(checkMatrix[i,:]) == changeLevel):
      successVector[i] = 1
    elif (sum(checkMatrix[i,:]) == 0):
      successVector[i] = 0      
    if (successVector[i] == 1):
      if (printOutput == True):
        print(baseNames[i])
      resultString.append(baseNames[i])
    elif (sum(successVector) == 0) and (p==0):
      if (printOutput == True):
        print('Discard')
      resultString.append('Discard')
      p=1
  if (printOutput == True):
    print(" ")

cap.release()
cv.destroyAllWindows()

#print(resultString)
if (printPercentages == True):
  resultLength = len(resultString)
  for i in range(0,baselength):
    print(str(resultString.count(baseNames[i])) + ' ' + str(baseNames[i]) + ' = ' + str(round(resultString.count(baseNames[i])/resultLength*100,2)) + str(' percent'))
  print(str(resultString.count('Discard')) + ' ' + str('Discards') + ' = ' + str(round(resultString.count('Discard')/resultLength*100, 2)) + str(' percent'))
