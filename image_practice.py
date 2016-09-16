import numpy as np
import seaborn as sns
sns.set()
import matplotlib.pyplot as plt
import seg_funcs as seg
import skimage.io
import skimage.filters
import skimage.segmentation
import skimage.measure
import operator

#load images
HG105_images_list = ['data/noLac_FITC_0000.tif',
                    'data/noLac_FITC_0001.tiff',
                    'data/noLac_FITC_0002.tiff',
                    'data/noLac_FITC_0003.tiff',
                    'data/noLac_FITC_0004.tiff',
                    'data/noLac_FITC_0005.tiff',
                    'data/noLac_FITC_0006.tiff',
                    'data/noLac_FITC_0007.tiff',
                    'data/noLac_FITC_0008.tiff',
                    'data/noLac_phase_0000.tiff',
                    'data/noLac_phase_0001.tiff',
                    'data/noLac_phase_0002.tiff',
                    'data/noLac_phase_0003.tiff',
                    'data/noLac_phase_0004.tiff',
                    'data/noLac_phase_0005.tiff',
                    'data/noLac_phase_0006.tiff',
                    'data/noLac_phase_0007.tiff',
                    'data/noLac_phase_0008.tiff']

#separate images by type:
#empty FITC list:
fitc_list = []
#empty phase list:
phase_list = []

for _, name in enumerate(HG105_images_list):
    if "FITC" in name:
        fitc_list.append(name)
    elif "phase" in name:
        phase_list.append(name)
