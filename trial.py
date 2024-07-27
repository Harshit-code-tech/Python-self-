from PIL import Image, ImageDraw, ImageFont

# Load the original image
img = Image.open("D:\\python\\pythonProject\\fallback_premium.png")
draw = ImageDraw.Draw(img)

# Define the text properties
oops_text = "Oops!"
fallback_text = "Something went wrong. Please try again later."
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size_oops = 150
font_size_fallback = 50

# Load the fonts with exception handling
try:
    font_oops = ImageFont.truetype(font_path, font_size_oops)
    font_fallback = ImageFont.truetype(font_path, font_size_fallback)
except OSError:
    font_oops = ImageFont.load_default()
    font_fallback = ImageFont.load_default()

# Define the text positions
oops_position = (img.width // 2, img.height // 4)
fallback_position = (img.width // 2, img.height // 2)

# Calculate text size to center it
oops_text_size = draw.textbbox((0, 0), oops_text, font=font_oops)
fallback_text_size = draw.textbbox((0, 0), fallback_text, font=font_fallback)

# Center the text
oops_position = (oops_position[0] - (oops_text_size[2] - oops_text_size[0]) // 2, oops_position[1] - (oops_text_size[3] - oops_text_size[1]) // 2)
fallback_position = (fallback_position[0] - (fallback_text_size[2] - fallback_text_size[0]) // 2, fallback_position[1] - (fallback_text_size[3] - fallback_text_size[1]) // 2)

# Draw the text on the image
draw.text(oops_position, oops_text, font=font_oops, fill="white")
draw.text(fallback_position, fallback_text, font=font_fallback, fill="white")

# Save the edited image
premium_image_path = "D:\\python\\pythonProject\\fallback_premium_oops.png"
img.save(premium_image_path)
premium_image_path