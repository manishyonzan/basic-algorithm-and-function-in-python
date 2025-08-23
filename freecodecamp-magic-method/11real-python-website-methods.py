# differrence between @classmethod , @staticmethod and plain methods


class Myclass:
    def method(self):
        """
            can modify object instance state
            can modify class state
        """
        return 'instance method called',self
    @classmethod
    def classmethod(cls):
        """
            can't modify object instance state
            can modify class state
        """
        return 'class method',cls
    
    @staticmethod
    def staticmethod():
        """
            can't modify object instance state
            can't modify class state
        """
        return 'static method'
    
obj = Myclass()
print(obj.method()) #('instance method called', <__main__.Myclass object at 0x0000021D920B4A90>)
print(obj.classmethod()) #('class method', <class '__main__.Myclass'>)
print(obj.staticmethod()) # static method

Myclass.staticmethod()
Myclass.classmethod()
# Myclass.method() #TypeError: Myclass.method() missing 1 required positional argument: 'self', we cannot run plain method without creating object






class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients})"
    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomato'])
    
    @classmethod
    def peperoni(cls):
        return  cls(['mozzarella', 'tomato', 'pepperoni'])
    @staticmethod
    def validate_ingredient(ingredient):
        return ingredient in ['mozzarella', 'tomato', 'basil']
    @staticmethod
    def calculate_price(size, num_toppings):
        base_price = {'small': 8, 'medium': 10, 'large': 12}
        return base_price[size] + num_toppings * 1.5


a  = Pizza.margherita()
a.add_ingredient('spice')
print(a.__repr__())

# Usage of static method
price = Pizza.calculate_price('medium', 3)
print(price)  # Output: 14.5

# add which ever value is available and not

profile = {
    'name':"N\A",
    'email' : "N\A",
    'phone':"N\A"
}

user = {
    'name':"bob",
    'phone':"9845433221"
}

profile |= user # only from python 3.9
# profile.update(user)
# profile = {**profile, ** user}
print(profile)

