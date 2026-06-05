"""
================================================================================
                    OBJECT ORIENTED PROGRAMMING - OVERVIEW
================================================================================

WHAT IS OOPS?
Object-Oriented Programming (OOP) is a programming paradigm that structures
code around "objects" rather than "functions and logic". It's a way to organize
code to be more modular, reusable, and easier to maintain.

WHY USE OOPS?
1. Modularity: Code is organized into reusable objects
2. Reusability: Classes can be used multiple times
3. Flexibility: Easy to modify and extend functionality
4. Security: Data hiding through encapsulation
5. Maintainability: Easier to debug and maintain
6. Real-world modeling: Objects mimic real-world entities

================================================================================
                            FOUR PILLARS OF OOPS
================================================================================

1. ENCAPSULATION  - Bundling data and methods, hiding internal details
2. INHERITANCE    - Creating new classes based on existing classes
3. POLYMORPHISM   - Using objects in different ways with different meanings
4. ABSTRACTION    - Hiding complex implementation, showing only essentials

================================================================================
                          LEARNING PATH (BASIC TO ADVANCED)
================================================================================

BASIC LEVEL:
  1. 01_class_and_objects.py       - Understanding classes and objects
  2. 02_attributes_and_methods.py  - Attributes (variables) and methods (functions)
  3. 03_constructors_and_destructors.py - Initialization and cleanup

INTERMEDIATE LEVEL:
  4. 04_encapsulation.py           - Data hiding and access control
  5. 05_inheritance.py             - Creating classes from other classes
  6. 06_polymorphism.py            - Same method, different behaviors

ADVANCED LEVEL:
  7. 07_abstraction.py             - Abstract classes and methods
  8. 08_composition.py             - Has-a relationship (objects within objects)
  9. 09_method_overloading_overriding.py - Advanced method techniques
  10. 10_operator_overloading.py   - Custom behavior for operators
  11. 11_property_decorators.py    - Using @property for controlled access
  12. 12_static_and_class_methods.py - Methods that work differently

MASTERY LEVEL:
  13. 13_design_patterns.py        - Common solutions to common problems
  14. 14_oops_best_practices.py    - Tips and tricks for professional code

================================================================================
"""

# SIMPLE EXAMPLE TO UNDERSTAND OOPS CONCEPT

# WITHOUT OOP (Procedural Approach) - Not ideal
# =====================================================
def create_student():
    student = {
        'name': 'Ali',
        'age': 20,
        'marks': 85
    }
    return student

def display_student(student):
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

s1 = create_student()
display_student(s1)


# WITH OOP (Object-Oriented Approach) - Better!
# =====================================================
class Student:
    """
    This is a Student class - a blueprint for creating student objects
    """
    def __init__(self, name, age, marks):
        # These are ATTRIBUTES (variables of the class)
        self.name = name
        self.age = age
        self.marks = marks
    
    def display_info(self):
        # This is a METHOD (function of the class)
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
    
    def is_passed(self):
        """Method to check if student passed (marks >= 40)"""
        return self.marks >= 40

# Creating objects from the Student class
student1 = Student("Ali", 20, 85)
student2 = Student("Fatima", 19, 92)

# Using methods
student1.display_info()
student2.display_info()

print(f"\nStudent 1 passed: {student1.is_passed()}")

print("\n" + "="*80)
print("KEY DIFFERENCES:")
print("="*80)
print("""
Procedural:
  - Data and functions are separate
  - Hard to manage multiple students
  - Code is less organized

Object-Oriented:
  - Data and functions are together in a class
  - Easy to create multiple student objects
  - Code is organized and reusable
  - Each object has its own data
""")
