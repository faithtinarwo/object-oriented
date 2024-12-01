# Base class: Animal
class Animal:
    def move(self):
        pass

# Derived class: Dog
class Dog(Animal):
    def move(self):
        return "The dog is running 🐕"

# Derived class: Bird
class Bird(Animal):
    def move(self):
        return "The bird is flying 🦅"

# Create objects
dog = Dog()
bird = Bird()

# Call the move method for each
print(dog.move())   # Output: The dog is running 🐕
print(bird.move())  # Output: The bird is flying 🦅
