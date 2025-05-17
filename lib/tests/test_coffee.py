import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture
def sample_coffee():
    return Coffee("Espresso")

@pytest.fixture
def sample_customer():
    return Customer("Alice")

class TestCoffee:
    def test_init_valid_name(self):
        # Test initialization with valid name
        coffee = Coffee("Latte")
        assert coffee.name == "Latte"
        assert coffee in Coffee.all_coffees

    def test_init_invalid_name_type(self):
        # Test initialization with invalid name type
        with pytest.raises(TypeError):
            Coffee(123)

    def test_init_invalid_name_length(self):
        # Test initialization with too short name
        with pytest.raises(ValueError):
            Coffee("XY")  # Less than 3 characters

    def test_name_property(self, sample_coffee):
        # Test name property getter
        assert sample_coffee.name == "Espresso"

    def test_name_property_setter_valid(self, sample_coffee):
        # Test name property setter with valid name
        sample_coffee.name = "Americano"
        assert sample_coffee.name == "Americano"

    def test_name_property_setter_invalid(self, sample_coffee):
        # Test name property setter with invalid name
        with pytest.raises(ValueError):
            sample_coffee.name = "XY"  # Too short

    def test_orders_empty(self, sample_coffee):
        # Test orders method with no orders
        assert sample_coffee.orders() == []

    def test_orders_with_orders(self, sample_coffee, sample_customer):
        # Test orders method with orders
        order = Order(sample_customer, sample_coffee, 3.5)
        assert order in sample_coffee.orders()
        assert len(sample_coffee.orders()) == 1

    def test_customers_empty(self, sample_coffee):
        # Test customers method with no orders
        assert sample_coffee.customers() == []

    def test_customers_with_orders(self, sample_coffee):
        # Test customers method with orders
        customer1 = Customer("Bob")
        customer2 = Customer("Charlie")
        
        Order(customer1, sample_coffee, 3.5)
        Order(customer2, sample_coffee, 4.0)
        Order(customer1, sample_coffee, 3.5)  # Duplicate customer to test uniqueness
        
        customers = sample_coffee.customers()
        assert len(customers) == 2
        assert customer1 in customers
        assert customer2 in customers

    def test_num_orders_empty(self, sample_coffee):
        # Test num_orders method with no orders
        assert sample_coffee.num_orders() == 0

    def test_num_orders_with_orders(self, sample_coffee, sample_customer):
        # Test num_orders method with orders
        Order(sample_customer, sample_coffee, 3.5)
        Order(sample_customer, sample_coffee, 4.0)
        
        assert sample_coffee.num_orders() == 2

    def test_average_price_no_orders(self, sample_coffee):
        # Test average_price method with no orders
        assert sample_coffee.average_price() == 0

    def test_average_price_with_orders(self, sample_coffee, sample_customer):
        # Test average_price method with orders
        Order(sample_customer, sample_coffee, 3.0)
        Order(sample_customer, sample_coffee, 5.0)
        
        # Average should be (3.0 + 5.0) / 2 = 4.0
        assert sample_coffee.average_price() == 4.0
