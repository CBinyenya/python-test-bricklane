from bricklane_platform.models.util import PaymentType


class BankAccount(PaymentType):
    bank_account_id = None
    
    def __init__(self, data=None):
        if data:
            PaymentType.__init__(self, data)
            self.bank_account_id = int(data["bank_account_id"])
    def is_successful(self):
        return True