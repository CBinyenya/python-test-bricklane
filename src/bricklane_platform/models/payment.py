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
    card = None

    def __init__(self, data=None, source=None):

        if not data or not source or source not in ["card", "bank"]:
            return
        self.source = source

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        if source == "card":
            card = Card()
            card.card_id = int(data["card_id"])
            card.status = data["card_status"]
            self.card = card
        else:
            account = BankAccount()
            account.bank_account_id = int(data["bank_account_id"])
            self.bank_account = account

    def is_successful(self):
        if self.source == "bank":
            return True
        if self.card:
            return self.card.status == "processed"
