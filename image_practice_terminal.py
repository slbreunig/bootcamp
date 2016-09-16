Last login: Thu Sep 15 12:55:14 on ttys001
stephaniebreunig@slb [~]
% cd git/bootcamp
stephaniebreunig@slb [~/git/bootcamp]
% ipython
Python 3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: import skimage

In [2]: skimage.img_as_float?
Signature: skimage.img_as_float(image, force_copy=False)
Docstring:
Convert an image to double-precision floating point format.

Parameters
----------
image : ndarray
    Input image.
force_copy : bool
    Force a copy of the data, irrespective of its current dtype.

Returns
-------
out : ndarray of float64
    Output image.

Notes
-----
The range of a floating point image is [0.0, 1.0] or [-1.0, 1.0] when
converting from unsigned or signed datatypes, respectively.
File:      //anaconda/lib/python3.5/site-packages/skimage/util/dtype.py
Type:      function

In [3]: q
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-3-c3be117041a1> in <module>()
----> 1 q

NameError: name 'q' is not defined

In [4]: sign = '<'

In [5]: 1 sign 2
  File "<ipython-input-5-acf4c820e9a2>", line 1
    1 sign 2
         ^
SyntaxError: invalid syntax


In [6]: import seg_funcs

In [7]: image = skimage.io.imread('data/bsub_100x_phase.tif')

In [8]: plt.imshow(image, cmap=plt.cm.viridis)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-ec99e68abc80> in <module>()
----> 1 plt.imshow(image, cmap=plt.cm.viridis)

NameError: name 'plt' is not defined

In [9]: sns.set()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-df096ba8da79> in <module>()
----> 1 sns.set()

NameError: name 'sns' is not defined

In [10]: import numpy as np

In [11]: import matplotlib.pyplot as plt

In [12]: %matplotlib
Using matplotlib backend: MacOSX

In [13]: import seaborn as sns

In [14]: plt.imshow(image, cmap=plt.cm.viridis)
Out[14]: <matplotlib.image.AxesImage at 0x11b818320>

In [15]: cfp_image = skimage.io.imread('data/bsub_100x_CFP.tif')

In [16]: plt.imshow(cfp_image, cmap=plt.cm.gray)
Out[16]: <matplotlib.image.AxesImage at 0x124eb74a8>

In [17]: seg_funcs.how_pixel(cfp_image, show_image=True)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-17-0ac83bcf48e8> in <module>()
----> 1 seg_funcs.how_pixel(cfp_image, show_image=True)

AttributeError: module 'seg_funcs' has no attribute 'how_pixel'

In [18]: seg_funcs.hot_pixel(cfp_image, show_image=True)
Out[18]:
array([[103, 103, 103, ...,  98,  99,  99],
       [101, 102, 103, ...,  98,  99,  99],
       [101, 102, 102, ...,  98,  98,  99],
       ...,
       [101, 102, 104, ..., 101, 101, 101],
       [101, 102, 104, ..., 101, 101, 101],
       [101, 102, 104, ..., 101, 101, 101]], dtype=uint16)

In [19]: import seg_funcs as seg

In [20]: image=seg_funcs.hot_pixel(cfp_image, show_image=True)

In [21]: seg.illumination_correction(image)
Out[21]:
array([[  2.09500482e-05,   2.09980934e-05,   2.10460680e-05, ...,
         -1.52148298e-05,   4.12311804e-08,   3.80293210e-08],
       [ -9.31898852e-06,   5.98838652e-06,   2.12957067e-05, ...,
         -1.52069814e-05,   4.88393735e-08,   4.53957490e-08],
       [ -9.06939369e-06,   6.23830455e-06,   6.28694192e-06, ...,
         -1.51996450e-05,  -1.52030817e-05,   5.22594119e-08],
       ...,
       [  1.39711362e-06,   1.67878821e-05,   4.74394855e-05, ...,
          6.17593980e-06,   6.16100147e-06,   6.14636468e-06],
       [  1.41979092e-06,   1.68102423e-05,   4.74615317e-05, ...,
          6.05880079e-06,   6.04367982e-06,   6.02887536e-06],
       [  1.44224745e-06,   1.68323808e-05,   4.74833553e-05, ...,
          5.94241573e-06,   5.92712204e-06,   5.91215946e-06]])

In [22]: plt.show()

In [23]: plt.close()

In [24]: image=seg_funcs.hot_pixel(cfp_image, show_image=True)

In [25]: import seg_funcs as seg

