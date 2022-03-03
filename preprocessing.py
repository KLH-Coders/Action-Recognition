import os
import sys
import itertools
import math
import logging
import json
import re
import random
from collections import OrderedDict
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.patches import Polygon

import utils
import visualize
from visualize import display_images
import model as modellib
from model import log

%matplotlib inline 

ROOT_DIR = os.getcwd()

# MS COCO Dataset
import coco
config = coco.CocoConfig()
COCO_DIR = r"C:\Users\sai kamal\AppData\Local\Programs\Python\Python310\Lib\site-packages\pycocotools\coco"  # TODO: enter value here
