from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create an image with a gradient background
width, height = 1000, 300
image = Image.new("RGB", (width, height))
for y in range(height):
    for x in range(width):
        r = int(34 + (255 - 34) * (x / width))
        g = int(45 + (255 - 45) * (y / height))
        b = int(65 + (255 - 65) * (x / width))
        image.putpixel((x, y), (r, g, b))

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 50)
except IOError:
    font = ImageFont.load_default()

# Create a drawing context
draw = ImageDraw.Draw(image)

# Add a premium style text
text_lines = ["OOPS!", "Something went wrong. Please try again."]

# Calculate the total height of the text block
total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line in text_lines)
current_y = (height - total_text_height) / 2

# Draw each line of text with shadow
for line in text_lines:
    bbox = draw.textbbox((0, 0), line, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) / 2
    # Draw shadow
    draw.text((text_x + 2, current_y + 2), line, font=font, fill=(0, 0, 0))
    # Draw text
    draw.text((text_x, current_y), line, font=font, fill=(255, 215, 0))
    current_y += bbox[3] - bbox[1]

# Save the image
file_path = 'D:\\python\\pythonProject\\fallback.png'
image.save(file_path)
file_path