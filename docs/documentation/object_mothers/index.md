# Object Mothers

This document provides a comprehensive overview of the Object Mother pattern implementation 
in the `sindri` library. 

For detailed information on object mother functionality, see:

- [Built-in object mothers](built_in_mothers.md)
- [Creating custom object mothers](customizing_mothers.md)

For creating value objects with domain-specific validation, see [Value Objects](../value_objects/index.md).

## Pattern Overview

The Object Mother pattern is a testing design pattern that provides a centralized way to create test data objects
with predefined or random values. It simplifies test setup by encapsulating the creation logic of complex objects
and their dependencies, making tests more readable and maintainable.

Object mothers are characterized by:

- **Centralized creation logic**: All test data generation is consolidated in dedicated mother classes
- **Reusability**: Common test scenarios can be shared across multiple test suites
- **Flexibility**: Support for generating random or specific test values
- **Readability**: Named factory methods that express test intent clearly
- **Maintainability**: Changes to object creation logic are isolated to mother classes

In this implementation, all object mothers inherit from the `ObjectMother` base class, 
which provides access to the Faker library for generating realistic test data.

## Base Object Mother Class

The `ObjectMother` base class provides core functionality for all object mothers in the library:

| Feature            | Description                                        | Implementation                     |
|--------------------|----------------------------------------------------|-----------------------------------|
| Faker Integration  | Access to Faker library for data generation       | `_faker()` class method           |
| Consistent API     | Uniform interface across all mother classes       | Class method pattern              |
| No Weighting       | Predictable random generation without bias        | `Faker(use_weighting=False)`      |
| Extensibility      | Easy to subclass for custom test data generators  | Minimal base implementation       |

!!! note "Subclassing"
    The `ObjectMother` class is designed to be subclassed for specific test data generators.
    It provides direct access to Faker for creating realistic test data.

## Object Mother Features

### Faker Integration

Object mothers leverage the [Faker](https://faker.readthedocs.io/) library to generate realistic test data:

- Each mother class has access to a Faker instance through the `_faker()` class method
- Faker is configured with `use_weighting=False` for consistent, predictable random generation
- This ensures reproducible test data across test runs when using the same random seed

### Class Method Pattern

All object mothers use class methods for data generation:

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

### Primitive vs. Value Object Mothers

The library provides two categories of object mothers:

1. **Primitive Mothers**: Generate raw Python primitive values (`str`, `int`, `float`, `bool`, `list`)
2. **Value Object Mothers**: Can be created to generate domain-specific value objects

Primitive mothers are useful for:

- Creating test data for primitive types
- Feeding values into value object constructors
- Testing validation logic in value objects

```python
from object_mother import IntegerPrimitivesMother
from value_objects import Integer

# Using primitive mother to create raw values
raw_age = IntegerPrimitivesMother.positive()

# Using primitive mother with value objects
age = Integer(IntegerPrimitivesMother.positive())
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

