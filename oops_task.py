#task 1
class Restaurant:
    def __init__(self, menu):
        self.__menu = menu

    def show_menu(self):
        print("Menu:", self.__menu)

    def prepare_food(self):
        print("Preparing food...")


class PizzaRestaurant(Restaurant):
    def prepare_food(self):
        print("Pizza is being baked.")


class BurgerRestaurant(Restaurant):
    def prepare_food(self):
        print("Burger is being grilled.")


class SouthIndianRestaurant(Restaurant):
    def prepare_food(self):
        print("Making hot dosa and sambar.")


p1 = PizzaRestaurant(["Margherita", "Veg Pizza"])
b1 = BurgerRestaurant(["Cheese Burger", "Veg Burger"])
s1 = SouthIndianRestaurant(["Dosa", "Idli"])

p1.show_menu()
p1.prepare_food()

b1.show_menu()
b1.prepare_food()

s1.show_menu()
s1.prepare_food()

#task 2

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    def __init__(self, account):
        self.__account = account

    def show_account(self):
        print("Account:", self.__account)

    @abstractmethod
    def process_payment(self, amount):
        pass


class UPI(PaymentMethod):

    def process_payment(self, amount):
        print("Paid", amount, "using UPI")


class CreditCard(PaymentMethod):

    def process_payment(self, amount):
        print("Paid", amount, "using Credit Card")


class NetBanking(PaymentMethod):

    def process_payment(self, amount):
        print("Paid", amount, "using Net Banking")


u = UPI("upi123")
c = CreditCard("card456")
n = NetBanking("bank789")

u.show_account()
u.process_payment(500)

c.show_account()
c.process_payment(1000)

n.show_account()
n.process_payment(750)

#task 3

from abc import ABC, abstractmethod


class SmartDevice(ABC):

    def __init__(self):
        self.__status = "OFF"

    def turn_on(self):
        self.__status = "ON"

    def turn_off(self):
        self.__status = "OFF"

    def show_status(self):
        print("Status:", self.__status)

    @abstractmethod
    def operate(self):
        pass


class Fan(SmartDevice):

    def operate(self):
        print("Fan is spinning.")


class Light(SmartDevice):

    def operate(self):
        print("Light is glowing.")


class AirConditioner(SmartDevice):

    def operate(self):
        print("AC is cooling the room.")


f = Fan()
l = Light()
a = AirConditioner()

f.turn_on()
f.show_status()
f.operate()

l.turn_on()
l.show_status()
l.operate()

a.turn_on()
a.show_status()
a.operate()