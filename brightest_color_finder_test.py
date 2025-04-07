import math

def create_color(hex_code):
    # Turn hex code into a color dictionary
    hex_clean = hex_code.lstrip('#')
    if len(hex_clean) != 6:
        raise ValueError("Invalid color code")

    try:
        r = int(hex_clean[0:2], 16)
        g = int(hex_clean[2:4], 16)
        b = int(hex_clean[4:6], 16)
    except ValueError:
        raise ValueError("Invalid color code")

    return {
        'hex': f"#{hex_clean.upper()}",
        'r': r,
        'g': g,
        'b': b
    }

def calculate_brightness(color):
    # Use formula to get brightness
    return math.sqrt(0.241 * color['r']**2 + 0.691 * color['g']**2 + 0.068 * color['b']**2)

def analyze_colors(hex_list):
    # Check all colors and find the brightest one
    valid_colors = []

    for hex_code in hex_list:
        try:
            color = create_color(hex_code)
            valid_colors.append(color)
            print(f"{color['hex']} added")
        except ValueError:
            print(f"{hex_code} is invalid - skipped")

    if not valid_colors:
        print("No valid colors found!")
        return None

    brightest = max(valid_colors, key=calculate_brightness)
