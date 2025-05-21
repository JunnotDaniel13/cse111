# Author: Jerenason Junnot Daniel
# Assignment: W01 Project Milestone: Tire Volume

import math
from datetime import datetime

while True:
    width_mm_str = input("Enter the width of the tire in mm (ex 205): ")
    aspect_ratio_str = input("Enter the aspect ratio of the tire (ex 60): ")
    diameter_inches_str = input("Enter the diameter of the wheel in inches (ex 15): ")

    w = float(width_mm_str)
    a = float(aspect_ratio_str)
    d = float(diameter_inches_str)

    numerator_term1 = math.pi * (w**2) * a
    numerator_term2 = w * a + 2540 * d
    numerator = numerator_term1 * numerator_term2
    denominator = 10_000_000_000
    volume_liters = numerator / denominator

    print(f"The approximate volume is {volume_liters:.2f} liters")

    current_date_object = datetime.now()
    formatted_date = current_date_object.strftime("%Y-%m-%d")

    try:
        with open("volumes.txt", "at") as outfile:
            outfile.write(f"{formatted_date}, {w}, {a}, {d}, {volume_liters:.2f}\n")
        print("Tire data successfully saved to volumes.txt.")  # Idea 4
    except IOError:
        print("Error: Could not write to volumes.txt.")

    another_entry = input(
        "Would you like to enter data for another tire? (yes/no): "
    ).lower()
    if another_entry != "yes":
        break

print("Thank you for using the tire volume calculator!")
