import colorgram

colors = colorgram.extract("image.jpg",6)


allColors = []

for i in range(len(colors)):
    current = colors[i]
    rgb = current.rgb 
    rgbTuple = (rgb.r, rgb.g, rgb.b)
    allColors.append(rgbTuple)
    
print(allColors)
    