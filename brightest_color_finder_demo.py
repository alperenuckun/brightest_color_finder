import math
from typing import List, Tuple

class BasicColor:
    def __init__(self, hex_code: str):
        self.hex_code = hex_code
        try:
            self.r = int(hex_code[1:3], 16)
            self.g = int(hex_code[3:5], 16)
            self.b = int(hex_code[5:7], 16)
        except:
            raise ValueError(f"Invalid hex color: {hex_code}")

    def brightness(self) -> float:
        return math.sqrt(0.241*self.r**2 + 0.691*self.g**2 + 0.068*self.b**2)

def find_brightest_basic(hex_codes: List[str]) -> Tuple[BasicColor, List[BasicColor]]:
    colors = []
    for code in hex_codes:
        try:
            colors.append(BasicColor(code))
        except ValueError:
            print(f"Skipping invalid color: {code}")
            continue
    
    if not colors:
        raise ValueError("No valid colors provided")
    
    brightest = max(colors, key=lambda c: c.brightness())
    return brightest, colors

def main():
    colors = ["#FF5733", "#33FF57", "#3357FF", "invalid", "#123ABC"]
    
    try:
        brightest, valid_colors = find_brightest_basic(colors)
        print(f"Analyzed {len(valid_colors)}/{len(colors)} colors")
        print(f"Brightest: {brightest.hex_code}")
        print(f"RGB: ({brightest.r}, {brightest.g}, {brightest.b})")
        print(f"Brightness: {brightest.brightness():.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()