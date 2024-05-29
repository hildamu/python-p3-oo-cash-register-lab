#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction = 0  

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity  
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.") 
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            print("No transactions to void.")