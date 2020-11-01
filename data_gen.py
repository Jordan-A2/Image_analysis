#!/usr/bin/env python3
#!/usr/bin/env python2
import numpy as np
import cv2

INCLUDE_NOISE = True

n_images = 100
n_circle = 200
imgs = np.zeros((n_images, 400, 600, 3), dtype=np.uint8)
colors = [[100, 200, 100], [100, 100, 200], [100, 100, 100], [100, 200, 200]]
radius = 20

# Define properbility function
p = lambda i: .25 * np.ones((4,)) + [.15, -.05, -.05, -.05] * (i == 3)

# Single transition
sigmoid = lambda x: 1 / (1 + np.exp((50 - x) / 6))
p = lambda i: [sigmoid(i), sigmoid(i), 1 - sigmoid(i), 1 - sigmoid(i)]

# Dual transition
sigmoid = lambda x, X: 1 / (1 + np.exp((X - x) / 6))
p = lambda i: [sigmoid(i, 33) - sigmoid(i, 67), sigmoid(i, 67), 1 - sigmoid(i, 33), 1 - sigmoid(i, 33)]

# Generate images/frames
for i, img in enumerate(imgs):
    choices = np.random.choice(np.arange(len(colors)), size=n_circle, p=p(i) / np.sum(p(i)))
    us = np.random.randint(0, imgs.shape[1], n_circle)
    vs = np.random.randint(0, imgs.shape[2], n_circle)
    for choice, u, v in zip(choices, us, vs):
        color = colors[choice]
        if INCLUDE_NOISE:
            color = list(int(i) for i in color + np.random.randint(-30, 30, size=(3,)))
        cv2.circle(img, (v, u), radius, color, thickness=-1)

# Write data and video output
np.save(f'video.npy', np.array(imgs))
codec = 'avc1'  # Alternative 'mp4v' 'xvid'
frame_rate = 5
fourcc = cv2.VideoWriter_fourcc(*codec)
out = cv2.VideoWriter("video.mp4", fourcc, frame_rate, imgs[0].shape[:2][::-1])
for frame in imgs:
    out.write(frame)
out.release()

#First number is amount of baseline imgs
baseImgs = np.zeros((2, 400, 600, 3), dtype=np.uint8)
baseImgs[0,:,:,:] = imgs[0,:,:,:]
baseImgs[1,:,:,:] = imgs[99,:,:,:]
#baseImgs[1,:,:,:] = imgs[99,:,:,:]
#baseImgs[1,:,:,:] = imgs[99,:,:,:]

np.save(f'video.npy', np.array(baseImgs))
codec = 'avc1'  # Alternative 'mp4v' 'xvid'
frame_rate = 5
fourcc = cv2.VideoWriter_fourcc(*codec)
out = cv2.VideoWriter("videoBase.mp4", fourcc, frame_rate, baseImgs[0].shape[:2][::-1])
for frame in baseImgs:
    out.write(frame)
out.release()
