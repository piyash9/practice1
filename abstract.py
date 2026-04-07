
from abc import ABC, abstractmethod

class paymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass

class CardPay(paymentGateway):
    def pay(self):
        print("Paid Using Card")

class UPIpay(paymentGateway):
    def pay(self):
        print("paid using UPI")

class purchase:
    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checkout started")
        self.gateway.pay()

p1 = purchase(CardPay())
p2 = purchase(UPIpay())

p1.checkout()
p2.checkout()