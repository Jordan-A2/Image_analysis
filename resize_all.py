#!/usr/bin/env python3
#!/usr/bin/env python2
import numpy as np
import glob
import cv2

INCLUDE_NOISE = False

n_images = 200
W = 200. #width of the pictures after Resizeing
imgs = []#= np.zeros((n_images, 400, 600, 3), dtype=np.uint8)

#image = cv2.imread(" 1.jpg")
#print(" 1.jpg")
#imgs.append(image)

#  cv.imread("%d.jpg" % count, frame)
#print('files:', file)
for k in range(n_images):
    x=(k+1)#*4
    #cv2.imread("%d.jpg" % x, image)
    #print('in the loop ',x)
    #print(myFile)
#x=100
    #print(" %d.jpg" % x)
    #image = cv2.imread(" %d.jpg" % x)


    filename = " %d.jpg" % x

    oriimg = cv2.imread(filename)
    height, width, depth = oriimg.shape
    imgScale = W/width
    newX,newY = oriimg.shape[1]*imgScale, oriimg.shape[0]*imgScale
    newimg = cv2.resize(oriimg,(int(newX),int(newY)))
    filenameRz = "rz%d.jpg" % x
    cv2.imwrite(filenameRz,newimg)
    print("filenameRz: ",filenameRz)


    #img = cv2.imread(' 100.jpg')

    dimensions = newimg.shape
    imgs.append(newimg)

#print('imgs shape:', np.array(imgs).shape)
#print('imgs[0] shape: ', image.shape)
print('1.jpg shape: ', oriimg.shape)
print('100.jpg dimensions: ', dimensions)


# Generate images/frames
print('Generate starting to write data')
# Write data and video output
np.save(f'video.npy', np.array(imgs))
codec = 'avc1'  # Alternative 'mp4v' 'xvid'
frame_rate = 5
fourcc = cv2.VideoWriter_fourcc(*codec)
out = cv2.VideoWriter("videoRz.mp4", fourcc, frame_rate, imgs[0].shape[:2][::-1])
for frame in imgs:
    out.write(frame)
out.release()#()()


#First number is amount of baseline imgs
baseImgs = []#np.zeros((2, 400, 600, 3), dtype=np.uint8)
baseImgs.append(imgs[0])
baseImgs.append(imgs[n_images-1])
#baseImgs[0,:,:,:] = imgs[0,:,:,:]
#baseImgs[1,:,:,:] = imgs[99,:,:,:]
#baseImgs[1,:,:,:] = imgs[99,:,:,:]
#baseImgs[1,:,:,:] = imgs[99,:,:,:]

np.save(f'video.npy', np.array(baseImgs))
codec = 'avc1'  # Alternative 'mp4v' 'xvid'
frame_rate = 5
fourcc = cv2.VideoWriter_fourcc(*codec)
out = cv2.VideoWriter("baseVideoRz.mp4", fourcc, frame_rate, baseImgs[0].shape[:2][::-1])
for frame in baseImgs:
    out.write(frame)
out.release()
