# Technique 1:- flipping the image technique

from PIL import image

# opening the image and it processes in terms of matrices
img = Image.open('flipped_image.jpeg')

# transposing the matrix
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# it takes the matrix that is captured by img object, transposes that matrix and this new matrix is stored in transposed_img object that object captures the new matrix

# now we have got the actual image in the matrix representation that is understandable by computers
# now we need to convert to a form that is understandable by humans and save it to a file

transposed_img.save('corrected.jpeg') # specify the path where you want your output file to be saved, here i am saving in same directory

print('Done Flipping')


# Technique 2:- Image Enhancement technique

# Here we will use adaptive histogram equalization or clahe
# clahe:- contrast limited adaptive histogram equalization

import cv2
# read the image
img = cv2.imread('crime.png')

# preparation for clahe
clahe = cv2.createCLAHE()

# this enhancement technique works well if the images is in the black and white format(gray scale image)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply enhancement
enh_img = clahe.apply(gray_img) # all are in the matrices form

# save it to file for human understandable format
cv2.imwrite('enhanced.png', enh_img) # we can change the format
print('Done Enhancing')
