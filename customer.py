from order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.order_id_counter = 1

    def place_order(self, shopping_cart):
        order_id = self.order_id_counter
        self.order_id_counter += 1
        order = Order(order_id, shopping_cart)
        self.orders.append(order)
        return order

    def display_order(self, order):
        print(f"Order ID: {order.get_order_id()}")
        print("Products:")
        for product, quantity in order.get_shopping_cart().get_products().items():
            print(f"{product.get_name()}: {quantity}")
        print(f"Total: ${order.get_shopping_cart().calculate_total()}")
