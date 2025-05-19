# tests/test_order.py
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()
    yield
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_order_creation_and_registry_and_linking():
    cust = Customer("Frank")
    coffee = Coffee("Cappuccino")
    o = Order(cust, coffee, 4.5)
    # class registry
    assert o in Order.all_orders
    # linked to customer and coffee
    assert o in cust.orders()
    assert o in coffee.orders()

def test_customer_setter_validation():
    cust = Customer("Gina")
    coffee = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order("not a customer", coffee, 3.0)

def test_coffee_setter_validation():
    cust = Customer("Hank")
    coffee = Coffee("Ristretto")
    with pytest.raises(TypeError):
        Order(cust, "not a coffee", 3.0)

def test_price_setter_validation():
    cust = Customer("Ivan")
    coffee = Coffee("Macchiato")
    with pytest.raises(TypeError):
        Order(cust, coffee, "free")
    with pytest.raises(ValueError):
        Order(cust, coffee, 0.5)    # below minimum
    with pytest.raises(ValueError):
        Order(cust, coffee, 15.0)   # above maximum

def test_price_getter_returns_float():
    cust = Customer("Jane")
    coffee = Coffee("Mocha")
    o = Order(cust, coffee, 5)
    assert isinstance(o.price, float)
    assert o.price == 5.0
