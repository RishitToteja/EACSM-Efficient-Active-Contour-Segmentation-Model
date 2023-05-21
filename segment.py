import math
import matplotlib.pyplot as plt
import skimage.data
import skimage.color
import numpy as np
import skimage.filters
import skimage.segmentation
from skimage import io
from scipy.interpolate import splprep, splev, BSpline, splrep
import scipy.ndimage
import helper
from math import sqrt

def getContour(pointsLeft, pointsRight, image_path, output_pth):
    print("Image Path in Segment Method - "+image_path)
    print(len(pointsLeft))
    print(len(pointsRight))
    image2 = io.imread(image_path)
    image2 = skimage.filters.gaussian(image2, 6.0, channel_axis=None)

    # Append the first point to the end to close the contour
    pointsLeft.append(pointsLeft[0])
    pointsRight.append(pointsRight[0])

    # ------------------------FOR LEFT SIDE----------------------------------

    # Convert the points to x and y arrays
    x, y = zip(*pointsLeft)
    # Create the initial contour
    init1 = np.array([x, y]).T

    # Use spline interpolation to create a smooth curve from the points
    tck, u = splprep([x, y], s=0)
    startPointsLeft = np.linspace(0, 1, 400)
    curved_init = splev(startPointsLeft, tck)
    init1 = np.array(curved_init).T
    a = init1
    # Use the Kass snake algorithm to segment the image
    snakeContourLeft = helper.kassSnake(image2, init1, wLine=0, wEdge=1.0, alpha=0.1, beta=0.1, gamma=0.001,
                                     maxIterations=5, maxPixelMove=None, convergence=0.1)

    # Storing Control points in the List
    contour_pointsLeft = []
    for i in range(1, 7):
        contour_pointsLeft.append((snakeContourLeft[66 * (i)][0], snakeContourLeft[66 * (i)][1]))


    # ------------------------FOR RIGHT SIDE----------------------------------

        # Convert the points to x and y arrays
        x, y = zip(*pointsRight)
        # Create the initial contour
        init2 = np.array([x, y]).T

        # Use spline interpolation to create a smooth curve from the points
        tck, u = splprep([x, y], s=0)
        startPointsRight = np.linspace(0, 1, 400)
        curved_init = splev(startPointsRight, tck)
        init2 = np.array(curved_init).T
        a = init2
        # Use the Kass snake algorithm to segment the image
        snakeContourRight = helper.kassSnake(image2, init2, wLine=0, wEdge=1.0, alpha=0.1, beta=0.1, gamma=0.001,
                                            maxIterations=5, maxPixelMove=None, convergence=0.1)

        # Storing Control points in the List
        contour_pointsRight = []
        for i in range(1, 7):
            contour_pointsRight.append((snakeContourRight[66 * (i)][0], snakeContourRight[66 * (i)][1]))


    # -----------Display the original image and the segmented contours----------------------------------------
    plt.figure()
    plt.imshow(image2, cmap='gray')
    plt.plot(init1[:, 0], init1[:, 1], '--r', lw=2)
    plt.plot(snakeContourLeft[:, 0], snakeContourLeft[:, 1], '-b', lw=2)

    plt.plot(init2[:, 0], init2[:, 1], '--r', lw=2)
    plt.plot(snakeContourRight[:, 0], snakeContourRight[:, 1], '-b', lw=2)
    plt.savefig(output_pth)

    return (contour_pointsLeft+contour_pointsRight);