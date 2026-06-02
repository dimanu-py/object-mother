# Built-in Object Mothers

The library provides several built-in object mother classes for generating test data.

All primitive object mothers inherit from the [`ObjectMother`](index.md#base-object-mother-class) base class and 
provide class methods for generating various types of test data. Each mother class is specialized for a specific 
Python primitive type and offers methods for common testing scenarios.

!!! note "Each object mother type can be [extended and customized as needed](customizing_mothers.md)."

## BooleanPrimitivesMother

The `BooleanPrimitivesMother` class generates boolean test data for testing scenarios requiring `bool` values.

| Method     | Description                                                    | Returns |
|------------|----------------------------------------------------------------|---------|
| `any()`    | Generate any random boolean value (True or False)              | `bool`  |
| `true()`   | Generate the `True` boolean value                              | `bool`  |
| `false()`  | Generate the `False` boolean value                             | `bool`  |

```python
from object_mother import BooleanPrimitivesMother

random_flag = BooleanPrimitivesMother.any()  # True or False
active_flag = BooleanPrimitivesMother.true()  # True
inactive_flag = BooleanPrimitivesMother.false()  # False
```

## IntegerPrimitivesMother

The `IntegerPrimitivesMother` class generates integer test data for testing scenarios requiring `int` values.

| Method                                              | Description                                             | Returns |
|-----------------------------------------------------|---------------------------------------------------------|---------|
| `any()`                                             | Generate any random integer value                       | `int`   |
| `positive()`                                        | Generate a positive integer value (> 0)                 | `int`   |
| `negative()`                                        | Generate a negative integer value (< 0)                 | `int`   |
| `zero()`                                            | Generate zero as an integer                             | `int`   |


```python
from object_mother import IntegerPrimitivesMother

random_number = IntegerPrimitivesMother.any()  # Random integer
age = IntegerPrimitivesMother.positive()  # Always > 0
debt = IntegerPrimitivesMother.negative()  # Always < 0
balance = IntegerPrimitivesMother.zero()  # 0
```

## FloatPrimitivesMother

The `FloatPrimitivesMother` class generates floating-point test data for testing scenarios requiring `float` values.

| Method                                                  | Description                                       | Returns |
|---------------------------------------------------------|---------------------------------------------------|---------|
| `any()`                                                 | Generate any random float value                   | `float` |
| `positive()`                                            | Generate a positive float value (≥ 0.1)           | `float` |
| `negative()`                                            | Generate a negative float value (≤ -0.1)          | `float` |
| `zero()`                                                | Generate zero as a float (0.0)                    | `float` |

```python
from object_mother import FloatPrimitivesMother

random_decimal = FloatPrimitivesMother.any()  # Random float
price = FloatPrimitivesMother.positive()  # Always > 0
loss = FloatPrimitivesMother.negative()  # Always < 0
balance = FloatPrimitivesMother.zero()  # 0.0
```

## StringPrimitivesMother

The `StringPrimitivesMother` class generates string test data for testing scenarios requiring `str` values.

| Method                            | Description                                                           | Returns |
|-----------------------------------|-----------------------------------------------------------------------|---------|
| `any()`                           | Generate any random string value (single word)                        | `str`   |
| `empty()`                         | Generate an empty string                                              | `str`   |
| `containing_character(character)` | Generate a string with a character in a random position (not at ends) | `str`   |
| `ending_with(character)`          | Generate a string ending with a specific character                    | `str`   |
| `beginning_with(character)`       | Generate a string beginning with a specific character                 | `str`   |
| `with_length(length)`             | Generate a string with exact length (empty if length ≤ 0)             | `str`   |
| `text()`                          | Generate a text string with spaces and punctuation (up to 200 chars)  | `str`   |

```python
from object_mother import StringPrimitivesMother

random_word = StringPrimitivesMother.any()  # e.g., "hello"
blank = StringPrimitivesMother.empty()  # ""
email_like = StringPrimitivesMother.containing_character("@")  # e.g., "user@name"
file_name = StringPrimitivesMother.ending_with(".txt")  # e.g., "document.txt"
hashtag = StringPrimitivesMother.beginning_with("#")  # e.g., "#trending"
code = StringPrimitivesMother.with_length(8)  # Exactly 8 characters
description = StringPrimitivesMother.text()  # e.g., "Lorem ipsum..."
```

## ListPrimitivesMother

The `ListPrimitivesMother` class generates list test data for testing scenarios requiring `list` values.

| Method     | Description                | Returns |
|------------|----------------------------|---------|
| `empty()`  | Generate an empty list     | `list`  |

```python
from object_mother import ListPrimitivesMother

empty_collection = ListPrimitivesMother.empty()  # []
```

## StringUuidPrimitivesMother

The `StringUuidPrimitivesMother` class generates UUID string test data for testing scenarios requiring identifier values.

| Method      | Description                                                        | Returns |
|-------------|--------------------------------------------------------------------|---------|
| `any()`     | Generate any random valid UUID string value (UUID4 format)         | `str`   |
| `invalid()` | Generate an invalid UUID string (useful for testing validation)    | `str`   |

```python
from object_mother import StringUuidPrimitivesMother

user_id = StringUuidPrimitivesMother.any()  # e.g., "550e8400-e29b-41d4-a716-446655440000"
bad_id = StringUuidPrimitivesMother.invalid()  # Invalid UUID format
```
