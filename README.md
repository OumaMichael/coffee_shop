# Coffee Shop Domain Model

## Overview

This project implements a comprehensive domain model for a Coffee Shop using object-oriented programming principles in Python. The model consists of three main entities: `Customer`, `Coffee`, and `Order`, with well-defined relationships between them.

### Domain Relationships

- A `Customer` can place many `Orders`
- A `Coffee` can have many `Orders`
- An `Order` belongs to one `Customer` and one `Coffee`
- `Customer` and `Coffee` have a many-to-many relationship through `Order`

## Installation

### Prerequisites

- Python 3.7 or higher
- pipenv (for virtual environment management)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/OumaMichael/coffee_shop
   cd coffee_shop
   ```

2. Create and activate a virtual environment:
   ```bash
   pipenv install
   pipenv shell
   ```

3. Install development dependencies:
   ```bash
   pipenv install pytest
   ```

## Class Documentation

### Customer Class

The `Customer` class represents a coffee shop customer.

#### Attributes:
- `name`: String between 1-15 characters
- `_orders`: Private list of Order instances

#### Methods:
- `orders()`: Returns a list of all Order instances for this customer
- `coffees()`: Returns a unique list of Coffee instances ordered by this customer
- `create_order(coffee, price)`: Creates a new Order for this customer
- `most_aficionado(coffee)` (class method): Returns the Customer who spent the most on a specific coffee

```bash
customer = Customer("Alice")
coffee = Coffee("Espresso")
order = customer.create_order(coffee, 3.5)
```

### Coffee Class

The `Coffee` class represents a type of coffee available in the shop.

#### Attributes:
- `name`: String at least 3 characters long
- `_orders`: Private list of Order instances

#### Methods:
- `orders()`: Returns a list of all Order instances for this coffee
- `customers()`: Returns a unique list of Customer instances who ordered this coffee
- `num_orders()`: Returns the total number of times this coffee has been ordered
- `average_price()`: Returns the average price of this coffee based on its orders

#### Example:
```bash
coffee = Coffee("Latte")
customers = coffee.customers()
avg_price = coffee.average_price()
```
The `Order` class represents a purchase of a coffee by a customer.

#### Attributes:
- `customer`: Reference to a Customer instance
- `coffee`: Reference to a Coffee instance
- `price`: Float between 1.0 and 10.0

#### Validation:
- Customer must be a Customer instance
- Coffee must be a Coffee instance
- Price must be a number between 1.0 and 10.0

#### Example:
```bash
order = Order(customer, coffee, 4.5)
```

## Usage Examples
```bash
order = Order(customer, coffee, 4.5)
from customer import Customer
from coffee import Coffee
from order import Order
```

# Create customers and coffees
```bash
alice = Customer("Alice")
bob = Customer("Bob")
espresso = Coffee("Espresso")
from customer import Customer
from coffee import Coffee
from order import Order
```

# Create customers and coffees
```bash
alice = Customer("Alice")
bob = Customer("Bob")
espresso = Coffee("Espresso")
latte = Coffee("Latte")
```
# Create orders
```bash
alice.create_order(espresso, 3.5)
alice.create_order(latte, 4.5)
bob.create_order(espresso, 3.0)
```
# Get all coffees ordered by Alice
```bash
alice_coffees = alice.coffees()
print([coffee.name for coffee in alice_coffees])  # ['Espresso', 'Latte']
```

# Get average price of Espresso
```bash
avg_price = espresso.average_price()
print(f"Average Espresso price: ${avg_price:.2f}")
```

# Find the biggest Espresso aficionado
```bash
aficionado = Customer.most_aficionado(espresso)
print(f"Biggest Espresso fan: {aficionado.name}")
```

## Testing

### Running Tests


To run all tests:

```bash
python debug.py
pytest -v
```

To run tests for a specific class:
```bash
pytest
```
### Test Coverage

The test suite provides comprehensive coverage of:
- Initialization with valid and invalid parameters
- Property getters and setters
- Methods for creating orders and getting coffees

```bash
pytest -v
```

## Validation Rules

The domain model enforces the following validation rules:

```bash
pytest tests/test_customer.py
```

2. **Coffee**:
   - Name must be a string
   - Name must be at least 3 characters long

3. **Order**:
   - Customer must be a Customer instance
   - Coffee must be a Coffee instance
   - Price must be a number between 1.0 and 10.0

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request


## License

This project is licensed under the MIT License - see the LICENSE file for details.
