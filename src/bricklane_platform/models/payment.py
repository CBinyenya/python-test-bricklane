from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.models.bank_account import BankAccount
from bricklane_platform.config import PAYMENT_FEE_RATE


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

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee
        if source == "card":
            self.payment_type = Card()
            self.payment_type.card_id = int(data["card_id"])
            self.payment_type.status = data["card_status"]
            self._card = self.payment_type
        else:
            self.payment_type = BankAccount()
            self.payment_type.bank_account_id = int(data["bank_account_id"])
            self._bank_account = self.payment_type

        
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
