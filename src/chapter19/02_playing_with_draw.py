#! /usr/bin/env python3
# Playing with Pillow Image Library (ImageDraw module)

from PIL import Image, ImageDraw, ImageFont

print("Playing with Pillow Image Library (ImageDraw module)")

image = Image.new("RGBA", (200, 200,), "white")
draw = ImageDraw.Draw(image)
draw.line([(0, 0), (199, 0), (199, 199), (0, 199)], fill="black")
draw.rectangle((20, 30, 60, 60), fill="blue")
draw.ellipse((120, 30, 160, 60), fill="red")
draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill="brown")
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill="green")
font = ImageFont.truetype("/usr/share/fonts/truetype/tlwg/Garuda.ttf", 26)
draw.text((40, 120), "Hello World!", fill="purple", font=font)
image.save("images/new/draw.png")
