
# PROJECTS 6 : _Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# 1. Using self
# Assignment:
#  Create a class Student with attributes name and marks.Use the self keyword to initialize these values via a constructor.
# Add a method display() that prints student details.

print ("1).++++++++++++++++++++++++++++++++++++++++++++++++++")



class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"student Name {self.name}")
        print(f"student marks {self.marks}")

student1 = student("Irfan",99.9)
student1.display()



# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

print ("2).++++++++++++++++++++++++++++++++++++++++++++++++++")


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_counter(cls):
        print(f"My total created objects are: {cls.count}")

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()
obj6 = Counter()
obj7 = Counter()
obj8 = Counter()
obj9 = Counter()
obj10 = Counter()

Counter.display_counter()



# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

print ("3).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Car():
    def __init__(self, brand):
        self.brand = brand
        

    def start(self):
        print(f"{self.brand} is starting..!")

my__car = Car("Audi")
print(my__car.brand)
my__car.start()



# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
# that allows changing the bank name. Show that it affects all instances.

print ("4).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Bank():
    bamk_name = "HBL"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_ame(cls, name):
        cls.bamk_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, bank: {self.bamk_name}")

account1 = Bank ("Ali")
account2 = Bank ("Imam")
account3 = Bank ("Kashif")
account4 = Bank ("Irfan")
account5 = Bank ("Imran")
account6 = Bank ("Kami")
account7 = Bank ("Furqan")

account1.display()
account2.display()
account3.display()
account4.display()
account5.display()
account1.display()
account6.display()
account7.display()

Bank.change_bank_ame("Standard Chartered Bank")


account1.display()
account2.display()
account3.display()
account4.display()
account5.display()
account1.display()
account6.display()
account7.display()



# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
print ("5).++++++++++++++++++++++++++++++++++++++++++++++++++")


class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
result = MathUtils.add(10, 5)
print(f"Sum of my 2 numbers are:", result)



# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
print ("6).++++++++++++++++++++++++++++++++++++++++++++++++++")


class Logger:
    def __init__(self):
        print("Message Before: Logger object created.")

    def __del__(self):
        print("Message After: Logger object destructor.")

log = Logger()
del log


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


# Hint
# Public : har jaga accessible, 
# protected: subclass access kr sakta hai lekin bahr se krna recommended nai, 
# private: sir class k under se ya gatter method se access ho sakta hai.
# Getter: get_ssn() private data ko safely read krne k liye
# setter: set_salary() protected variable ko validate kr k sata krta hai
print ("7).++++++++++++++++++++++++++++++++++++++++++++++++++")


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive")
    def display(self):
        print(f"Name: {self.name}") #publie
        print(f"Salary: {self._salary}") # protected
        print(f"SSN: {self.__ssn}") #private


class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter command : {self.get_ssn()}")

m= Manager("Ali", "12000", "3467-2541-3685", "IT")
m.show_manager_info()
m.set_salary(15000)
print("Update Salary:" , m._salary)

# print(m.__ssn)
print("private SSN via managed: ", m._Employee__ssn)



# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

print ("8).++++++++++++++++++++++++++++++++++++++++++++++++++")


class Person():
    def __init__(self, name):
        self.name = name
        print(f"Person created with the name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher teaches: {self.subject}")
    
t = Teacher("Sir Hamza", "GIAIC Python")




# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
print ("9).++++++++++++++++++++++++++++++++++++++++++++++++++")

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

    def area(self):
        return self.lenght * self.width
rect =  Rectangle(5,4)
print("Simple area of Ractangle:", rect.area())


# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.
print ("10).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says : Woof Woof!")


dog1 = Dog("Buddy", "Aidi")
dog1.bark()



# 11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.
print ("11).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Book:
    total_books = 0  # Class-level variable

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Test the class method
book1 = Book()
book2 = Book()
book3 = Book()

# Call the class method for each book to increment the total book count
book1.increment_book_count()
book2.increment_book_count()
book3.increment_book_count()

# Print the total book count
print(f'Total books: {Book.total_books}')


#12. Static Methods
#Assignment:
#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.
print ("12).++++++++++++++++++++++++++++++++++++++++++++++++++")


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Usage
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")



# 13. Composition
#Assignment:
#Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.
print ("13).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

# Create an Engine object
my_engine = Engine()

# Create a CarWithEngine object, passing the Engine instance
my_car = CarWithEngine(my_engine)

# Start the engine via the car
my_car.start_engine()  # This will print "Engine started"



#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

print ("14).++++++++++++++++++++++++++++++++++++++++++++++++++")


class EmployeeAgg:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Department:
    def __init__(self, name, employees):
        self.name = name
        # employees is expected to be a list of EmployeeAgg objects
        self.employees = employees

    def show_employees(self):
        print(f"Employees in the {self.name} department:")
        for employee in self.employees:
            print(employee)

# Create some EmployeeAgg objects
employee1 = EmployeeAgg("Farida")
employee2 = EmployeeAgg("Erum")
employee3 = EmployeeAgg("Alishba")

# Create a Department object and pass in the EmployeeAgg objects as a list
department = Department("HR", [employee1, employee2, employee3])

# Call the method to show employees in the department
department.show_employees()


# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.
print ("15).++++++++++++++++++++++++++++++++++++++++++++++++++")


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass
d = D()
d.show()


# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
print ("16).++++++++++++++++++++++++++++++++++++++++++++++++++")


def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

# Now, if we call say_hello():
say_hello()



# 17. Class Decorators
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
print ("17).++++++++++++++++++++++++++++++++++++++++++++++++++")


def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class PersonWithGreeting:
    def __init__(self, name):
        self.name = name

# Create an instance of PersonWithGreeting
person = PersonWithGreeting("Farida")

# Call the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!



# 18. Property Decorators
# Assignment:
#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
print ("18).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage:
product = Product(100)  # Initialize with price 100

# Accessing the price using the getter
print("Initial Price:", product.price)

# Changing the price using the setter
product.price = 150
print("Updated Price:", product.price)

# Deleting the price using the deleter
del product.price

# Trying to access the price after deletion (this will raise an AttributeError)
try:
    print("Price after deletion:", product.price)
except AttributeError as e:
    print("Error:", e)




# 19. callable() and __call__()
# assignment
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
print ("19).++++++++++++++++++++++++++++++++++++++++++++++++++")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Create an instance of Multiplier with a factor of 3
multiply_by_3 = Multiplier(3)

# Use the __call__ method by calling the object as a function
result = multiply_by_3(5)  # Should multiply 5 by 3

print(result)



# 20. Creating a Custom Exception
# Assignmemt
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
print ("20).++++++++++++++++++++++++++++++++++++++++++++++++++")

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    return "Age is valid"

# Test the function
try:
    age = 16  # You can change this value to test different cases
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")


# 21. Make a Custom Class Iterable
# Countdown class that makes it an iterable
print ("21).++++++++++++++++++++++++++++++++++++++++++++++++++")

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Testing the Countdown class
countdown = Countdown(5)

# Collecting the output from the Countdown iterable
output = list(countdown)
print(output)