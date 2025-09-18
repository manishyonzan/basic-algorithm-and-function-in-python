# High-level modules should not depend on low-level modules. Both should depend on abstractions.

from abc import abstractmethod, ABC

class PaymentGateAway(ABC):
    @abstractmethod
    def process_payment():
        pass
    
class Credit_Card_Gateaway(PaymentGateAway):
    def process_payment(self,amount):
        return f"Processing amount:{amount} in credit card payment"
class Paypal_Gateway(PaymentGateAway):
    def process_payment(self,amount):
        return f"Processing amount:{amount} in paypal payment"
    
class PaymentService:
    def __init__(self, payment_gateway: PaymentGateAway):
        self.payment_gateway = payment_gateway
    def make_payment(self,amount):
        return self.payment_gateway.process_payment(amount)
    
if __name__ == "__main__":
    #credit card payment
    credit_payment_service = PaymentService(Credit_Card_Gateaway())
    print(credit_payment_service.make_payment(100))
    
    #paypal payment
    paypal_payment_service = PaymentService(Paypal_Gateway())
    print(paypal_payment_service.make_payment(100))
        