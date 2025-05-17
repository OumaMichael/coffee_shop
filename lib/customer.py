class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    def orders(self):
        return self._orders

    def coffees(self):
        # Return unique list of coffees ordered by this customer
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        from order import Order
        # Create a new order and associate it with this customer and the coffee
        new_order = Order(self, coffee, price)
        return new_order

    @classmethod
    def most_aficionado(cls, coffee):
        # Find the customer who has spent the most on the given coffee
        if not coffee.orders():
            return None
        
        # Create a dictionary to track total spent by each customer
        customer_spending = {}
        
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        
        # Find the customer with the highest spending
        if not customer_spending:
            return None
            
        return max(customer_spending.items(), key=lambda x: x[1])[0]
