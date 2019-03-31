from order import Order


class TransformationOrder(Order):
    def __init__(self, number, from_, to, quantity):
        super().__init__(number)
        self.from_ = from_
        self.to = to
        self.quantity = quantity

    def print(self):
        print("Number: %s, From: %s, To: %s, Quantity: %s" % (self.number, self.from_, self.to, self.quantity))
