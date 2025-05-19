# tests/test_coffee.py
import pytest
from coffee import Coffee
from customer import Customer
from order import Order

@pytest.fixture(autouse=True)
def clear_coffees():
    # Clear class-level state before each test
    Coffee.all_coffees.clear()
    yield
    Coffee.all_coffees.clear()

def test_coffee_creation_and_registry():
    c = Coffee("Mocha")
    assert c.name == "Mocha"
    assert c in Coffee.all_coffees

def test_name_setter_validates_type_and_length():
    with pytest.raises(TypeError):
        Coffee(123)            # non-string name
    with pytest.raises(ValueError):
        Coffee("ab")           # too short

def test_orders_and_num_orders_and_average_price():
    cust = Customer("TestUser")
    coffee = Coffee("Latte")
    # no orders yet
    assert coffee.orders() == []
    assert coffee.num_orders() == 0
    assert coffee.average_price() == 0
    
    # place some orders
    o1 = Order(cust, coffee, 3.0)
    o2 = Order(cust, coffee, 4.0)
    assert coffee.orders() == [o1, o2]
    assert coffee.num_orders() == 2
    assert pytest.approx(coffee.average_price(), rel=1e-3) == 3.5

def test_customers_returns_unique_list():
    alice = Customer("Alice")
    bob = Customer("Bob")
    coffee = Coffee("Espresso")
    o1 = Order(alice, coffee, 3.5)
    o2 = Order(bob, coffee, 3.0)
    o3 = Order(alice, coffee, 3.5)
    names = sorted(c.name for c in coffee.customers())
    assert names == ["Alice", "Bob"]
