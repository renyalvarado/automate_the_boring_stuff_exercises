#! /usr/bin/env python3
# Playing with Pillow Image Library
from PIL import Image

bruno = Image.open("images/original/bruno.jpeg")
bruno.save("images/new/bruno.png")

img_red = Image.new("RGBA", (300, 400), "red")
img_red.save("images/new/img_red.png")
bruno_crop = bruno.crop((260, 420, 670, 832))
bruno_crop.save("images/new/bruno_crop.png")

bruno_faces = Image.new("RGBA", (1640, 1648), "red")
for x_y in [(i * 410, j * 412,) for i in range(4) for j in range(4)]:
    bruno_faces.paste(bruno_crop, x_y)

bruno_faces.save("images/new/bruno_faces.png")
bf_width, bf_height = bruno_faces.size
small_faces = bruno_faces.resize((bf_width // 2, bf_height // 2))
small_faces.save("images/new/bruno_small_faces.png")

bruno_mosaic = Image.new("RGBA", (1234, 1234), "black")
bruno_mosaic.paste(bruno_crop, (412, 822))
bruno_mosaic.paste(bruno_crop.rotate(90), (822, 412))
bruno_mosaic.paste(bruno_crop.rotate(180), (412, 0))
bruno_mosaic.paste(bruno_crop.rotate(270), (0, 412))

bruno_mosaic.save("images/new/bruno_mosaic.png")

logo = Image.open("images/original/logo.png")
bruno_with_logo = bruno.copy()
bruno_with_logo.paste(logo, (300, 300,), logo)
bruno_with_logo.save("images/new/bruno_with_logo.png")
