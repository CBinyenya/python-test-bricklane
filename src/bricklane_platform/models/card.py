from bricklane_platform.models.util import PaymentType


class Card(PaymentType):

    card_id = None
    status = None
    
    def is_successful(self):
        return self.status == "processed"
