# Base class: Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def fight_crime(self):
        return f"{self.name} is fighting crime with their {self.power} in {self.city}!"

    def save_the_day(self):
        return f"{self.name} saves the day in {self.city} with their {self.power}."

# Derived class: FlyingSuperhero (inherits from Superhero)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, can_fly=True):
        super().__init__(name, power, city)
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying high above {self.city}!"
        else:
            return f"{self.name} cannot fly, but they can still save the day!"

# Create objects
hero1 = Superhero("Spiderman", "web-slinging", "New York")
hero2 = FlyingSuperhero("Superman", "super strength", "Metropolis", True)

# Interact with objects
print(hero1.fight_crime())  # Output: Spiderman is fighting crime with their web-slinging in New York!
print(hero1.save_the_day()) # Output: Spiderman saves the day in New York with their web-slinging.

print(hero2.fight_crime())  # Output: Superman is fighting crime with their super strength in Metropolis!
print(hero2.save_the_day()) # Output: Superman saves the day in Metropolis with their super strength.
print(hero2.fly())          # Output: Superman is flying high above Metropolis!


