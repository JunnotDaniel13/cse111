LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}\\|;:'\",.<>/?`~")

DICTIONARY_FILE = "wordlist.txt"
TOP_PASSWORDS_FILE = "toppasswords.txt"


def word_in_file(word, filename, case_sensitive=False):
    """
    Checks if a word exists in a file.
    Parameters:
        word: The word to search for.
        filename: The name of the file to search in.
        case_sensitive: Boolean, True for case-sensitive match,
                        False for case-insensitive. Defaults to False.
    Return Type: Boolean
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                file_word = line.strip()
                if not case_sensitive:
                    if word.lower() == file_word.lower():
                        return True
                else:
                    if word == file_word:
                        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False
    return False


def word_has_character(word, character_list):
    """
    Checks if any character in the word is present in the character_list.
    Parameters:
        word: The word to check.
        character_list: A list of characters to look for.
    Return Type: Boolean
    """
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """
    Calculates the complexity of a word based on character types.
    Parameters:
        word: The word to analyze.
    Return Type: Integer (0-4)
    """
    if not word:
        return 0

    complexity_score = 0
    if word_has_character(word, LOWER):
        complexity_score += 1
    if word_has_character(word, UPPER):
        complexity_score += 1
    if word_has_character(word, DIGITS):
        complexity_score += 1
    if word_has_character(word, SPECIAL):
        complexity_score += 1
    return complexity_score


def has_sequential_chars(password, length=3):
    """Checks for sequential characters (e.g., "abc", "123")."""
    if len(password) < length:
        return False
    for i in range(len(password) - length + 1):
        is_seq_letter = True
        for j in range(length - 1):
            if ord(password[i + j + 1]) - ord(password[i + j]) != 1:
                is_seq_letter = False
                break
        if is_seq_letter and password[i : i + length].isalpha():
            return True

        is_seq_digit = True
        for j in range(length - 1):
            if ord(password[i + j + 1]) - ord(password[i + j]) != 1:
                is_seq_digit = False
                break
        if is_seq_digit and password[i : i + length].isdigit():
            return True
    return False


def has_repeated_chars(password, count=3):
    """Checks for repeated characters (e.g., "aaa", "111")."""
    if len(password) < count:
        return False
    for i in range(len(password) - count + 1):
        substring = password[i : i + count]
        if len(set(substring)) == 1:
            return True
    return False


def password_strength(password, min_length=10, strong_length=16):
    """
    Calculates the strength of a password based on various criteria.
    Parameters:
        password: The password string to check.
        min_length: The minimum acceptable password length. Defaults to 10.
        strong_length: The length at which a password is considered strong
                       regardless of complexity. Defaults to 16.
    Return Type: Integer (0-5)
    """
    if not password:
        print("Password cannot be empty.")
        return 0

    if word_in_file(password, DICTIONARY_FILE, case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, TOP_PASSWORDS_FILE, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if has_sequential_chars(password):
        print(
            "Password contains sequential characters (e.g., 'abc', '123') and is less secure."
        )

    if has_repeated_chars(password):
        print(
            "Password contains repeated characters (e.g., 'aaa', '111') and is less secure."
        )

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    complexity = word_complexity(password)
    strength_score = 1 + complexity

    complexity_details = []
    if word_has_character(password, LOWER):
        complexity_details.append("lowercase letters")
    if word_has_character(password, UPPER):
        complexity_details.append("uppercase letters")
    if word_has_character(password, DIGITS):
        complexity_details.append("digits")
    if word_has_character(password, SPECIAL):
        complexity_details.append("special symbols")

    if complexity_details:
        print(
            f"Password complexity score: {complexity} (uses: {', '.join(complexity_details)})"
        )
    else:
        print("Password does not meet basic complexity (e.g. only unknown characters).")

    return strength_score


def main():
    """
    Provides the user input loop for checking password strength.
    """
    print("Password Strength Checker")
    print("Enter 'q' or 'Q' to quit.")

    while True:
        password = input("Enter a password to test: ")
        if password.lower() == "q":
            print("Exiting password checker.")
            break

        if not password:
            print("Please enter a password.")
            continue

        strength = password_strength(password)
        print(f"Calculated password strength: {strength}/5")
        print("-" * 30)


if __name__ == "__main__":
    main()
