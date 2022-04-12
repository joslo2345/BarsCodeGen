import barcode
from barcode.writer import ImageWriter
import PIL
from PIL import Image

bar_class = barcode.get_barcode_class('ean13')
barcode = '123456789011'

writer=ImageWriter()
ean13 = bar_class(barcode, writer)

# save the originally generated image
ean13.save('filename')

# open in a PIL Image object
to_be_resized = Image.open('filename.png')

# new size will be 500 by 300 pixels, for example
newSize = (500, 300)

# you can choose other :resample: values to get different quality/speed results
resized = to_be_resized.resize(newSize) 

resized.save('filename_resized.png') # save the resized image

