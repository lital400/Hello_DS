# Author: Lital Israel
# Course: CAP 4784
# 2/2/21
# Lab 3 - CreditCard Class Assignment

import random


class CreditCard:

    cardTypes = {1: 'Visa', 2: 'Mastercard', 3: 'Amex', 4: 'Discover'}
    
    def __init__(self, ccNumber, name, expiration):
        self.creditLimit = 1000
        self.cardBalance = random.randint(0, 999)
        self.ccNumber = ccNumber
        self.name = name
        self.expiration = expiration

    def get_cardOwner(self):
        return self.name

    def get_cardType(self):
        if int(self.ccNumber[5]) in self.cardTypes:
            return self.cardTypes[int(self.ccNumber[5])]
        else:
            return 'Not Supported Card Type'

    def processOrder(self, price):
        cardType = self.get_cardType()
        if cardType == 'Not Supported Card Type':
            return False
        elif price < self.cardBalance:
            self.cardBalance += price
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} is the owner of the credit card with number {self.ccNumber} which expires on {self.expiration}."
