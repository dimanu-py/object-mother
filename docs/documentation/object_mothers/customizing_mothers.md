# Customizing Object Mothers

To create domain-specific object mothers for your tests, extend the `ObjectMother` base class or one of the 
[built-in primitive mothers](built_in_mothers.md). Custom mothers help you generate test data that reflects your 
domain concepts and reduces duplication across your test suites.

## Creating Object Mothers through Subclassing

The main goal for creating custom object mothers is to encapsulate test data generation logic and
express the ubiquitous language of your domain in your tests.

### Extending ObjectMother

The simplest way to create custom object mothers is by subclassing the `ObjectMother` base class:

```python
from object_mother import ObjectMother


class UserMother(ObjectMother):
    @classmethod
    def any(cls) -> dict:
        faker = cls._faker()
        return {
            "username": faker.user_name(),
            "email": faker.email(),
            "age": faker.random_int(min=18, max=100)
        }

    @classmethod
    def adult(cls) -> dict:
        faker = cls._faker()
        return {
            "username": faker.user_name(),
            "email": faker.email(),
            "age": faker.random_int(min=18, max=65)
        }

    @classmethod
    def minor(cls) -> dict:
        faker = cls._faker()
        return {
            "username": faker.user_name(),
            "email": faker.email(),
            "age": faker.random_int(min=1, max=17)
        }
```

This mother can now be used in your tests to generate user test data:

```python
user_data = UserMother.any()
adult_user = UserMother.adult()
minor_user = UserMother.minor()
```

### Extending Primitive Mothers

You can also extend existing primitive mothers to add domain-specific generation methods:

```python
from object_mother import StringPrimitivesMother


class EmailMother(StringPrimitivesMother):
    @classmethod
    def valid(cls) -> str:
        """Generate a valid email address."""
        return cls._faker().email()

    @classmethod
    def with_domain(cls, domain: str) -> str:
        """Generate an email with a specific domain."""
        username = cls._faker().user_name()
        return f"{username}@{domain}"

    @classmethod
    def invalid(cls) -> str:
        """Generate an invalid email (missing @ symbol)."""
        return cls._faker().word() + cls._faker().word()
```

## Creating Mothers for Value Objects

When working with [value objects](../value_objects/index.md), you can create mothers that generate
value object instances directly:

```python
from object_mother import ObjectMother
from value_objects import String, Integer


class Email(String):
    """A value object representing an email address."""
    pass


class Age(Integer):
    """A value object representing a person's age."""
    pass


class EmailMother(ObjectMother):
    @classmethod
    def any(cls) -> Email:
        """Generate any valid email value object."""
        return Email(cls._faker().email())

    @classmethod
    def with_domain(cls, domain: str) -> Email:
        """Generate an email with a specific domain."""
        username = cls._faker().user_name()
        return Email(f"{username}@{domain}")


class AgeMother(ObjectMother):
    @classmethod
    def any(cls) -> Age:
        """Generate any valid age."""
        return Age(cls._faker().random_int(min=0, max=120))

    @classmethod
    def adult(cls) -> Age:
        """Generate an adult age (18+)."""
        return Age(cls._faker().random_int(min=18, max=100))

    @classmethod
    def child(cls) -> Age:
        """Generate a child age (0-17)."""
        return Age(cls._faker().random_int(min=0, max=17))
```

These mothers can be used in tests to create value objects with appropriate test data:

```python
email = EmailMother.any()
corporate_email = EmailMother.with_domain("company.com")
person_age = AgeMother.adult()
```

## Creating Mothers for Complex Objects

For more complex domain objects or aggregates, you can create mothers that handle the entire
object graph:

```python
from object_mother import ObjectMother, StringPrimitivesMother, IntegerPrimitivesMother
from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    postal_code: str


@dataclass
class Person:
    name: str
    age: int
    address: Address


class AddressMother(ObjectMother):
    @classmethod
    def any(cls) -> Address:
        faker = cls._faker()
        return Address(
            street=faker.street_address(),
            city=faker.city(),
            postal_code=faker.postcode()
        )


class PersonMother(ObjectMother):
    @classmethod
    def any(cls) -> Person:
        faker = cls._faker()
        return Person(
            name=faker.name(),
            age=faker.random_int(min=1, max=100),
            address=AddressMother.any()
        )

    @classmethod
    def with_age(cls, age: int) -> Person:
        """Generate a person with a specific age."""
        faker = cls._faker()
        return Person(
            name=faker.name(),
            age=age,
            address=AddressMother.any()
        )

    @classmethod
    def with_address(cls, address: Address) -> Person:
        """Generate a person with a specific address."""
        faker = cls._faker()
        return Person(
            name=faker.name(),
            age=faker.random_int(min=1, max=100),
            address=address
        )
```

## Composing Mothers

Object mothers can be composed to create more complex test scenarios:

```python
from object_mother import ObjectMother


class OrderMother(ObjectMother):
    @classmethod
    def any(cls):
        faker = cls._faker()
        return {
            "order_id": faker.uuid4(),
            "customer": PersonMother.any(),
            "items": [ItemMother.any() for _ in range(faker.random_int(min=1, max=5))],
            "total": faker.pyfloat(positive=True, min_value=10, max_value=1000)
        }

    @classmethod
    def with_customer(cls, customer):
        faker = cls._faker()
        return {
            "order_id": faker.uuid4(),
            "customer": customer,
            "items": [ItemMother.any() for _ in range(faker.random_int(min=1, max=5))],
            "total": faker.pyfloat(positive=True, min_value=10, max_value=1000)
        }
```

## Best Practices

When creating custom object mothers, follow these best practices:

### Use Descriptive Names

Name your factory methods to clearly express their purpose:

```python
# Good
class UserMother(ObjectMother):
    @classmethod
    def active(cls): ...
    
    @classmethod
    def suspended(cls): ...
    
    @classmethod
    def with_verified_email(cls): ...

# Avoid
class UserMother(ObjectMother):
    @classmethod
    def type1(cls): ...
    
    @classmethod
    def type2(cls): ...
```

### Provide Flexibility

Allow customization of generated data when needed:

```python
class ProductMother(ObjectMother):
    @classmethod
    def any(cls, price: float | None = None, name: str | None = None):
        faker = cls._faker()
        return {
            "name": name or faker.word(),
            "price": price or faker.pyfloat(positive=True, min_value=1, max_value=1000),
            "description": faker.text()
        }
```

### Keep Methods Focused

Each factory method should have a single, clear purpose:

```python
class AccountMother(ObjectMother):
    @classmethod
    def with_positive_balance(cls):
        """Generate an account with a positive balance."""
        ...
    
    @classmethod
    def with_negative_balance(cls):
        """Generate an account with a negative balance."""
        ...
    
    @classmethod
    def with_zero_balance(cls):
        """Generate an account with zero balance."""
        ...
```

### Leverage Faker Capabilities

Take advantage of Faker's rich set of providers:

```python
class ArticleMother(ObjectMother):
    @classmethod
    def any(cls):
        faker = cls._faker()
        return {
            "title": faker.sentence(),
            "content": faker.text(max_nb_chars=500),
            "author": faker.name(),
            "published_date": faker.date_time_this_year(),
            "tags": faker.words(nb=3),
            "url": faker.url()
        }
```

!!! tip "Reusability"
    Design your mothers to be reusable across different test suites. Avoid coupling them 
    to specific test scenarios or assertions.

