import argparse
from src.code_generator import generate_code_statements
from src.drawing import draw_code_on_image

def generate_fake_code(num_statements=200, width=1920, height=1080, output_filename="fake_code_banner.png"):
    """Generates a wall of fake code resembling C-like languages and saves it as an image."""
    all_code_parts = generate_code_statements(num_statements)
    output_filename = draw_code_on_image(all_code_parts, width, height, output_filename)
    return output_filename

def main():
    parser = argparse.ArgumentParser(description="Generate a fake code image.")
    parser.add_argument("--width", type=int, default=1920, help="Width of the output image.")
    parser.add_argument("--height", type=int, default=1080, help="Height of the output image.")
    parser.add_argument("--statements", type=int, default=300, help="Number of fake statements to generate.")
    parser.add_argument("--output", type=str, default="fake_code_banner.png", help="Output filename for the image.")
    args = parser.parse_args()

    output_file = generate_fake_code(num_statements=args.statements, width=args.width, height=args.height, output_filename=args.output)
    print(f"Generated fake code image: {output_file}")

if __name__ == "__main__":
    main()
