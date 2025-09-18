# Objects of a superclass should be replaceable with objects of its subclasses without altering the correctness of the program

# Scenario: Bird Behavior Simulation
# Let’s say you’re modeling birds. 
# All birds can fly, right? 
# Well… not quite. If you design your system assuming every bird flies, and then add a penguin, things break. LSP helps you avoid that trap.


# Violating LSP (Bad Design)
class Bird:
    def fly(self):
        print("Flying high!")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates LSP

def make_bird_fly(bird: Bird):
    bird.fly()

"""
penguin = Penguin()
make_bird_fly(penguin) 
"""




# LSP-Compliant Design

from abc import ABC, abstractmethod

# Base class for all birds
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

# Flying birds
class Sparrow(Bird):
    def move(self):
        print("Sparrow flies through the sky.")

# Non-flying birds
class Penguin(Bird):
    def move(self):
        print("Penguin waddles on the ice.")

# Function that respects LSP
def move_bird(bird: Bird):
    bird.move()

# 🧪 Usage
sparrow = Sparrow()
penguin = Penguin()

move_bird(sparrow)  
move_bird(penguin)  
