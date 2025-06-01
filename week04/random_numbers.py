import random

def append_random_numbers(numbers_list, quantity=1):
    """
    Appends 'quantity' random floating-point numbers to 'numbers_list'.
    Each number is between 0.0 and 100.0 and rounded to one decimal place.

    Parameters:
        numbers_list: The list to append numbers to.
        quantity: The number of random numbers to append. Defaults to 1.
    """
    for _ in range(quantity):
        random_float = random.uniform(0.0, 100.0)
        rounded_float = round(random_float, 1)
        numbers_list.append(rounded_float)

def append_random_words(words_list, quantity=1):
    """
    Appends 'quantity' random words to 'words_list' from a predefined list.

    Parameters:
        words_list: The list to append words to.
        quantity: The number of random words to append. Defaults to 1.
    """
    sample_words = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon",
        "join", "love", "smile", "cloud", "head", "dream" 
    ]
    for _ in range(quantity):
        random_word = random.choice(sample_words)
        words_list.append(random_word)

def main():
    """
    Main function to demonstrate list manipulation with random numbers and words.
    """
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    print() 

    words = ["join", "love", "smile"] 
    append_random_words(words, 3)
    print(f"words {words}")


if __name__ == "__main__":
    main()