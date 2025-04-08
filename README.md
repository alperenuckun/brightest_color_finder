# Color Analysis Tool

A Python program that analyzes random colors from a CSS Colors API, calculates their brightness, and identifies the brightest color among them. Includes caching, graceful fallback, and saves analysis results.

---

## Features

- Fetches color data from a public CSS Colors API
- Caches color names locally in `color_cache.json`
- Analyzes **10 random colors by default** (configurable)
- Calculates **brightness using perceptive luminance**
- Saves results to `color_results.json`
- Identifies the **brightest color** in each analysis
- Graceful fallback to cached data when the API is unavailable

---

## 🖼Flowchart

![Flowchart](https://github.com/alperenuckun/brightest_color_finder/blob/main/algorithm_flowchart.svg)

---

## Example Output

```
Selecting 10 random colors...

Analysis Results:
#FAF0E6 - Linen - Brightness: 0.948
#EE82EE - Violet - Brightness: 0.685
#CD853F - Peru - Brightness: 0.575
#6495ED - CornflowerBlue - Brightness: 0.566
#808000 - Olive - Brightness: 0.445
#228B22 - ForestGreen - Brightness: 0.375
#8B4513 - SaddleBrown - Brightness: 0.330
#663399 - RebeccaPurple - Brightness: 0.305
#8B008B - DarkMagenta - Brightness: 0.225
#8B0000 - DarkRed - Brightness: 0.163

Brightest color: Linen (#FAF0E6)
Brightness value: 0.948
Results saved to color_results.json

```

---

### Install dependencies:

```bash
pip install requests
```

### Download the script:

```bash
wget https://raw.githubusercontent.com/alperenuckun/brightest_color_finder/main/brightest_color_finder_final.py

```

---

## Usage

To run the program:

```bash
brightest_color_finder_final.py
```

The program will:

- Load or create the local color cache
- Fetch the latest color list from the API (or use cache)
- Analyze a random set of colors
- Display and save results
- Prompt you to run it again

---

## Files

- `color_analyzer.py`: Main program
- `color_cache.json`: Local color database
- `color_results.json`: Analysis results

---

## Customization

You can modify these in the source code:

- Number of random colors to analyze (default: **10**)
- API endpoint URL
- Filenames for cache and results

---

## Brightness Calculation

Uses the **Perceptive Luminance** formula:

```
brightness = sqrt(0.299 * R^2 + 0.587 * G^2 + 0.114 * B^2) / 255
```

---

