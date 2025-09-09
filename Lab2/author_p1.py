class Author:
    """A class to represent an author and their published books."""

    def __init__(self, name):
        """Initialize a new Author with a name and empty books list.

        Args:
            name (str): The author's name
        """
        self.name = name
        self.books = []  # Start with empty list of books

    def publish(self, title):
        """Add a new book title to the author's list of published books.

        Args:
            title (str): The title of the book to publish
        """
        self.books.append(title)

    def __str__(self):
        """Return a string representation of the author and their books.

        Returns:
            str: Author name and list of their published books
        """
        if self.books:
            # Join book titles with commas if the author has published books
            book_list = ', '.join(self.books)
            return f'{self.name}. Books: {book_list}'
        else:
            # Handle case where author has no published books yet
            return f'{self.name}. Books: No published books'


def main():
    """Test the Author class with example authors and books."""

    # Create first author and add multiple books
    rowling = Author('J. K. Rowling')
    rowling.publish('Harry Potter and the Philosopher\'s Stone')
    rowling.publish('Fantastic Beasts and Where to Find Them')
    print(rowling)

    # Create second author with different books
    tolkien = Author('J.R.R. Tolkien')
    tolkien.publish('The Hobbit')
    tolkien.publish('The Lord of the Rings')
    print(tolkien)

    # Test author with no books initially
    new_author = Author('Clara Smith')
    print(new_author)

    # Test adding a book to previously book-less author
    new_author.publish('My First Novel')
    print(new_author)

# Only run main function if this file is executed directly
if __name__ == '__main__':
    main()