import numpy
from PIL import Image
from numpy import asarray


def imageToArray(path) -> numpy.ndarray:
    """
    Converts an image to len(input_array) = num of rows, len(input_array[i]) = num of columns

    (In other words the image is converted up to down, then in the rows left to right)

    [R, G, B, A] format in each instance of input_array[i][i].

    Automatically resizes pictures to 50 x 50

    Parameter
        path (str): The path of the image

    Returns
        numpy.ndarray(): the image in an array format
    """
    image = Image.open(path)
    return asarray(image.resize((50, 50)))


def RGBAtoGreyScaleList(array) -> list:
    """
    Turns RGBA to Grey scale. (Normalized) into one list.

    Parameter:
        array (ndarray): The numpy.ndarray, in the format of nested arrays (array of array of ints)
    """
    greyList = []
    for row in range(len(array)):
        for cell in range(len(array[row])):
            greyList.append(sum(array[row][cell][:3]) / 765)
    return greyList


def arrayToImage(array) -> None:
    """
    Converts a ndarray object into a png file, saves it as a test_result.png

    Parameter
        array (ndarray): The numpy.ndarray that is being converted into an image
    """
    output_image = Image.fromarray(array)
    output_image.save("test_result.png")


def arrayInfo(array) -> str:
    """
    Returns the dimension of the array (image)

    Parameter
        array (ndarray): The numpy.ndarray that is being converted into an image
    """
    return "width: " + str(array.shape[1]) + "\nheight: " + str(array.shape[0])
