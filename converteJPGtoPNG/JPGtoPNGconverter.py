
import sys
import os
from PIL import Image

image_folder = sys.argv[1]  #Pokedex
output_folder = sys.argv[2] #new

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    #remove .jpg
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All Done!')

# run in the terminal: python JPGtoPNGconverter.py Pokedex\ new\