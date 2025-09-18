# 🧠 Scenario: Discount System for a Store
# Let’s say you’re building a system to apply discounts to customer orders.
# Instead of modifying the discount logic every time a new type of discount is added, we’ll design it so new discounts can be added by extending the system.

from abc import abstractmethod, ABC

class DiscountStragegy(ABC):
    @abstractmethod
    def applyDiscount(self, total):
        pass
        
class NoDiscount(DiscountStragegy):
    def applyDiscount(self, total):
        return total

class PercentageDiscount(DiscountStragegy):
    def __init__(self,percent):
        self.percent = percent
    def applyDiscount(self, total):
        return total - ((self.percent/100) * total)
class FixedAmountDiscount(DiscountStragegy):
    def __init__(self, amount):
        self.amount = amount
    def applyDiscount(self, total):
        return total - self.amount

class Order:
    def __init__(self, customer, items, discount_strategy:DiscountStragegy):
        self.customer = customer
        self.items = items
        self.discount_strategy = discount_strategy
    
    def total_price(self):
        return sum(price for _,price in self.items)
    
    def final_price(self):
        return self.discount_strategy.applyDiscount(self.total_price())
    
# 🧪 Usage
items = [("Phone", 800), ("Case", 50)]
order1 = Order("Sita", items, NoDiscount())
order2 = Order("Gita", items, PercentageDiscount(10))
order3 = Order("Hari", items, FixedAmountDiscount(100))

print(f"{order1.customer}'s final price: ${order1.final_price()}")
print(f"{order2.customer}'s final price: ${order2.final_price()}")
print(f"{order3.customer}'s final price: ${order3.final_price()}")


# You can now add a LoyaltyDiscount, SeasonalDiscount, 
# or even a BuyOneGetOneDiscount without touching the Order class. That’s the magic of OCP.