import math
import random
import requests
import json
import os
from datetime import datetime

# Simple class to store color data
class Color:
    def __init__(self, hex_code):
        # Standardize hex format (e.g., ABC -> AABBCC)
        self.hex_code = hex_code.upper().lstrip("#")
        if len(self.hex_code) == 3:
            self.hex_code = "".join([c*2 for c in self.hex_code])
        
        # Convert HEX to RGB
        self.r = int(self.hex_code[0:2], 16)
        self.g = int(self.hex_code[2:4], 16)
        self.b = int(self.hex_code[4:6], 16)
        
        # Calculate brightness (0-1 scale)
        self.brightness = (0.299*self.r + 0.587*self.g + 0.114*self.b)/255

# Main analyzer class
class ColorAnalyzer:
    def __init__(self):
        self.cache_file = "color_cache.json"
        self.result_file = "color_results.json"
        self.color_cache = self.load_cache()
        
        # Get colors from API
        self.api_colors = self.get_colors_from_api()
        self.update_cache()

    def load_cache(self):
        # Load existing color cache
        if os.path.exists(self.cache_file):
            with open(self.cache_file, "r") as f:
                return json.load(f)
        return {}

    def save_cache(self):
        # Save cache to file
        with open(self.cache_file, "w") as f:
            json.dump(self.color_cache, f, indent=2)

    def get_colors_from_api(self):
        # Fetch colors from API
        try:
            response = requests.get("https://www.csscolorsapi.com/api/colors", timeout=5)
            return response.json().get("colors", [])
        except:
            print("Failed to get colors from API")
            return []

    def update_cache(self):
        # Add new colors to cache
        for color in self.api_colors:
            hex_code = color["hex"].upper().lstrip("#")
            if hex_code not in self.color_cache:
                self.color_cache[hex_code] = color["name"]
        self.save_cache()

    def get_random_colors(self, count=10):
        # Pick random colors from cache
        if not self.color_cache:
            return [Color("FFFFFF"), Color("000000")]  # Default colors
        
        hex_codes = random.sample(list(self.color_cache.keys()), min(count, len(self.color_cache)))
        return [Color(hex_code) for hex_code in hex_codes]

    def analyze_colors(self, colors):
        # Prepare analysis results
        results = []
        for color in colors:
            results.append({
                "hex": f"#{color.hex_code}",
                "rgb": (color.r, color.g, color.b),
                "brightness": round(color.brightness, 3),
                "name": self.color_cache.get(color.hex_code, "Unknown")
            })
        return results

    def save_results(self, results):
        # Save results to JSON file
        data = {
            "total_colors": len(self.color_cache),
            "analysis_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "colors": results,
            "brightest": max(results, key=lambda x: x["brightness"])
        }
        
        with open(self.result_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Results saved to {self.result_file}")

# Main program
def main():
    print("Color Analysis Program")
    print("=====================")
    
    analyzer = ColorAnalyzer()
    
    while True:
        print("\nSelecting 10 random colors...")
        colors = analyzer.get_random_colors(10)
        results = analyzer.analyze_colors(colors)
        
        # Show results
        print("\nAnalysis Results:")
        for color in sorted(results, key=lambda x: -x["brightness"]):
            print(f"{color['hex']} - {color['name']} - Brightness: {color['brightness']:.3f}")
        
        # Show brightest color
        brightest = max(results, key=lambda x: x["brightness"])
        print(f"\nBrightest color: {brightest['name']} ({brightest['hex']})")
        print(f"Brightness value: {brightest['brightness']:.3f}")
        
        analyzer.save_results(results)
        
        if input("\nAnalyze again? (y/n): ").lower() != 'y':
            print(f"\nTotal colors in database: {len(analyzer.color_cache)}")
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()