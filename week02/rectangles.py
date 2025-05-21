def get_positive_value(prompt):
    """Prompt the user for a value and re-prompt the if the value is negative

    Args:
        prompt (string): the prompt to ask the user
        value (string): the value asking from the user
    """

    value = -1

    while value < 0:
        value = float(input(f"{prompt} "))

        if value != -1 and value < 0:
            print("Sorry, the value cannot be negative.")

    return value


length = get_positive_value("What is the length of you rectangle? ")
width = get_positive_value("What is the width of you rectangle? ")

area = length * width

print(f"The area is {area}")