In [26]: seg.thresh_hist(image)

In [27]: thresh_image = seg.threshold(image, 140, False)

In [28]: thresh_image = seg.threshold(image, 140, False)

In [29]: plt.imshow(thresh_image, cmap=plt.cm.viridis)
Out[29]: <matplotlib.image.AxesImage at 0x12ea1ccc0>

In [30]: plt.imshow(image, cmap=plt.cm.viridis)
Out[30]: <matplotlib.image.AxesImage at 0x12fe08dd8>

In [31]: thresh_image = seg.threshold(image, 140, False)

In [32]: plt.imshow(thresh_image, cmap=plt.cm.viridis)
Out[32]: <matplotlib.image.AxesImage at 0x1310eccf8>

In [33]: thresh_image = seg.threshold(image, 140, less_than=False, show_image=Tr
    ...: ue)

In [34]: thresh_image = seg.threshold(image, 140, less_than=True, show_image=Tru
    ...: e)

In [35]: thresh_image = seg.threshold(image, 140, less_than=True, show_image=Tru
    ...: e)

In [36]: import seg_funcs as seg

In [37]: thresh_image = seg.threshold(image, 140, less_than=True, show_image=Tru
    ...: e)

In [38]: thresh_image = seg.threshold(image, 140, less_than=False, show_image=Tr
    ...: ue)

In [39]: exit()
stephaniebreunig@slb [~/git/bootcamp]
% ipython
Python 3.5.2 |Anaconda custom (x86_64)| (default, Jul  2 2016, 17:52:12)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: %run seg_functions.py
ERROR:root:File `'seg_functions.py'` not found.

In [2]: %run seg_funcs.py

In [3]: import seg_funcs as seg

In [4]: image
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-4802fcebd761> in <module>()
----> 1 image

NameError: name 'image' is not defined

In [5]: cfp_image = skimage.io.imread('data/bsub_100x_CFP.tif')

In [6]: image = seg.hot_pixel(image)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-7a3dac6a317e> in <module>()
----> 1 image = seg.hot_pixel(image)

NameError: name 'image' is not defined

In [7]: image = seg.hot_pixel(cfp_image)


In [8]:

In [8]: %matplotlib
Using matplotlib backend: MacOSX

In [9]: phage_image = skimage.io.imread('data/bsub_100x_phage.tif')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-9-768b0182e788> in <module>()
----> 1 phage_image = skimage.io.imread('data/bsub_100x_phage.tif')

//anaconda/lib/python3.5/site-packages/skimage/io/_io.py in imread(fname, as_grey, plugin, flatten, **plugin_args)
     59
     60     with file_or_url_context(fname) as fname:
---> 61         img = call_plugin('imread', fname, plugin=plugin, **plugin_args)
     62
     63     if not hasattr(img, 'ndim'):

//anaconda/lib/python3.5/site-packages/skimage/io/manage_plugins.py in call_plugin(kind, *args, **kwargs)
    209                                (plugin, kind))
    210
--> 211     return func(*args, **kwargs)
    212
    213

//anaconda/lib/python3.5/site-packages/skimage/io/_plugins/tifffile_plugin.py in imread(fname, dtype, **kwargs)
     27     if 'img_num' in kwargs:
     28         kwargs['key'] = kwargs.pop('img_num')
---> 29     with open(fname, 'rb') as f:
     30         tif = TiffFile(f)
     31         return tif.asarray(**kwargs)

FileNotFoundError: [Errno 2] No such file or directory: 'data/bsub_100x_phage.tif'

In [10]: phage_image = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif
    ...: ')

In [11]: ill_image=seg.illumination(phage_image)

In [12]: Sep 15 21:14:55  python[21234] <Warning>: void CGSUpdateManager::log()
In [12]:

In [12]: otsu_image = otsu(ill_image)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-12-0ba07aad78c3> in <module>()
----> 1 otsu_image = otsu(ill_image)

/Users/stephaniebreunig/git/bootcamp/seg_funcs.py in otsu(image, show_image)
    112
    113     #apply thresholding
--> 114     thresh = skimage.threshold.filters_otsu(image)
    115
    116     #perform segmentation

AttributeError: module 'skimage' has no attribute 'threshold'

In [13]: import seg_funcs as seg

In [14]: otsu_image = otsu(ill_image)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-14-0ba07aad78c3> in <module>()
----> 1 otsu_image = otsu(ill_image)

