from decimal import Decimal
from dateutil.parser import parse
from bricklane_platform.config import PAYMENT_FEE_RATE

class PaymentType(object):
    def __init__(self, data=None):
        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])
        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee
    def is_successful(self):
        return