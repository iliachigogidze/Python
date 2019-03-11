import rawpy
import imageio

img = '/home/ilia/Downloads/1.DNG'

raw = rawpy.imread(img)
rgb = raw.postprocess()
imageio.imsave('default.jpg', rgb)