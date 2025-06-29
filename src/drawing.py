from PIL import Image, ImageDraw, ImageFont
from src.config import COLOR_BACKGROUND

def draw_code_on_image(all_code_parts, width, height, output_filename):
    img = Image.new('RGB', (width, height), color = COLOR_BACKGROUND)
    d = ImageDraw.Draw(img)

    x_offset = 10
    y_offset = 10

    avg_chars_per_statement = 50
    estimated_total_chars = len(all_code_parts) * avg_chars_per_statement
    estimated_lines = estimated_total_chars / (width / 8)
    font_size = int(height / (estimated_lines + 2))
    min_font_size = 10
    max_font_size = 24
    font_size = max(min_font_size, min(font_size, max_font_size))

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        font_size = 12

    line_height = font_size + 3

    current_x = x_offset
    current_y = y_offset
    for statement_parts in all_code_parts:
        for part, color in statement_parts:
            text_to_draw = part + " "
            text_width = d.textlength(text_to_draw, font=font)
            
            if current_x + text_width > width - x_offset:
                current_x = x_offset
                current_y += line_height
                if current_y > height - line_height:
                    break
            
            d.text((current_x, current_y), text_to_draw, font=font, fill=color)
            current_x += text_width
        
        if current_y > height - line_height:
            break

    img.save(output_filename)
    return output_filename
