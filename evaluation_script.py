from imageio import imread
import numpy as np
from numpy import loadtxt
from keras.models import load_model
from PIL import Image


lat = -35.363250
lon = 149.165250
image = imread('https://maps.googleapis.com/maps/api/staticmap?center=38.031627,-85.928664&zoom=18&scale=1&size=224x224&maptype=satellite&format=png&visual_refresh=true&key=YourAPIKey')
image = image[:,:,0:3]
im = Image.fromarray(image)
im.save("image.jpeg")
image = np.reshape(image, (-1, 224, 224, 3))

model = load_model('modified_NWPU_RESISC45_vgg16.model')
res = model.predict(image)
if np.argmax(res) == 34:
    print("runway detected!")
    print("latitude: %f" % lat)
    print("longitude: %f" % lon)
