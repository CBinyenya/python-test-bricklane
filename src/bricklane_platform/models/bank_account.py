from bricklane_platform.models.util import PaymentType


class BankAccount(PaymentType):
    bank_account_id = None
    
    def is_successful(self):
        return True