
# 🎨 Color Brightness Analyzer

This project analyzes a list of color hex codes, determines the **brightest color**, and fetches its **CSS color name** via an online API. It also includes a robust testing suite to validate the logic.

---

## 📌 Features

- Parse and validate hex color codes
- Convert to RGB format
- Calculate perceived brightness using the formula:
  ```
  √(0.241 * R² + 0.691 * G² + 0.068 * B²)
  ```
- Identify the brightest color from the list
- Fetch the CSS name of the color from an online API
- Built-in unit tests for:
  - Color parsing
  - Brightness calculation
  - Full analysis workflow

---

## 🧠 Algorithm Flowchart

<img src="https://raw.githubusercontent.com/alperenuckun/brightest_color_finder/main/Algorithm%20Flowchart.svg" width="800"/>>

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/kullaniciAdi/repoAdi.git
   cd repoAdi
   ```

2. Install dependencies (optional, only if you're using a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python color_analyzer.py
   ```

4. Run the tests:
   ```bash
   python color_analyzer.py
   ```

---

## 🧪 Sample Output

```
Color Analysis Results:
Total colors provided  : 5
Valid colors parsed     : 5
Brightest color         : #FFFFFF (R=255, G=255, B=255)
Color name              : White
Brightness value        : 255.00
```

---

## 📂 File Structure

```
├── color_analyzer.py       # Main script with analysis logic and tests
├── flowchart.svg           # Algorithm flowchart
└── README.md               # Project description
```

---

## 🌐 API Used

- [CSS Colors API](https://csscolorsapi.com/) — used to get the human-readable name of a color

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## 🙌 Contributions

Contributions and suggestions are always welcome! Feel free to fork the repo and submit a pull request.
