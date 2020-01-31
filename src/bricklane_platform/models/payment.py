from bricklane_platform.models.card import Card
from bricklane_platform.models.bank_account import BankAccount


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None
    source = None
    
    def __init__(self, data=None, source=None):

        if not data or not source or source not in ["card", "bank"]:
            return
        self.source = source
        self._card = None
        self._bank_account = None
        
        self.payment_type = None
        if source == "card":
            self.payment_type = Card(data)
            self._card = self.payment_type
        elif source == "bank":
            self.payment_type = BankAccount(data)
            self._bank_account = self.payment_type
        else:
            raise ValueError("Please provide source either (card or bank)")
        if self.payment_type:
            self.customer_id = self.payment_type.customer_id
            self.date = self.payment_type.date
            self.fee = self.payment_type.fee
            self.amount = self.payment_type.amount

        
    @property
    def card(self):
        return self._card
    
    @card.setter
    def card(self, value):
        self._card = value
        self.payment_type = value
    
    @property
    def bank_account(self):
        return self._bank_account
    
    @bank_account.setter 
    def bank_account(self, value):
        self._bank_account = value
        self.payment_type = value
        
    
    def is_successful(self):
        return self.payment_type.is_successful()
