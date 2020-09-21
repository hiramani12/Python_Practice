from PIL import Image #package to read image metadatas.
from PIL.ExifTags import TAGS  # Collection of name of image metadata and number associated with it
import pandas as pd
import glob
from datetime import datetime
from datetime import timedelta
import numpy as np
import math as m
from sklearn.cluster import DBSCAN # clustering alogirthm
import sklearn.utils
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_toolkits import mplot3d
import matplotlib.colors as colors
import matplotlib.cm as cmx

# Path where the photo to read is stored

path = '/Users/hiramani/Desktop/Python Practice/HeHe/Lawson re-fuel, sheen on Pine/'

files_image = [f for f in glob.glob(path + "*.JPG", recursive=True)] # Returns the list with path of the images with "JPG" extension based
file_names_image = [f.split('/')[-1] for f in files_image]  # Exact file names from the given path

