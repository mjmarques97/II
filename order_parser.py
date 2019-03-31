from xml.etree import cElementTree as ET
from order import Order
from transformationorder import TransformationOrder
from unload_order import UnloadOrder


class OrderCreator:
    def __init__(self, file):
        self.file = file
        self.xmldoc = ET.parse(self.file)
        self.root = self.xmldoc.getroot()
        self.transformation_order_list = []
        self.unload_order_list = []

        self.create_orders()

    def create_orders(self):
        for orders in self.root:
            number = orders.get('Number')
            # Transform
            for transform in orders.iter('Transform'):
                from_ = transform.get('From')
                to = transform.get("To")
                quantity = transform.get("Quantity")
                self.transformation_order_list.append(TransformationOrder(number, from_, to, quantity))

            # Unload
            for unload in orders.iter('Unload'):
                type_ = unload.get("Type")
                destination = unload.get("Destination")
                quantity = unload.get("Quantity")
                self.unload_order_list.append(UnloadOrder(number, type_, destination, quantity))

    def print_unload_order_list(self):
        print("Unload: ")
        for orders in self.unload_order_list:
            orders.print()

    def print_transform_order_list(self):
        print("Transform: ")
        for orders in self.transformation_order_list:
            orders.print()

    def print_all(self):
        self.print_transform_order_list()
        self.print_unload_order_list()
        print("")
