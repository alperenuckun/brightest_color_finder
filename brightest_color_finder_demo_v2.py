import math
import requests
from dataclasses import dataclass
from typing import List, Tuple, Dict
from functools import lru_cache

@dataclass(frozen=True)
class Color:
    """Stores color in hex and RGB format"""
    hex_code: str
    r: int  # Red (0-255)
    g: int  # Green (0-255)
    b: int  # Blue (0-255)

    @classmethod
    def from_hex(cls, hex_code: str) -> 'Color':
        """Create Color from hex string (#RRGGBB)"""
        hex_clean = hex_code.lstrip('#')
        if len(hex_clean) != 6:
            raise ValueError(f"Invalid length: {hex_code}")
        
        try:
            # Convert hex to RGB integers
            r = int(hex_clean[0:2], 16)
            g = int(hex_clean[2:4], 16)
            b = int(hex_clean[4:6], 16)
        except ValueError:
            raise ValueError(f"Invalid hex code: {hex_code}")
            
        return cls(f"#{hex_clean.upper()}", r, g, b)

    @property
    def brightness(self) -> float:
        """Calculate perceived brightness"""
        return math.sqrt(0.241*self.r**2 + 0.691*self.g**2 + 0.068*self.b**2)

    def __str__(self) -> str:
        return f"{self.hex_code} (R:{self.r}, G:{self.g}, B:{self.b})"

class ColorNameService:
    """API service for color names"""
    _instance = None
    API_URL = "https://csscolorsapi.com/api/colors"

    def __new__(cls):
        # Singleton pattern
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._load_colors()
        return cls._instance

    def _load_colors(self):
        """Load color names from API"""
        try:
            response = requests.get(self.API_URL, timeout=3)
            response.raise_for_status()
            self._color_map = {
                c["hex"].lstrip('#').upper(): c["name"]["value"] 
                for c in response.json() 
                if "hex" in c and "name" in c
            }
        except Exception as e:
            print(f"API error: {e}")
            self._color_map = {}

    @lru_cache(maxsize=256)
    def get_name(self, hex_code: str) -> str:
        """Get color name for hex code"""
        return self._color_map.get(hex_code.lstrip('#').upper(), "Unknown")

def analyze_colors(hex_codes: List[str]) -> Tuple[Color, List[Color]]:
    """Find brightest color from list"""
    if not hex_codes:
        raise ValueError("Empty color list")

    colors = []
    for code in hex_codes:
        try:
            colors.append(Color.from_hex(code))
        except ValueError as e:
            print(f"Skipping: {code} - {e}")

    if not colors:
        raise ValueError("No valid colors found")

    # Return brightest color and all valid colors
    return max(colors, key=lambda c: c.brightness), colors

def test_system():
    """Run basic test cases"""
    test_data = [
        ("#FF0000", "#00FF00", "#0000FF"),  # Red, Green, Blue
        ("#000000", "#FFFFFF", "#123456"),   # Black, White, Gray
        ("invalid", "#AABBCC", "#112233")    # Invalid code
    ]
    
    for i, colors in enumerate(test_data, 1):
        print(f"\nTest {i}: {colors}")
        try:
            brightest, valid = analyze_colors(list(colors))
            name = ColorNameService().get_name(brightest.hex_code)
            print(f"Result: {brightest} - Brightness: {brightest.brightness:.2f}")
            print(f"Color Name: {name}")
            print(f"Valid Colors: {len(valid)}/{len(colors)}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("=== Color Analysis System ===")
    test_system()
    
    # Example usage
    sample = ["#FF5733", "#33FF57", "#3357FF", "INVALID", "#123ABC"]
    print("\nExample Run:")
    try:
        brightest, valid = analyze_colors(sample)
        name = ColorNameService().get_name(brightest.hex_code)
        print(f"Brightest: {brightest}")
        print(f"Name: {name}")
        print(f"Brightness: {brightest.brightness:.2f}")
        print(f"Success Rate: {len(valid)}/{len(sample)}")
    except ValueError as e:
        print(f"System error: {e}")