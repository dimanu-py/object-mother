Once you have [installed the package], you can start generating test data using object mothers.

## Your First Object Mother

The `object-mother-sindri` package provides a set of built-in object mothers that you 
can use to generate realistic test data. To create your first object mother, follow these steps:

1. First import the object mother classes you want to use from the `object_mother` module.
2. Then use the `any()` method of the object mother to generate a random primitive value
3. Finally, you can use the generated values in your tests.

```python
from object_mother import IntegerPrimitivesMother, StringPrimitivesMother

def test_user_creation() -> None:
    user_request = {
        "age": IntegerPrimitivesMother.any(),
        "name": StringPrimitivesMother.any()
    }
    ...
```

!!! tip "More about Object Mothers"
    Object mothers has a lot more to offer too. You can learn more about the object mother pattern, the built-in object 
    mothers that are implemented, what methods they provide, and how to extend or create your custom object mothers in the 
    [Object Mothers] section.

[installed the package]: installation.md
[Object Mothers]: ../object_mothers/index.md
