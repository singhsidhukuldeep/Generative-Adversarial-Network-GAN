from PIL import Image
import numpy as np

ipath = "./images/%d.png"

import imageio
images = []
for i in range(1,299):
    pathnow = ipath%(i*1000)
    print ("File running " + pathnow)
    images.append(imageio.imread(pathnow))
imageio.mimsave('./progress.gif', images, fps=2)
