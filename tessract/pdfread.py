import pytesseract
from pdf2image import convert_from_path


file_path = './file/Wealth-Maxima-V3-Brochure-Web_Hindi.pdf'
pages = convert_from_path(file_path)

# Initialize an empty string to store extracted text
extracted_text = ''

# Loop through each page image and extract text using Tesseract OCR
for page in pages:
    # Extract text from the current page image
    page_text = pytesseract.image_to_string(page, lang='hin')
    
    # Append the extracted text to the overall text
    extracted_text += page_text + '\n'  # Add a newline character to separate text from different pages

# Print the extracted text
print(extracted_text)