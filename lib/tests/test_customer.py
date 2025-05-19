# tests/test_customer.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_state():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()
    yield
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_customer_creation_and_registry():
    c = Customer("Charlie")
    assert c.name == "Charlie"
    assert c in Customer.all_customers

def test_name_setter_validates_type_and_length():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")      # too short
    with pytest.raises(ValueError):
        Customer("x"*16)  # too long

def test_create_order_links_objects():
    cust = Customer("Dana")
    coffee = Coffee("Americano")
    order = cust.create_order(coffee, 5.0)
    # order should be in both sides
    assert order in cust.orders()
    assert order in coffee.orders()

def test_coffees_returns_unique_list():
    cust = Customer("Eve")
    c1 = Coffee("Flat White")
    c2 = Coffee("Filter")
    Order(cust, c1, 4.0)
    Order(cust, c2, 4.5)
    Order(cust, c1, 4.0)
    names = sorted(coffee.name for coffee in cust.coffees())
    assert names == ["Filter", "Flat White"]

def test_most_aficionado():
    alice = Customer("Alice")
    bob = Customer("Bob")
    espresso = Coffee("Espresso")
    # no orders yet
    assert Customer.most_aficionado(espresso) is None
    # orders
    Order(alice, espresso, 3.5)
    Order(bob, espresso, 4.0)
    Order(alice, espresso, 3.5)
    # Alice spent 7.0, Bob 4.0
    top = Customer.most_aficionado(espresso)
    assert top is alice
