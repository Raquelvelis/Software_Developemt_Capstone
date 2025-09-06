def main():
    print("Let's create a list of your classes for this semester!")
    print("Enter each class name (press Enter after each one)")
    print("When you're done, just press Enter on an empty line.")
    print()

    classes = []

    while True:
        class_name = input("Enter a class name (or press Enter to finish): ")

        # If user presses Enter without typing anything, we're done
        if class_name == "":
            break

        # Add the class to our list
        classes.append(class_name)

    # Print the results
    print("\n" + "=" * 40)
    print("YOUR CLASSES THIS SEMESTER:")
    print("=" * 40)

    if classes:  # Check if the list is not empty
        for class_name in classes:
            print(class_name)
    else:
        print("No classes entered.")

    print(f"\nTotal number of classes: {len(classes)}")


if __name__ == "__main__":
    # Run the main version (keeps asking until user presses Enter)
    main()

    # Uncomment the line below to run the version that asks for a count first:
    # main_with_count()