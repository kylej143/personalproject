import ImageConverter
import Activation
import NetworkStrategy

image1 = "image/shape1.png"
image2 = "image/shape2.png"

input_array = ImageConverter.imageToArray(image1)
print(ImageConverter.arrayInfo(input_array))

# set the initial neuron size (should be 2500)
nn = NetworkStrategy.Network(2500, 3)

# learn an image
input = ImageConverter.RGBAtoGreyScaleList(input_array)
nn.learn(input, "triangle")

count = 0
right = 0

import os

for filename in os.listdir("image"):
    input_test = ImageConverter.imageToArray("image/" + filename)
    it = ImageConverter.RGBAtoGreyScaleList(input_test)
    right += nn.compare(it, "triangle")
    count += 1

for filename in os.listdir("imageFalse"):
    input_test = ImageConverter.imageToArray("imageFalse/" + filename)
    it = ImageConverter.RGBAtoGreyScaleList(input_test)
    right += nn.compare(it, None)
    count += 1

print(right, count, right/count)


print('end')
