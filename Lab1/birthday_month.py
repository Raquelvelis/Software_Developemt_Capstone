from datetime import datetime


def main():
    # Get user input
    name = input("What's your name? ")
    birth_month = input("What month were you born in? ")

    # Print greeting with name
    print(f"Hello, {name}!")

    # Print number of letters in name
    letter_count = len(name)
    print(f"Your name has {letter_count} letters in it.")

    # Get current month name
    current_month = datetime.now().strftime("%B")

    # Check if it's their birthday month (case-insensitive comparison)
    if birth_month.lower() == current_month.lower():
        print("Happy birthday month!")
    else:
        print(f"It's currently {current_month}, so it's not your birthday month yet.")

if __name__ == "__main__":
    # Run the main version (using datetime to get current month)
    main()

    # Uncomment the line below to run the easier version instead:
    # main_easy()