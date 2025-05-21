age = int(input("Enter your age: "))

max_heart_rate = 220 - age

slowest = 0.65 * max_heart_rate
fastest = 0.85 * max_heart_rate

print(
    f"When you exercise to strengthen your heart, you should\nkeep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute."
)
