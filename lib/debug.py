from customer import Customer
from coffee import Coffee
from order import Order

# Create some customers
print("Creating customers...")
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")
print(f"Created customers: {alice.name}, {bob.name}, {charlie.name}")

# Create some coffees
print("\nCreating coffees...")
espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")
print(f"Created coffees: {espresso.name}, {latte.name}, {cappuccino.name}")

# Create some orders
print("\nCreating orders...")
order1 = alice.create_order(espresso, 3.5)
order2 = alice.create_order(latte, 4.5)
order3 = bob.create_order(espresso, 3.0)
order4 = bob.create_order(cappuccino, 5.0)
order5 = charlie.create_order(latte, 4.0)
order6 = alice.create_order(espresso, 3.5)
print("Orders created successfully")

# Test Customer methods
print("\nTesting Customer methods...")
print(f"Alice's orders: {len(alice.orders())}")
print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")

# Test Coffee methods
print("\nTesting Coffee methods...")
print(f"Espresso orders: {espresso.num_orders()}")
print(f"Espresso customers: {[customer.name for customer in espresso.customers()]}")
print(f"Espresso average price: ${espresso.average_price():.2f}")

# Test most_aficionado class method
print("\nTesting most_aficionado method...")
espresso_aficionado = Customer.most_aficionado(espresso)
latte_aficionado = Customer.most_aficionado(latte)
print(f"Biggest Espresso aficionado: {espresso_aficionado.name}")
print(f"Biggest Latte aficionado: {latte_aficionado.name}")

# Test validation
print("\nTesting validation...")
try:
    invalid_customer = Customer("")
except ValueError as e:
    print(f"Validation error (expected): {e}")

try:
    invalid_coffee = Coffee("XY")
except ValueError as e:
    print(f"Validation error (expected): {e}")

try:
    invalid_order = Order(alice, espresso, 15.0)
except ValueError as e:
    print(f"Validation error (expected): {e}")

print("\nAll tests completed successfully!")
