import random
from PIL import Image, ImageDraw, ImageFont
import argparse

def generate_fake_code(num_statements=200, width=1920, height=1080):
    """Generates a wall of fake code resembling C-like languages and saves it as an image."""
    
    keywords = ["public", "private", "class", "static", "void", "int", "string", "bool", "float", "if", "else", "for", "while", "return", "try", "catch", "new"]
    operators = ["=", "==", "!=", "<", ">", "<=", ">=", "+", "-", "*", "/", "%", "++", "--"]
    data_types = ["int", "string", "bool", "float", "List<int>", "Map<string, string>"]
    functions = ["print", "calculate", "getData", "process", "isValid", "save", "load", "render"]
    variables = ["data", "result", "count", "value", "item", "index", "temp", "config", "user", "product"]

    # Define colors for image (more varied, yet subtle)
    COLOR_BACKGROUND = (25, 25, 25)   # Dark background
    COLOR_KEYWORD = (255, 100, 100)   # Soft Red
    COLOR_DATATYPE = (100, 200, 255)  # Light Blue
    COLOR_FUNCTION = (150, 255, 150)  # Light Green
    COLOR_VARIABLE = (220, 220, 220)  # Off-White
    COLOR_STRING = (255, 255, 100)    # Pale Yellow
    COLOR_NUMBER = (200, 150, 255)    # Lavender
    COLOR_OPERATOR = (255, 180, 100)  # Light Orange
    COLOR_COMMENT = (120, 120, 120)   # Medium Gray

    # Create a blank image with a dark background
    img = Image.new('RGB', (width, height), color = COLOR_BACKGROUND)
    d = ImageDraw.Draw(img)

    try:
        # Try to load a common monospace font, or fallback to default
        font = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        font = ImageFont.load_default()

    x_offset = 10
    y_offset = 10
    line_height = 15 # Approximate line height for the font size

    def get_text_color(text, statement_type=None):
        if text in keywords:
            return COLOR_KEYWORD
        elif text in data_types:
            return COLOR_DATATYPE
        elif text in functions:
            return COLOR_FUNCTION
        elif text.startswith('"') and text.endswith('"'):
            return COLOR_STRING
        elif text.isdigit() or ('.' in text and text.replace('.', '').isdigit()):
            return COLOR_NUMBER
        elif text in operators:
            return COLOR_OPERATOR
        elif text in ["true", "false", "null"]:
            return COLOR_KEYWORD
        elif text.startswith("/*") and text.endswith("*/"):
            return COLOR_COMMENT
        else:
            return COLOR_VARIABLE

    def generate_inner_statements(min_statements=2, max_statements=7):
        inner_code_parts = []
        num_inner = random.randint(min_statements, max_statements)
        for _ in range(num_inner):
            inner_statement_type = random.choice(["declaration", "assignment", "function_call", "return_statement"])
            if inner_statement_type == "declaration":
                var_type = random.choice(data_types)
                var_name = random.choice(variables) + str(random.randint(0,9))
                value = ""
                if var_type == "int":
                    value = str(random.randint(0, 100))
                elif var_type == "string":
                    value = f'"{random.choice(["hello", "world", "test"])}"'
                elif var_type == "bool":
                    value = random.choice(["true", "false"])
                elif var_type == "float":
                    value = f"{random.uniform(0.0, 100.0):.2f}"
                inner_code_parts.append((var_type, COLOR_DATATYPE))
                inner_code_parts.append((var_name, COLOR_VARIABLE))
                inner_code_parts.append(("=", COLOR_OPERATOR))
                inner_code_parts.append((value, get_text_color(value)))
                inner_code_parts.append((";", COLOR_VARIABLE))
            elif inner_statement_type == "assignment":
                var_name = random.choice(variables) + str(random.randint(0,9))
                value = random.choice([str(random.randint(0, 100)), f'"{random.choice(["hello", "world", "test"])}"', "true", "false", "null"])
                inner_code_parts.append((var_name, COLOR_VARIABLE))
                inner_code_parts.append(("=", COLOR_OPERATOR))
                inner_code_parts.append((value, get_text_color(value)))
                inner_code_parts.append((";", COLOR_VARIABLE))
            elif inner_statement_type == "function_call":
                func_name = random.choice(functions)
                arg1 = random.choice(variables + [str(random.randint(0, 10))])
                arg2 = random.choice(variables + [str(random.randint(0, 10))])
                inner_code_parts.append((func_name, COLOR_FUNCTION))
                inner_code_parts.append(("(", COLOR_VARIABLE))
                inner_code_parts.append((arg1, COLOR_VARIABLE))
                inner_code_parts.append((",", COLOR_VARIABLE))
                inner_code_parts.append((arg2, COLOR_VARIABLE))
                inner_code_parts.append((")", COLOR_VARIABLE))
                inner_code_parts.append((";", COLOR_VARIABLE))
            elif inner_statement_type == "return_statement":
                return_val = random.choice(variables + [str(random.randint(0, 100)), f'"{random.choice(["success", "failure"])}"', "true", "false", "null"])
                inner_code_parts.append(("return", COLOR_KEYWORD))
                inner_code_parts.append((return_val, get_text_color(return_val)))
                inner_code_parts.append((";", COLOR_VARIABLE))
        return inner_code_parts

    all_code_parts = []
    for _ in range(num_statements):
        statement_type = random.choice(["declaration", "assignment", "function_call", "method_definition", "class_definition", "conditional", "loop"])
        
        current_statement_parts = []
        if statement_type == "declaration":
            var_type = random.choice(data_types)
            var_name = random.choice(variables) + str(random.randint(0,9))
            value = ""
            if var_type == "int":
                value = str(random.randint(0, 100))
            elif var_type == "string":
                value = f'"{random.choice(["hello", "world", "test"])}"'
            elif var_type == "bool":
                value = random.choice(["true", "false"])
            elif var_type == "float":
                value = f"{random.uniform(0.0, 100.0):.2f}"
            current_statement_parts.append((var_type, COLOR_DATATYPE))
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append((value, get_text_color(value)))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "assignment":
            var_name = random.choice(variables) + str(random.randint(0,9))
            value = random.choice([str(random.randint(0, 100)), f'"{random.choice(["hello", "world", "test"])}"', "true", "false", "null"])
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append((value, get_text_color(value)))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "function_call":
            func_name = random.choice(functions)
            arg1 = random.choice(variables + [str(random.randint(0, 10))])
            arg2 = random.choice(variables + [str(random.randint(0, 10))])
            current_statement_parts.append((func_name, COLOR_FUNCTION))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((arg1, COLOR_VARIABLE))
            current_statement_parts.append((",", COLOR_VARIABLE))
            current_statement_parts.append((arg2, COLOR_VARIABLE))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "method_definition":
            return_type = random.choice(["void", "int", "string", "bool"])
            func_name = random.choice(functions) + "".join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(3, 6)))
            param1_type = random.choice(data_types)
            param1_name = random.choice(variables)
            param2_type = random.choice(data_types)
            param2_name = random.choice(variables)
            current_statement_parts.append((return_type, COLOR_DATATYPE))
            current_statement_parts.append((func_name, COLOR_FUNCTION))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((param1_type, COLOR_DATATYPE))
            current_statement_parts.append((param1_name, COLOR_VARIABLE))
            current_statement_parts.append((",", COLOR_VARIABLE))
            current_statement_parts.append((param2_type, COLOR_DATATYPE))
            current_statement_parts.append((param2_name, COLOR_VARIABLE))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(3, 8))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "class_definition":
            class_name = "".join(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)) + "".join(random.sample("abcdefghijklmnopqrstuvwxyz", random.randint(4, 8)))
            current_statement_parts.append(("class", COLOR_KEYWORD))
            current_statement_parts.append((class_name, COLOR_DATATYPE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(5, 10))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "conditional":
            var_name = random.choice(variables) + str(random.randint(0,9))
            op = random.choice(operators)
            val = random.randint(0, 100)
            current_statement_parts.append(("if", COLOR_KEYWORD))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append((var_name, COLOR_VARIABLE))
            current_statement_parts.append((op, COLOR_OPERATOR))
            current_statement_parts.append((str(val), COLOR_NUMBER))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(2, 6))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        elif statement_type == "loop":
            var_name = random.choice(variables) + str(random.randint(0,9))
            list_name = random.choice(variables) + "List"
            current_statement_parts.append(("for", COLOR_KEYWORD))
            current_statement_parts.append(("(", COLOR_VARIABLE))
            current_statement_parts.append(("int", COLOR_DATATYPE))
            current_statement_parts.append(("i", COLOR_VARIABLE))
            current_statement_parts.append(("=", COLOR_OPERATOR))
            current_statement_parts.append(("0", COLOR_NUMBER))
            current_statement_parts.append((";", COLOR_VARIABLE))
            current_statement_parts.append(("i", COLOR_VARIABLE))
            current_statement_parts.append(("<", COLOR_OPERATOR))
            current_statement_parts.append((list_name, COLOR_VARIABLE))
            current_statement_parts.append((".length", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
            current_statement_parts.append(("i++", COLOR_OPERATOR))
            current_statement_parts.append((")", COLOR_VARIABLE))
            current_statement_parts.append(("{", COLOR_VARIABLE))
            current_statement_parts.extend(generate_inner_statements(2, 6))
            current_statement_parts.append(("}", COLOR_VARIABLE))
            current_statement_parts.append((";", COLOR_VARIABLE))
        
        all_code_parts.append(current_statement_parts)

    # Draw the code onto the image
    current_x = x_offset
    current_y = y_offset
    for statement_parts in all_code_parts:
        for part, color in statement_parts:
            text_to_draw = part + " "
            text_width = d.textlength(text_to_draw, font=font)
            
            if current_x + text_width > width - x_offset: # Check if text goes beyond image width
                current_x = x_offset # Reset x to start of next line
                current_y += line_height # Move to next line
                if current_y > height - line_height: # Check if we are out of vertical space
                    break # Stop drawing if out of space
            
            d.text((current_x, current_y), text_to_draw, font=font, fill=color)
            current_x += text_width
        
        if current_y > height - line_height: # Check after each statement if we are out of vertical space
            break

    output_filename = "fake_code_banner.png"
    img.save(output_filename)
    return output_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a fake code image.")
    parser.add_argument("--width", type=int, default=1920, help="Width of the output image.")
    parser.add_argument("--height", type=int, default=1080, help="Height of the output image.")
    parser.add_argument("--statements", type=int, default=300, help="Number of fake statements to generate.")
    args = parser.parse_args()

    output_file = generate_fake_code(num_statements=args.statements, width=args.width, height=args.height)
    print(f"Generated fake code image: {output_file}")