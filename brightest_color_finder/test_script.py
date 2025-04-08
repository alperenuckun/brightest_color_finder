from brightest_color_finder import BrightestColorFinder

if __name__ == "__main__":
    sample_colors = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    finder = BrightestColorFinder(sample_colors)
    result = finder.find_brightest()
    print(result)