from rembg import remove
from PIL import Image

input_path = "./loh.jpeg"
output_path = "./loh.jpeg"

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open("./loh.jpeg")
