import cv2
import numpy as np

x = "hello World"
print(x)

img = cv2.imread("tests/test.png")

type(img)
map_imgdata = map(str, img.shape)
img_data = " , ".join(map_imgdata)

cv2.imshow(img_data, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
