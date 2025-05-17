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

class TestCustomer:
    def test_init_valid_name(self):
        # Test initialization with valid name
        customer = Customer("Bob")
        assert customer.name == "Bob"
        assert customer in Customer.all_customers

    def test_init_invalid_name_type(self):
        # Test initialization with invalid name type
        with pytest.raises(TypeError):
            Customer(123)

    def test_init_invalid_name_length_short(self):
        # Test initialization with empty name
        with pytest.raises(ValueError):
            Customer("")

    def test_init_invalid_name_length_long(self):
        # Test initialization with too long name
        with pytest.raises(ValueError):
            Customer("ThisNameIsTooLongForTheSystem")

    def test_name_property(self, sample_customer):
        # Test name property getter
        assert sample_customer.name == "Alice"

    def test_name_property_setter_valid(self, sample_customer):
        # Test name property setter with valid name
        sample_customer.name = "Alex"
        assert sample_customer.name == "Alex"

    def test_name_property_setter_invalid(self, sample_customer):
        # Test name property setter with invalid name
        with pytest.raises(ValueError):
            sample_customer.name = ""

    def test_orders_empty(self, sample_customer):
        # Test orders method with no orders
        assert sample_customer.orders() == []

    def test_orders_with_orders(self, sample_customer, sample_coffee):
        # Test orders method with orders
        order = sample_customer.create_order(sample_coffee, 3.5)
        assert order in sample_customer.orders()
        assert len(sample_customer.orders()) == 1

    def test_coffees_empty(self, sample_customer):
        # Test coffees method with no orders
        assert sample_customer.coffees() == []

    def test_coffees_with_orders(self, sample_customer):
        # Test coffees method with orders
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Cappuccino")
        
        sample_customer.create_order(coffee1, 4.0)
        sample_customer.create_order(coffee2, 4.5)
        sample_customer.create_order(coffee1, 4.0)  # Duplicate coffee to test uniqueness
        
        coffees = sample_customer.coffees()
        assert len(coffees) == 2
        assert coffee1 in coffees
        assert coffee2 in coffees

    def test_create_order(self, sample_customer, sample_coffee):
        # Test create_order method
        order = sample_customer.create_order(sample_coffee, 3.5)
        
        assert order.customer == sample_customer
        assert order.coffee == sample_coffee
        assert order.price == 3.5
        assert order in sample_customer.orders()
        assert order in sample_coffee.orders()

    def test_most_aficionado_no_orders(self):
        # Test most_aficionado with no orders
        coffee = Coffee("Mocha")
        assert Customer.most_aficionado(coffee) is None

    def test_most_aficionado_with_orders(self):
        # Test most_aficionado with orders
        # Reset class variables to avoid interference from other tests
        Customer.all_customers = []
        Coffee.all_coffees = []
        Order.all_orders = []
        
        # Create test data
        alice = Customer("Alice")
        bob = Customer("Bob")
        charlie = Customer("Charlie")
        
        coffee = Coffee("Espresso")
        
        # Alice spends $7 total on Espresso
        alice.create_order(coffee, 3.5)
        alice.create_order(coffee, 3.5)
        
        # Bob spends $3 total on Espresso
        bob.create_order(coffee, 3.0)
        
        # Charlie spends $10 total on Espresso (should be the aficionado)
        charlie.create_order(coffee, 5.0)
        charlie.create_order(coffee, 5.0)
        
        # Test the method
        aficionado = Customer.most_aficionado(coffee)
        assert aficionado == charlie