/Users/stephaniebreunig/git/bootcamp/seg_funcs.py in otsu(image, show_image)
    112
    113     #apply thresholding
--> 114     thresh = skimage.filters.threshold_otsu(image)
    115
    116     #perform segmentation

AttributeError: module 'skimage' has no attribute 'threshold'

In [15]: %run seg_funcs.py

In [16]: otsu_image = otsu(ill_image)

In [17]: seg_image, num_cells = segmentation_mask(otsu_image)

In [18]: fitc_image = skimage.io/imread('data/HG105_images/noLac_FITC_0004.tif')
    ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-18-90835d19254b> in <module>()
----> 1 fitc_image = skimage.io/imread('data/HG105_images/noLac_FITC_0004.tif')

NameError: name 'imread' is not defined

In [19]: fitc_image = skimage.io.imread('data/HG105_images/noLac_FITC_0004.tif')
    ...:

In [20]: cut_image = fitc_image*seg_image

In [21]: plt.imshow(cut_image, cmap=plt.cm.Grays_r)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-21-236b0b239b35> in <module>()
----> 1 plt.imshow(cut_image, cmap=plt.cm.Grays_r)

AttributeError: module 'matplotlib.cm' has no attribute 'Grays_r'

In [22]: plt.imshow(cut_image, cmap=plt.cm.Greys_r)
Out[22]: <matplotlib.image.AxesImage at 0x12570ad68>

In [23]: plt.imshow(cut_image, cmap=plt.cm.Greys_r)
Out[23]: <matplotlib.image.AxesImage at 0x11c2b2550>

In [24]:

In [25]: properties = skimage.measure.regionprops(cut_image)

In [26]: intensities = np.array([prop.mean_intensity for prop in properties])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-26-b14a9623c96d> in <module>()
----> 1 intensities = np.array([prop.mean_intensity for prop in properties])

<ipython-input-26-b14a9623c96d> in <listcomp>(.0)
----> 1 intensities = np.array([prop.mean_intensity for prop in properties])

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in mean_intensity(self)
    210
    211     def mean_intensity(self):
--> 212         return np.mean(self.intensity_image[self.image])
    213
    214     def min_intensity(self):

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in wrapper(obj)
     69
     70         if not ((prop in cache) and obj._cache_active):
---> 71             cache[prop] = f(obj)
     72
     73         return cache[prop]

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in intensity_image(self)
    193     def intensity_image(self):
    194         if self._intensity_image is None:
--> 195             raise AttributeError('No intensity image specified.')
    196         return self._intensity_image[self._slice] * self.image
    197

AttributeError: No intensity image specified.

In [27]: int_1 = properties[0].mean_intensity
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-27-a087014d76c7> in <module>()
----> 1 int_1 = properties[0].mean_intensity

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in mean_intensity(self)
    210
    211     def mean_intensity(self):
--> 212         return np.mean(self.intensity_image[self.image])
    213
    214     def min_intensity(self):

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in wrapper(obj)
     69
     70         if not ((prop in cache) and obj._cache_active):
---> 71             cache[prop] = f(obj)
     72
     73         return cache[prop]

//anaconda/lib/python3.5/site-packages/skimage/measure/_regionprops.py in intensity_image(self)
    193     def intensity_image(self):
    194         if self._intensity_image is None:
--> 195             raise AttributeError('No intensity image specified.')
    196         return self._intensity_image[self._slice] * self.image
    197

AttributeError: No intensity image specified.

In [28]: properties = skimage.measure.regionprops(seg_image, intensity_image=fitc_image)

In [29]: properties[0].mean_intensity
Out[29]: 200.00930232558139

In [30]: intensities = np.empty(len(range(num_cells)))

In [31]: for i in range(num_cells):
    ...:     intensities[i]=properties[i].mean_intensity
    ...:

In [32]: intensities
Out[32]:
array([ 200.00930233,  295.64189794,  151.609375  ,  240.42056075,
        207.83993399,  193.58680556,  444.45673077,  206.76586433,
        222.60080645,  213.57009346,  194.47665056,  235.62244898,
        218.72706935,  213.68362832,  108.77083333,  105.171875  ,
        105.88888889,  106.        ,  106.        ,  149.08241758,
        219.69685767,  196.94710327,  108.        ,  108.        ,
        104.5       ,  274.11494253,  230.02064897,  202.85141509,
        201.32010582,  110.        ,  102.        ,  189.14390602,
        104.875     ,  104.69230769,  106.66666667,  106.        ])
