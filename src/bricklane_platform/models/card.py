from bricklane_platform.models.util import PaymentType


class Card(PaymentType):

    card_id = None
    status = None
    
    def __init__(self, data=None):
        PaymentType.__init__(self, data)
        if data:
            self.card_id = int(data["card_id"])
            self.status = data["card_status"]
    
    def is_successful(self):
        return self.status == "processed"
