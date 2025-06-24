
"""
Operator	Magic Method	Description
+	        __add__	        Addition
-	        __sub__	        Subtraction
*	        __mul__	        Multiplication
/	        __truediv__	    Division
//	        __floordiv__	Floor division
%	        __mod__	        Modulo
**	        __pow__	        Exponentiation

"""


"""
Operator	Magic Method	Description
==	        __eq__	        Equal to
!=	        __ne__	        Not equal to
<	        __lt__	        Less than
>	        __gt__	        Greater than
<=	        __le__	        Less than or equal to
>=	        __ge__	        Greater than or equal to

"""


from functools import total_ordering
from decimal import Decimal


@total_ordering # Implements all comparison methods based on __eq__ and __lt__
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = Decimal(str(amount))
        self.currency = currency
        
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f'cannot add differenct currencies: {self.currency} and {other.currency}')
        return Money(self.amount + other.amount, currency=self.currency)
    
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f'cannot add differenct currencies: {self.currency} and {other.currency}')
        return Money(self.amount - other.amount, currency=self.currency)
    
    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount * other, currency=self.currency)
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return Money(self.amount / Decimal(str(other)), self.currency)
        return NotImplemented
    
    def _eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return NotImplemented
    
    def __lt__(self,other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f'cannot add differenct currencies: {self.currency} and {other.currency}')
        return self.amount < other.amount
    
    def __str__(self):
        return f"{self.currency} {self.amount:.2f}"

    def __repr__(self):
        return f"Money({repr(float(self.amount))}, {repr(self.currency)})"
    
    
    
    
    
wallet = Money(100, "USD")
expense = Money(20, "USD")

print(wallet - expense)        #USD 80.00


# adding the currency

salary = Money(1000, "USD")
bonus = Money(20, "USD")

total = salary + bonus

print(type(total), total)  #<class '__main__.Money'> USD 1020.00



# Division by scalar


weekly_pay = total / 4

print(weekly_pay) # USD 255.00

#comparisions


# @total_ordering: This decorator automatically implements all comparison methods based on __eq__ and __lt__.

# so even > (__gt__) is not implemented it is automatically created

print(Money(100, "USD") > Money(50,"USD"))
print(Money(100, "USD") == Money(100,"USD"))



try:
    Money(100, "USD") + Money(100, "EURO")
except ValueError as e:
    print(e)
    
