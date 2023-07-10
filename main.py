import cv2

# configurable parameters
inputImageName = "peakpx.jpg"
outputImageName = "newpeak.jpg"
scaleBy = 50

# read image
src = cv2.imread(inputImageName, cv2.IMREAD_UNCHANGED)

# set new width and height
newWidth = int(src.shape[1] * scaleBy / 100)
newHeight = int(src.shape[0] * scaleBy / 100)

# resize image
output = cv2.resize(src, (newWidth, newHeight))

cv2.imwrite(outputImageName, output)
