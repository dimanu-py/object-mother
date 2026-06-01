from object_mother.object_mother import ObjectMother


class IntegerPrimitivesMother(ObjectMother):
    """Generate int primitive values for testing."""

    @classmethod
    def any(cls) -> int:
        """Generate any random int value."""
        return cls._faker().random_int()

    @classmethod
    def positive(cls) -> int:
        """Generate a positive int value greater than zero."""
        return cls._faker().random_int(min=1)

    @classmethod
    def negative(cls) -> int:
        """Generate a negative int value less than zero."""
        return cls._faker().random_int(min=-(2**31), max=-1)

    @staticmethod
    def zero() -> int:
        """Generate zero as an int."""
        return 0
