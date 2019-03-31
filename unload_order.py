from order import Order


class UnloadOrder(Order):
    def __init__(self, number, type_, destination, quantity):
        super().__init__(number)
        self.type_ = type_
        self.destination = destination
        self.quantity = quantity

    def print(self):
        print("Number: %s , Type: %s, Destination: %s, Quantity: %s" % (self.number, str(self.type_),
                                                                        str(self.destination), str(self.quantity)))
