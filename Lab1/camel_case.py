import re
import keyword

def to_camel_case(sentence):
    """
    Converts a sentence to camelCase format.
    First word is lowercase, subsequent words have first letter capitalized.
    All words are joined together with no spaces.

    Args:
        sentence (str): The input sentence to convert

    Returns:
        str: The camelCase version of the sentence
    """
    # Split the sentence into words (handles multiple spaces)
    words = sentence.split()

    # If no words, return empty string
    if not words:
        return ""

    # Convert first word to lowercase
    camel_case_words = [words[0].lower()]

    # Convert remaining words: first letter uppercase, rest lowercase
    for word in words[1:]:
        camel_case_words.append(word.capitalize())

    # Join all words together
    return ''.join(camel_case_words)


def is_valid_variable_name(name):
    """
    Checks if a string would make a valid Python variable name.

    Args:
        name (str): The string to check

    Returns:
        tuple: (is_valid: bool, issues: list of strings)
    """
    issues = []

    # Check if empty
    if not name:
        issues.append("Variable name cannot be empty")
        return False, issues

    # Check if starts with a number
    if name[0].isdigit():
        issues.append("Variable name cannot start with a number")

    # Check for valid characters (letters, numbers, underscores only)
    # Using regex to find any invalid characters
    invalid_chars = re.findall(r'[^a-zA-Z0-9_]', name)
    if invalid_chars:
        unique_invalid = list(set(invalid_chars))
        issues.append(f"Variable name contains invalid characters: {', '.join(unique_invalid)}")

    # Check if it's a Python keyword
    # First use the keyword package to get the real list
    python_keywords = keyword.kwlist

    if name in python_keywords:
        issues.append(f"'{name}' is a Python keyword and cannot be used as a variable name")

    # Return True if no issues found
    return len(issues) == 0, issues


def main():
    """
    Main function to demonstrate the camel case converter with validation.
    """
    print("=== Camel Case Converter ===")
    print("Enter a sentence to convert to camelCase format.")
    print("Type 'quit' to exit.\n")

    # Test cases for demonstration
    test_cases = [
        "fOnt proCESSOR and ParsER",
        "hello world test",
        "PYTHON programming LANGUAGE",
        "123 start with number",
        "has special characters #@!",
        "class definition method",  # Contains Python keyword
        "valid variable name",
        "a",
        "",
        "multiple    spaces   between    words",
        "import",
        "class",
        "raquel velis cordero"
    ]

    print("First, let's test with some example inputs:\n")

    for i, test_input in enumerate(test_cases, 1):
        print(f"Test {i}: '{test_input}'")

        # Convert to camel case
        camel_result = to_camel_case(test_input)
        print(f"  Camel case: '{camel_result}'")

        # Check if it's a valid variable name
        is_valid, issues = is_valid_variable_name(camel_result)

        if is_valid:
            print("  ✅ Valid variable name!")
        else:
            print("  ⚠️  Warning - Invalid variable name:")
            for issue in issues:
                print(f"     - {issue}")

        print()  # Empty line for readability

if __name__ == "__main__":
    main()