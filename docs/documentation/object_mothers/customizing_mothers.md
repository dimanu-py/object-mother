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
    def any(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=faker.random_int(min=18, max=100)
        )

    @classmethod
    def adult(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=30
        )

    @classmethod
    def under_age(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=5
        )
```

This mother can now be used in your tests to generate user test data:

```python
user = UserMother.any()
adult = UserMother.adult()
under_age = UserMother.under_age()
```

Another common approach is to create specific mothers for different concepts of the same class:

```python
from object_mother import ObjectMother


class GeneralUserMother(ObjectMother):
    @classmethod
    def any(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=faker.random_int(min=18, max=100)
        )

class UserByAgeMother(ObjectMother):

    @classmethod
    def adult(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=30
        )

    @classmethod
    def under_age(cls) -> User:
        faker = cls._faker()
        return User(
            username=faker.user_name(),
            email=faker.email(),
            age=5
        )
```

This way it's easier to find the right mother for the right scenario and avoid having a single mother with too many methods.

### Extending Primitive Mothers

You can also extend existing primitive mothers to add domain-specific generation methods:

```python
from object_mother import StringPrimitivesMother


class UserEmailMother(StringPrimitivesMother):
    @classmethod
    def valid(cls) -> UserEmail:
        """Generate a valid email address."""
        return UserEmail(cls._faker().email())

    @classmethod
    def with_domain(cls, domain: str) -> UserEmail:
        """Generate an email with a specific domain."""
        username = cls._faker().user_name()
        return UserEmail(f"{username}@{domain}")
```

### Composing Mothers

Object mothers can be composed to create more complex test scenarios:

```python
from object_mother import ObjectMother


class OrderMother(ObjectMother):
    @classmethod
    def any(cls) -> Order:
        faker = cls._faker()
        return Order(
            order_id=faker.uuid4(),
            customer=PersonMother.any(),
            items=[ItemMother.any() for _ in range(3)],
            total=250
        )

    @classmethod
    def with_products(cls, quantity: int) -> Order:
        faker = cls._faker()
        return Order(
            order_id=faker.uuid4(),
            customer=PersonMother.any(),
            items=[ItemMother.any() for _ in range(quantity)],
            total=250
        )
```

## Best Practices

When creating custom object mothers, follow these best practices:

### Use Descriptive Names

Name your factory methods to clearly express the business purpose:

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
    def status1(cls): ...
    
    @classmethod
    def status2(cls): ...
```

### Keep Methods Focused

Each factory method should have a single, clear purpose. Avoid methods that admit too much variability or that allows
parameters that can generate a wide range of scenarios. If you need more flexibility, consider creating multiple methods 
instead of one with parameters:

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

### Separate Concerns

If your object mother grows too large or has too many methods, consider splitting it into multiple mothers that focus on 
different aspects of the domain:

```python
class UserMother(ObjectMother):
    @classmethod
    def any(cls) -> User: ...
    
class UserByStatusMother(ObjectMother):
    @classmethod
    def active(cls) -> User: ...
    
    @classmethod
    def suspended(cls) -> User: ...
```

### Leverage Faker Capabilities

Take advantage of Faker's rich set of providers when the value is really not relevant and does not affect the result of the test

```python
class ArticleMother(ObjectMother):
    @classmethod
    def any(cls):
        faker = cls._faker()
        return Article(
            title=faker.sentence(),
            content=faker.text(max_nb_chars=500),
            author=faker.name(),
            published_date=faker.date_time_this_year(),
            tags=faker.words(nb=3),
            url=faker.url()
        )
```
