import math
import requests
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from functools import lru_cache


@dataclass(frozen=True)
class Color:
    """This class represents a color using a hex code and its RGB values."""
    hex_code: str
    r: int
    g: int
    b: int

    @classmethod
    def from_hex(cls, hex_code: str) -> 'Color':
        """Creates a Color object from a hex string like '#FFAA33'."""
        hex_clean = hex_code.lstrip('#').upper()
        if len(hex_clean) != 6:
            raise ValueError(f"Hex code must be 6 characters long: {hex_code}")
        
        try:
            components = [int(hex_clean[i:i+2], 16) for i in range(0, 6, 2)]
        except ValueError:
            raise ValueError(f"Invalid hex characters in: {hex_code}")
            
        return cls(
            hex_code=f"#{hex_clean}",
            r=components[0],
            g=components[1],
            b=components[2]
        )

    @property
    def brightness(self) -> float:
        """Calculates how bright the color is using a formula."""
        return math.sqrt(0.241 * self.r**2 + 0.691 * self.g**2 + 0.068 * self.b**2)

    def __str__(self) -> str:
        return f"{self.hex_code} (R={self.r}, G={self.g}, B={self.b})"


class ColorNameService:
    """This class gets color names from an online API and saves them for reuse."""
    
    API_URL = "https://csscolorsapi.com/api/colors"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._color_map = cls._fetch_color_map()
        return cls._instance

    @classmethod
    def _fetch_color_map(cls) -> Dict[str, str]:
        """Gets color names from the internet and stores them in a dictionary."""
        try:
            response = requests.get(cls.API_URL, timeout=5)
            response.raise_for_status()
            return {
                color["hex"].lstrip('#').upper(): color["name"]["value"]
                for color in response.json()
                if "hex" in color and "name" in color
            }
        except Exception as e:
            print(f"Could not fetch color names: {str(e)}")
            return {}

    @lru_cache(maxsize=256)
    def get_name(self, hex_code: str) -> str:
        """Returns the name of a color using its hex code."""
        return self._color_map.get(hex_code.lstrip('#').upper(), "Unknown")


def analyze_colors(hex_codes: List[str]) -> Tuple[Color, List[Color]]:
    """Takes a list of color codes and returns the brightest color."""
    if not hex_codes:
        raise ValueError("No color codes given.")

    colors = []
    for code in hex_codes:
        try:
            colors.append(Color.from_hex(code))
        except ValueError as e:
            print(f"Skipping invalid color '{code}': {e}")

    if not colors:
        raise ValueError("No valid colors found.")

    brightest = max(colors, key=lambda c: c.brightness)
    return brightest, colors


def run_tests() -> None:
    """Runs several tests to check if everything works correctly."""
    print("\nRunning Test Suite...\n")
    test_results = []

    try:
        color = Color.from_hex("#A1B2C3")
        assert (color.r, color.g, color.b) == (0xA1, 0xB2, 0xC3)
        test_results.append(("Color Parsing", "Passed"))
    except Exception as e:
        test_results.append(("Color Parsing", f"Failed: {str(e)}"))

    try:
        test_cases = [
            ("#000000", 0.0),
            ("#FFFFFF", 255.0),
            ("#FF0000", math.sqrt(0.241 * 255 ** 2)),
            ("#00FF00", math.sqrt(0.691 * 255 ** 2)),
        ]
        for hex_code, expected in test_cases:
            actual = Color.from_hex(hex_code).brightness
            assert math.isclose(actual, expected, rel_tol=0.01), \
                f"{hex_code} expected {expected}, got {actual:.2f}"
        test_results.append(("Brightness Calculation", "Passed"))
    except Exception as e:
        test_results.append(("Brightness Calculation", f"Failed: {str(e)}"))

    try:
        test_colors = ["#AABBCC", "#000000", "#FFFFFF", "invalid", "#123456"]
        brightest, _ = analyze_colors(test_colors)
        assert brightest.hex_code == "#FFFFFF"
        test_results.append(("Full Workflow", "Passed"))
    except Exception as e:
        test_results.append(("Full Workflow", f"Failed: {str(e)}"))

    max_len = max(len(name) for name, _ in test_results)
    print("Test Results:")
    for name, result in test_results:
        print(f"  {name.ljust(max_len)} : {result}")

    if all("Passed" in result for _, result in test_results):
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed.")


if __name__ == "__main__":
    sample_colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]

    try:
        brightest, valid_colors = analyze_colors(sample_colors)
        name_service = ColorNameService()

        print("\nColor Analysis Results:")
        print(f"Total colors provided  : {len(sample_colors)}")
        print(f"Valid colors parsed     : {len(valid_colors)}")
        print(f"Brightest color         : {brightest}")
        print(f"Color name              : {name_service.get_name(brightest.hex_code)}")
        print(f"Brightness value        : {brightest.brightness:.2f}")

    except ValueError as e:
        print(f"\nError: {str(e)}")

    run_tests()
