from PIL import Image, ImageDraw, ImageFont

# make a blank image for the text, initialized to transparent text color
tmp = Image.new('RGB', (500,500), (255,255,255,0))

# get a font
#fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(tmp)

d.line(((0,0),(500,500)), fill='black')
# draw text, half opacity
#d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
#d.text((10,60), "World", font=fnt, fill=(255,255,255,255))


tmp.show()
