class Coffee:
    all_coffees = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name

    def orders(self):
        return self._orders

    def customers(self):
        # Return unique list of customers who ordered this coffee
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        # Return the total number of times this coffee has been ordered
        return len(self._orders)

    def average_price(self):
        # Return the average price of this coffee based on its orders
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
