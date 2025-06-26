import sys

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
      
      
# Compare memory usage
regular_people = [RegularPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]
slotted_people = [SlottedPerson("Vivek" + str(i), 30, "hello@wewake.dev") for i in range(1000)]
  

print(f"Regular person size: {sys.getsizeof(regular_people[0])} bytes")  # Output: Regular person size: 48 bytes
print(f"Slotted person size: {sys.getsizeof(slotted_people[0])} bytes")  # Output: Slotted person size: 56 bytes
print(f"Memory saved per instance: {sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])} bytes")  # Output: Memory saved per instance: -8 bytes
print(f"Total memory saved for 1000 instances: {(sys.getsizeof(regular_people[0]) - sys.getsizeof(slotted_people[0])) * 1000 / 1024:.2f} KB")  # Output: Total memory saved for 1000 instances: -7.81 KB



print("\n")


# A more accurate memory measurement
import sys

def get_size(obj):
    """Get a better estimate of the object's size in bytes."""
    size = sys.getsizeof(obj)
    if hasattr(obj, '__dict__'):
        size += sys.getsizeof(obj.__dict__)
        # Add the size of the dict contents
        size += sum(sys.getsizeof(v) for v in obj.__dict__.values())
    return size

class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

class SlottedPerson:
    __slots__ = ['name', 'age', 'email']

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

regular = RegularPerson("Vivek", 30, "hello@wewake.dev")
slotted = SlottedPerson("Vivek", 30, "hello@wewake.dev")

print(f"Complete Regular person size: {get_size(regular)} bytes")  # Output: Complete Regular person size: 610 bytes
print(f"Complete Slotted person size: {get_size(slotted)} bytes")  # Output: Complete Slotted person size: 56 bytes




