from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash.")


# Main Program
credit = CreditCardPayment()
upi = UPIPayment()
cash = CashPayment()

credit.pay(1500)
upi.pay(800)
cash.pay(500)