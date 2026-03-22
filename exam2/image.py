from PIL import Image , ImageFilter 

img = Image.open("image.png")
img.show()

#grey scale 

img_grey = img.convert("L")
img_grey.save("bw_img.png")
img_grey.show()

# rotate 

img_rotate = img.rotate(90)
img_rotate.save("rotated.png")
img_rotate.show()

#blurr

img_blur = img.filter(ImageFilter.BLUR)
img_blur.save("blur.png")
img_blur.show()