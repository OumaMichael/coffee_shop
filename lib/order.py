class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
        
        # Add this order to the customer's and coffee's order lists
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not 1.0 <= float(price) <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(price)
