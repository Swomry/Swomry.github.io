#160353105
import os
from PIL import ImageDraw
from PIL import Image
from PIL import ImageColor
from collections import Counter

import csv

def imageCreate(size):
    image = Image.new('RGB', (2000*size, 2000*size))
    canvas = ImageDraw.Draw(image)


    with open('C:/Users/Swomr/Desktop/rPlace/rPlaceSmall.csv', 'r') as file:
        reader = csv.reader(file)

        counter = 0
        for line in reader:
            counter += 1
            if line[0] != 'timestamp':

                coordinates = line[3].split(',')
                #add condition for coordinates greater than 3
                if len(coordinates)>2:
                    coordinates[1] = coordinates[0]+coordinates[1]
                    coordinates.pop(0)
                coordinates = ((int(coordinates[0])*size, int(coordinates[1])*size))
                pixel = [coordinates, line[2]]
                if size != 1:
                    try:
                        canvas.rectangle((coordinates[0], coordinates[1], (coordinates[0]+size, coordinates[1]+size)), fill=ImageColor.getrgb(line[2]))
                    except:
                        print(f'{pixel}, {counter}')
                else:
                    try:
                        canvas.rectangle((coordinates[0], coordinates[1], (coordinates[0]*size, coordinates[1]*size)), fill=ImageColor.getrgb(line[2]))
                    except:
                        print(f'{pixel}, {counter}')

    return image
        


result = imageCreate(16)
result = result.save('image.png')
result.show()