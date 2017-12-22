import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from PIL import Image

im = Image.open("gazellepic.jpg")
resize_factor = 0.05
resize_params = tuple([int(x*resize_factor) for x in im.size])
im_resized = im.resize(resize_params,Image.ANTIALIAS)
im_values = np.array(im_resized)

r = im_values[:,:,0].flatten()
g = im_values[:,:,1].flatten()
b = im_values[:,:,2].flatten()

colors = np.array([[r,g,b] for r,g,b in zip(r,g,b)])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(r,g,b, c= colors/255.0)
plt.show()
