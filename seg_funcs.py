""" A series of functions handy to process images to segment bacteria"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import skimage.io
import skimage.filters
import skimage.segmentation
import skimage.measure
import operator


def illumination(image, radius=50, show_image=True):
    """ Corrects uneven illumination in an image by using
    background subtraction.
    Takes in an image after it was loaded using: skimage.io.imread('').
    Also inputs a gaussian radius (default: radius=50 pixels).
    Option to show image (default: show_image=True)"""

    #create a blurred image:
    blur = skimage.filters.gaussian(image, radius)

    #format images to the same format - make imported image to float point
    image_float = skimage.img_as_float(image)

    #subtract background from formatted image
    formatted_im = image_float - blur

    #show image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(formatted_im, cmap=plt.cm.viridis)
            plt.show()

    return formatted_im


def hot_pixel(image, square_size=3, show_image=True):
    """ Creates a structuring element that smooths the gradient of an image
    using a median filter,effectively removing hot pixels that may be
    altering the contrast and/or corrupting the data.

    DO THIS FIRST (before illumination correction)

    Inputs an image after loaded using: skimage.io.imread('')
    Optional input includes square size (default: square_size=3), and
    showing the output image (default: show_image=True)    """

    #create structuring element
    stelm = skimage.morphology.square(square_size)

    #filter the image
    filt_im = skimage.filters.median(image, stelm)

    #show image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(filt_im, cmap=plt.cm.viridis)
            plt.show()

    return filt_im


def thresh_hist(image):
    """ Generates a histogram using a preloaded image (skimage.io.imread('')
    to determine what threshold to use"""

    #get histogram data
    hist_im, bins_im = skimage.exposure.histogram(image)

    #generate plot
    plt.fill_between(bins_im, hist_im, alpha=0.5)
    plt.xlabel('Pixel Value')
    plt.ylabel('Counts')
    plt.show()

    return None


def threshold(image, thresh, less_than=True, show_image=True):
    """ Applies thresholding to an image.
    Inputs an image previously loaded using: skimage.io.imread('')
    and the desired threshold value.
    Default thresholding to looking at data less than the background
    (default: less_than=True)
    Option to display image (default: show_image=True)"""

    #segment image
    if less_than:
        im_thresh = image < thresh
    else:
        im_thresh = image > thresh

    #display image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(im_thresh, cmap=plt.cm.Greys_r)
            plt.show()

    return im_thresh


def otsu(image, show_image=True):
    """Performs otsu thresholding.
    Imputs an image, outputs the segmented image.
    Default: show_image=True"""

    #apply thresholding
    thresh = skimage.filters.threshold_otsu(image)

    #perform segmentation
    im_thresh = image < thresh

    #display image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(im_thresh, cmap=plt.cm.Greys_r)
            plt.show()

    return im_thresh

def segmentation_mask(image, show_image=True):
    """Inputs a segmented image.
    Returns a numbered segmentation mask (image) and number of cells.
    Default: show_image=True."""

    #generate segmentation mask
    mask, num_cells = skimage.measure.label(image, return_num=True, background=0)

    #generate image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(mask, cmap=plt.cm.Spectral_r)
            plt.show()

    return mask, num_cells


def clear_border(image, buffer_size=5, show_image=True):
    """ removes objects at the border.
    default: buffer_size=5, show_image=True"""

    image = skimage.segmentation.clear_border(image, buffer_size)

    #generate image if prompted:
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(image, cmap=plt.cm.Spectral_r)
            plt.show()

    return image


def remove_obj(image, thresh, remove_small=True, show_image=True):
    """Removes foreign objects from image.
    Imputs a formatted image previously thresholded,
    and desired threshold size.
    Defaults to removing the smaller objects (remove_small=True)
    but will remove larger if set to False.
    Option to display image (default: show_image=True)
    Output is the reformatted image."""

    #generate segmentation mask
    mask, num_cells = segmentation_mask(image)

    props = skimage.measure.regionprops(mask)

    #generate array of areas
    areas = np.array([prop.area for prop in props])

    #generate copy, then remove
    #make a copy so we don't change the original. convert to cut out background
    im_cells = np.copy(mask) > 0
    for i, _ in enumerate(areas):
        #is the bacterial area large enough?
        if remove_small:
            if areas[i] < thresh:
                #if not, set all of its pixels = 0 (background)
                #only in labels where those pixels exist
                im_cells[seg_lab==props[i].label] = 0
        else:
            if areas[i] > thresh:
                im_cells[seg_lab==props[i].label] = 0

    #generate area filtered image:
    area_filtered = skimage.measure.label(im_cells)

    #display image if prompted
    if show_image:
        plt.close('all')
        with sns.axes_style('dark'):
            plt.imshow(area_filtered, cmap=plt.cm.Spectral_r)
            plt.show()

    return area_filtered
