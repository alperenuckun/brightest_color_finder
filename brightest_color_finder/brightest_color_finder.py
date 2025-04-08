import math
import requests

class Color:
    def __init__(self, hex_code):
        self.hex_code = hex_code.upper().lstrip("#")
        self.r, self.g, self.b = self.hex_to_rgb()

    def hex_to_rgb(self):
        if len(self.hex_code) != 6:
            raise ValueError("Hex code must be 6 characters long")
        return tuple(int(self.hex_code[i:i+2], 16) for i in (0, 2, 4))

    def brightness(self):
        return math.sqrt(0.241 * self.r**2 + 0.691 * self.g**2 + 0.068 * self.b**2)

    def get_name(self):
        basic_colors = {
            "FFFFFF": "White",
            "000000": "Black",
            "FF0000": "Red",
            "00FF00": "Green",
            "0000FF": "Blue",
            "AABBCC": "Pale Blue",
            "154331": "Dark Green",
            "A0B1C2": "Grayish Blue"
        }
        
        if self.hex_code in basic_colors:
            return basic_colors[self.hex_code]

        try:
            response = requests.get(f"https://www.csscolorsapi.com/api/colors/{self.hex_code}", timeout=3)
            if response.status_code == 200:
                return response.json().get("name", "Unknown")
        except Exception:
            pass
        
        return "Unknown"

class BrightestColorFinder:
    def __init__(self, color_list):
        self.colors = [Color(hex_code) for hex_code in color_list]

    def find_brightest(self):
        if not self.colors:
            return "No colors provided"
        
        brightest = max(self.colors, key=lambda c: c.brightness())
        name = brightest.get_name()
        return (f"The brightest color is: #{brightest.hex_code} "
                f"(r={brightest.r}, g={brightest.g}, b={brightest.b}), "
                f"called {name}")