import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#using this instead of sns.set() and with sns.axes_style('dark')
sns.set_style('dark')


import skimage.io
import skimage.filters
import skimage.measure
import skimage.segmentation


#load an example phase image
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

#show the image
plt.imshow(phase_im, cmap=plt.cm.viridis)

#illumination is off on this image - it is uneven
#now do background subtraction
#uneven illumination is on a large scale in this instance, so we can...

#apply gaussian blur to blur out the details and look at the uneven ill.
#choose radius of blur larger than individual bacterium: 50.0 pixels
im_blur = skimage.filters.gaussian(phase_im, 50.0)

#show the blurred image
plt.imshow(im_blur, cmap=plt.cm.viridis)

#phase_im and im_blur are physically arrays
#we want to subtract these two images to remove the background
#need to make sure they are the same data type - phase_im is unit16
#and im_blur is float64
#need to convert phase_im to a float before subtraction

#convert phase image to a float64
phase_float = skimage.img_as_float(phase_im)
#background subtraction
phase_sub = phase_float - im_blur

#show original phase image
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')
#show altered, subtracted image
plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

#Chambolle total variation filter

#apply otsu thresholding
thresh = skimage.filters.threshold_otsu(phase_sub)
#'perform' segmentation
seg = phase_sub < thresh

#plot our segmentation
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)
plt.show()

#label our bacteria
#will return total number of objects that have been segmented
#make background, nonlabeled objects numbered 0
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)

plt.close()
#show labeled images
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)

#to look at an individual object:
#plt.imshow(seg_lab==n) where n is an integer value 1 to num_cells
#1 starts at the top right

#compute the region properties and extract areas of each object
#know interpixel distance:
ip_dist = 0.063 #um per pixel
#seg_lab = segmentation map
props = skimage.measure.regionprops(seg_lab)
#now can do props[0].area - gives area of object labeled 1 (index=0)

#get the areas as an array
areas = np.array([prop.area for prop in props])
#define cutoff value for area of what we say a bacterium must surpass
cutoff = 300

#make a copy so we don't change the original. convert to cut out background
im_cells = np.copy(seg_lab) > 0
for i, _ in enumerate(areas):
    #is the bacterial area large enough?
    if areas[i] < cutoff:
        #if not, set all of its pixels = 0 (background)
        #only in labels where those pixels exist
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)

#show image
plt.figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
