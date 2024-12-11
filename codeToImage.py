# This code translate your code to image.
# pip install pytoimage
from pytoimage import PyImage
code = PyImage('twitterPostAutomationScript.py', background=(255,255,255))
palette = {'line': (255, 0, 255), 'normal': (0,0,0),}
code.set_color_palette(palette=palette)
code.generate_image()
code.show_image()
code.save_image('codeToImage.png')