# Student dataclass example
# Comparing dataclass vs traditional class

from dataclasses import dataclass

@dataclass
class Student:
    """
    Student data class - much simpler than a traditional class!

    DATACLASS BENEFITS vs TRADITIONAL CLASS:
    - No need to write __init__ method manually
    - No need to write __str__ method manually
    - No need to write __repr__ method manually
    - Automatically gets comparison methods (__eq__, etc.)
    - Less code = fewer bugs!
    """
    name: str
    college_id: int
    gpa: float

    # That's it! Dataclass automatically creates:
    # - __init__(self, name, college_id, gpa)
    # - __str__ method for nice printing


# For comparison, here's what the TRADITIONAL CLASS would look like:
class StudentTraditional:
    """
    Traditional class version - much more code for the same functionality!
    """

    def __init__(self, name: str, college_id: int, gpa: float):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f"StudentTraditional(name='{self.name}', college_id={self.college_id}, gpa={self.gpa})"

    def __eq__(self, other):
        if not isinstance(other, StudentTraditional):
            return False
        return (self.name == other.name and
                self.college_id == other.college_id and
                self.gpa == other.gpa)

def main():
    """
    Test both dataclass and traditional class versions
    """
    print("=== DATACLASS VERSION ===")

    # Create some example students using dataclass
    student1 = Student("Alice Johnson", 12345, 3.75)
    student2 = Student("Bob Smith", 67890, 3.42)
    student3 = Student("Carol Davis", 11111, 3.95)

    # Verify we can read individual fields
    print("Reading individual fields:")
    print(f"Student 1 name: {student1.name}")
    print(f"Student 1 college ID: {student1.college_id}")
    print(f"Student 1 GPA: {student1.gpa}")

    # Verify printing includes GPA
    print("\nPrinting whole student objects (notice GPA is included):")
    print(student1)
    print(student2)
    print(student3)

    print("\n=== TRADITIONAL CLASS VERSION (for comparison) ===")

    # Create the same students using a traditional class
    trad_student1 = StudentTraditional("Alice Johnson", 12345, 3.75)
    trad_student2 = StudentTraditional("Bob Smith", 67890, 3.42)

    print("Traditional class output:")
    print(trad_student1)
    print(trad_student2)

    # Bonus: Show that dataclasses support equality comparison automatically
    print("\n=== BONUS: Automatic equality comparison ===")
    student1_copy = Student("Alice Johnson", 12345, 3.75)
    print(f"student1 == student1_copy: {student1 == student1_copy}")  # True!
    print(f"student1 == student2: {student1 == student2}")  # False


# Run the test
if __name__ == "__main__":
    main()