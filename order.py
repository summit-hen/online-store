class Order:
    def __init__(self, order_id, shopping_cart):
        self.order_id = order_id
        self.shopping_cart = shopping_cart

    def get_order_id(self):
        return self.order_id

    def get_shopping_cart(self):
        return self.shopping_cart
