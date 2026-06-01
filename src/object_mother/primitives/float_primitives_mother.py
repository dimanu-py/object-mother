from object_mother.object_mother import ObjectMother


class FloatPrimitivesMother(ObjectMother):
    """Generate float primitive values for testing."""

    @classmethod
    def any(cls) -> float:
        """Generate any random float value."""
        return cls._faker().pyfloat()

    @classmethod
    def positive(cls) -> float:
        """Generate a positive float value greater than zero."""
        return cls._faker().pyfloat(positive=True, min_value=0.1)

    @classmethod
    def negative(cls) -> float:
        """Generate a negative float value less than zero."""
        return cls._faker().pyfloat(positive=False, max_value=-0.1)

    @staticmethod
    def zero() -> float:
        """Generate zero as a float."""
        return 0.0
