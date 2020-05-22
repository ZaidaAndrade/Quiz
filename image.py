import PIL
from PIL import Image

img = Image.open("./Resources/create.png")
img = img.resize((20, 20), Image.ANTIALIAS)
img.save("./Resources/create_1.png")

img = Image.open("./Resources/delete.png")
img = img.resize((20, 20), Image.ANTIALIAS)
img.save("./Resources/delete_1.png")

img = Image.open("./Resources/modify.png")
img = img.resize((20, 20), Image.ANTIALIAS)
img.save("./Resources/modify_1.png")

img = Image.open("./Resources/cancel.png")
img = img.resize((15, 15), Image.ANTIALIAS)
img.save("./Resources/cancel_1.png")

img = Image.open("./Resources/create.png")
img = img.resize((15, 15), Image.ANTIALIAS)
img.save("./Resources/create_2.png")



