import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#for image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

#load images
#argument is path to image
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

#open image using terminal (python): ! open '[data path]'
#completely black image
#need to reformat to 12 bit image, instead of default 16 bit

# #show the phase imate
# plt.imshow(phase_im)

#colors right now are based off of lookup tables, basically arbitrary
#cmap = colormap

#plt.cm.<tab> -- gives you list of color schemes you can use
#this one reverses grey coloring:
plt.imshow(phase_im, cmap=plt.cm.Greys_r)

plt.close()
#colormap used can really imact how you interpret/view the image
#Don't use jet!

#another:
plt.imshow(phase_im, cmap=plt.cm.viridis)

plt.close()
#plot the histogram of the phase image
#could write a loop to extract all data, etc - BUT this has already been done
#use .exposure (above) to get this
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
#now we can just plot bins vs histogram
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

#big spike = background of the image
#bacteria are dark = pixel value is ~200 (little hump)

#apply a threshold to image to find the bacteria
#picking threshold is important
thresh = 260
im_phase_thresh = phase_im < thresh

plt.close()

#to get rid of gridlines
#these settings are on seaborn webpage
#this one has a dark background, no grid
#getting bools, so now segments will be white on a black bkgd with
#our colormap settings
with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)
plt.close()

#Now looking at fluorescence image
#look at fluorescence image
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

plt.close()
#there is a nasty bright pixel that is ruining our contrast
#slice out the region with the hot pixel (in predetermined location)
#the following gives an image of a hot pixel
#the
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

#do median filtering to remove outliers
#need to import .morphology and .filters
#generating a cross:
#interpolate removes the computer trying to interpolate the image
# selem = skimage.morphology.disk(1)
# plt.imshow(selem, interpolate='nearest')

plt.close()
#generate a structural element
#get rid of hot pixels
#apply median filter across the entire image

#create the structuring element
selem = skimage.morphology.square(3)
#perform the filter using the element. This smooths the gradient
cfp_filt = skimage.filters.median(cfp_im, selem)
with sns.axes_style('dark'):
    plt.imshow(cfp_filt, cmap=plt.cm.viridis)

#look at histogram of median filered image
cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.close()
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')
plt.show()

#define a threshold
cfp_thresh = cfp_filt > 120
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

#appy an otsu threshold
phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

plt.close()
#generates a new figure object
with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase otsu')

    plt.figure()
    plt.imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    plt.title('cfp otsu')
