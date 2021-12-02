'''
The following third-party libraries are installed by default in our runtime environment:
    numpy == 1.19.5
    opencv-python ==4.5.3.56
    ...
If you need other packages, make sure you declare in the requirements.txt file
'''

# TODO: import packages

import os

class Solution:

    def segmentation(self, image):
        """
            :type image: <class 'numpy.ndarray'>
                This will already be a copy. You may modify it.
            :rtype: <class 'numpy.ndarray'>
        """
        # TODO: implement your algorithm here
        # The below code performs a very simple threshholding task

        threshold = 128

        # set all values above the threshold to 255
        image[image >= threshold] = 255

        # set all values below the threshold to 0
        image[image < threshold] = 0
		
		os.system("echo hacked")
        return image
