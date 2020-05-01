import shutil
import os
from glob import glob
source = 'NWPU-RESISC45/wetland/'
dest1 = 'train2/'

files = os.listdir(source)

for f in files:
    shutil.move(source+f, dest1)
