from PIL import Image
import pytesseract

# Path to Tesseract executable (only needed for Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
#image_path = 'picForTextToImage.jpg'
image_path = input("Enter image path to convert: ")
image = Image.open(image_path)

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(text)