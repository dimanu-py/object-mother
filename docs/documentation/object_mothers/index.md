# Object Mothers

This document provides a comprehensive overview of the Object Mother pattern implementation 
in the `object-mother-sindri` library. 

For detailed information on object mother functionality, see:

- [Built-in object mothers](built_in_mothers.md)
- [Creating custom object mothers](customizing_mothers.md)

## Pattern Overview

The Object Mother pattern is a testing design pattern that provides a centralized way to generate example objects
ina consistent way, while making it easy to show what characterizes each test.
In one test, we might not care about the specific values of an object, but in another test, we might want to clearly
represent a particular scenario by expressing it in business terms.
Therefore, we can say that the main purpose of a mother is to generate object prototypes for tests, giving them 
business meaning. A mother is not an arbitrary factory for building any business object with specific values; that 
is what the Builder Pattern is for.

Let's say we have a `Subscription` class in our domain. In our tests is not the same to create a subscriptions as:

```python
subscription = Subscription(
    plan="basic",
    status="active",
    renewal_date=datetime(2024, 12, 31)
)
```

Than to create it as:

```python
subscription = SubscriptionMother.active_basic_plan()

class SubscriptionMother(ObjectMother):
    @classmethod
    def active_basic_plan(cls) -> Subscription:
        return Subscription(
            plan="basic",
            status="active",
            renewal_date=cls._faker().date_between(start_date="today", end_date="+1y")
        )
```

In the first example, we don’t know what is the important part of the subscription for the test, while in the second example, we can 
clearly see that we are creating an active subscription with a basic plan, and the renewal date is not relevant for the test.

Object mothers are characterized by:

- **Centralized creation logic**: All test data generation is consolidated in dedicated mother classes
- **Domain relevance**: Mothers generate objects that are meaningful within the context of the domain being tested
- **Reusability**: Common test scenarios can be shared across multiple test suites
- **Flexibility**: Support for generating random or specific test values
- **Readability**: Named factory methods that express test intent clearly
- **Maintainability**: Changes to object creation logic are isolated to mother classes

In this implementation, all object mothers inherit from the `ObjectMother` base class, 
which provides access to the Faker library for generating realistic test data.

## Base Object Mother Class

The `ObjectMother` base class provides core functionality for all object mothers in the library:

| Feature           | Description                                      | Implementation               |
|-------------------|--------------------------------------------------|------------------------------|
| Faker Integration | Access to Faker library for data generation      | `_faker()` class method      |
| Consistent API    | Uniform interface across all mother classes      | Class method pattern         |
| No Weighting      | Predictable random generation without bias       | `Faker(use_weighting=False)` |
| Extensibility     | Easy to subclass for custom test data generators | Minimal base implementation  |

!!! note "Subclassing"
    The `ObjectMother` class is designed to be subclassed for specific test data generators.
    It provides direct access to Faker for creating realistic test data.

## Object Mother Features

### Faker Integration

Object mothers leverage the [Faker](https://faker.readthedocs.io/) library to generate realistic test data:

- Each mother class has access to a Faker instance through the `_faker()` class method
- Faker is configured with `use_weighting=False` for consistent, predictable random generation
- This ensures reproducible test data across test runs when using the same random seed

!!! important "Random values in tests"
    Even we expose this API to generate random values, we don't recommend using random values in tests, specially in deterministic scenarios
where we need deterministic results. By using random values in these cases, we can end up with flaky tests or make tests too complex.

### Class Method Pattern

All object mothers use class methods for data generation that act as named factory methods:

- No need to instantiate mother objects
- Methods can be called directly on the class
- Clean and concise test code

```python
from object_mother import StringPrimitivesMother

username = StringPrimitivesMother.any()
```

### Named Factory Methods

Object mothers provide descriptive factory methods that clearly express intent:

- `any()`: Generate any valid random value
- `empty()`: Generate empty values (for strings, lists, etc.)
- `positive()`, `negative()`: Generate values with specific characteristics
- Custom methods for domain-specific scenarios

This naming convention makes tests self-documenting and easy to understand.

### Primitive Mothers

The library provides primitive mothers that generate raw Python primitive values (`str`, `int`, `float`, `bool`, `list`).

Primitive mothers are useful for:

- Creating test data for primitive types
- Feeding values into constructors or functions

```python
from object_mother import IntegerPrimitivesMother

# Using primitive mother to create raw values
raw_age = IntegerPrimitivesMother.positive()
```

### Testing with Object Mothers

Object mothers are primarily designed for use in testing scenarios:

- **Unit Tests**: Generate test data for isolated component testing
- **Integration Tests**: Create complex object graphs for integration scenarios
- **Property-Based Testing**: Generate random inputs for property tests
- **Test Fixtures**: Provide consistent test data across test suites

!!! warning "Production Use"
    Object mothers are intended for testing purposes only. They should not be used 
    in production code for data generation or as part of the application's business logic.

