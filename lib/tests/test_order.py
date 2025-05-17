import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture
def sample_customer():
    return Customer("Alice")

@pytest.fixture
def sample_coffee():
    return Coffee("Espresso")

class TestOrder:
    def test_init_valid_parameters(self, sample_customer, sample_coffee):
        # Test initialization with valid parameters
        order = Order(sample_customer, sample_coffee, 3.5)
        
        assert order.customer == sample_customer
        assert order.coffee == sample_coffee
        assert order.price == 3.5
        assert order in Order.all_orders
        assert order in sample_customer.orders()
        assert order in sample_coffee.orders()

    def test_init_invalid_customer(self, sample_coffee):
        # Test initialization with invalid customer
        with pytest.raises(TypeError):
            Order("Not a customer", sample_coffee, 3.5)

    def test_init_invalid_coffee(self, sample_customer):
        # Test initialization with invalid coffee
        with pytest.raises(TypeError):
            Order(sample_customer, "Not a coffee", 3.5)

    def test_init_invalid_price_type(self, sample_customer, sample_coffee):
        # Test initialization with invalid price type
        with pytest.raises(TypeError):
            Order(sample_customer, sample_coffee, "3.5")

    def test_init_invalid_price_low(self, sample_customer, sample_coffee):
        # Test initialization with price too low
        with pytest.raises(ValueError):
            Order(sample_customer, sample_coffee, 0.5)

    def test_init_invalid_price_high(self, sample_customer, sample_coffee):
        # Test initialization with price too high
        with pytest.raises(ValueError):
            Order(sample_customer, sample_coffee, 15.0)

    def test_customer_property(self, sample_customer, sample_coffee):
        # Test customer property getter
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order.customer == sample_customer

    def test_customer_property_setter_valid(self, sample_customer, sample_coffee):
        # Test customer property setter with valid customer
        order = Order(sample_customer, sample_coffee, 3.5)
        new_customer = Customer("Bob")
        order.customer = new_customer
        assert order.customer == new_customer

    def test_customer_property_setter_invalid(self, sample_customer, sample_coffee):
        # Test customer property setter with invalid customer
        order = Order(sample_customer, sample_coffee, 3.5)
        with pytest.raises(TypeError):
            order.customer = "Not a customer"

    def test_coffee_property(self, sample_customer, sample_coffee):
        # Test coffee property getter
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order.coffee == sample_coffee

    def test_coffee_property_setter_valid(self, sample_customer, sample_coffee):
        # Test coffee property setter with valid coffee
        order = Order(sample_customer, sample_coffee, 3.5)
        new_coffee = Coffee("Latte")
        order.coffee = new_coffee
        assert order.coffee == new_coffee

    def test_coffee_property_setter_invalid(self, sample_customer, sample_coffee):
        # Test coffee property setter with invalid coffee
        order = Order(sample_customer, sample_coffee, 3.5)
        with pytest.raises(TypeError):
            order.coffee = "Not a coffee"

    def test_price_property(self, sample_customer, sample_coffee):
        # Test price property getter
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order.price == 3.5

    def test_price_property_setter_valid(self, sample_customer, sample_coffee):
        # Test price property setter with valid price
        order = Order(sample_customer, sample_coffee, 3.5)
        order.price = 4.0
        assert order.price == 4.0

    def test_price_property_setter_invalid_type(self, sample_customer, sample_coffee):
        # Test price property setter with invalid price type
        order = Order(sample_customer, sample_coffee, 3.5)
        with pytest.raises(TypeError):
            order.price = "4.0"

    def test_price_property_setter_invalid_range(self, sample_customer, sample_coffee):
        # Test price property setter with invalid price range
        order = Order(sample_customer, sample_coffee, 3.5)
        with pytest.raises(ValueError):
            order.price = 0.5  # Too low
        with pytest.raises(ValueError):
            order.price = 15.0  # Too high

    def test_relationship_with_customer(self, sample_customer, sample_coffee):
        # Test relationship with customer
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order in sample_customer.orders()

    def test_relationship_with_coffee(self, sample_customer, sample_coffee):
        # Test relationship with coffee
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order in sample_coffee.orders()
