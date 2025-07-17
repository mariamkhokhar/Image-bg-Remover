!pip install rembg   # Here we are installing remove background library
!pip install onnxruntime
from rembg import remove
from PIL import Image   # PIL is Python Image Library
import io

input_img = Image.open("IMG_3453.jpg")

# Removing Bacground
output_img = remove(input_img)

#Save Image
output_img.save("cat_remove.png")

#Show Image
output_img.show()



