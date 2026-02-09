


class Outer:
    def __init__(self):
        self.name = "Outer class"
        
    class Inner:
        def __init__(self):
            self.name = "inner class"
        def display(self):
            print("This is inner class")
            
outer = Outer()
inner = outer.Inner()

inner.display()




# Pass the outer class instance to the inner class:

class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()



# example

class Car:
    def __init__(self, brand, model, engine):
       self.brand = brand
       self.model = model
       self.engine = engine
       
    