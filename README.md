
# Brightest Color Finder

This project finds the **brightest color** from a list of hex color codes.  
It also gives you the name of that color using an online API.

---

## What It Does

- Takes a list of hex color codes (like #FFAA33).
- Converts them into RGB values.
- Calculates how bright each color is.
- Finds the one with the highest brightness
- Gets the name of the color using an online color name API.

---

## How the Algorithm Works

1. It removes the `#` from each hex code.
2. Converts the hex code to red, green, and blue values (R, G, B).
3. Uses this formula to calculate brightness:

   ```
   √(0.241 * R² + 0.691 * G² + 0.068 * B²)
   ```

4. Compares all brightness values and picks the brightest color.
5. It then asks an API: “What’s the name of this color?”

---

## Algorithm Flowchart

<img src="https://raw.githubusercontent.com/alperenuckun/brightest_color_finder/main/algorithm_flowchart.svg" width="800"/> 

---

## ▶How to Use

1. Clone the project:
   ```bash
   git clone https://github.com/alperenuckun/brightest_color_finder.git
   cd brightest_color_finder.
   ```

2. Run the Python file:
   ```bash
   python brightest_color_finder.py
   ```

---

## Example Output

```
Color Analysis Results:
Total colors provided  : 5
Valid colors parsed     : 5
Brightest color         : #FFFFFF (R=255, G=255, B=255)
Color name              : Unknown
Brightness value        : 255.00

Running Test Suite...

Skipping invalid color 'invalid': Hex code must be 6 characters long: invalid
Test Results:
Color Parsing          : Passed
Brightness Calculation : Passed
Full Workflow          : Passed

All tests passed!
```

---

## Color Name API

We use this API to get color names:  
🔗 https://csscolorsapi.com/

---

