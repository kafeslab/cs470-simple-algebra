"""Small finite algebraic structures, using integers as elements.

The classes describe structures whose axioms are assumed to hold.
The two factories below construct valid examples using modular arithmetic.
"""

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Group:
    """One associative operation, an identity, and an inverse for each element."""

    elements: tuple[int, ...]
    operation: Callable[[int, int], int]
    identity: int

    def inverse(self, element: int) -> int:
        if element not in self.elements:
            raise ValueError(f"{element} is not an element of this group")

        for candidate in self.elements:
            if (
                self.operation(element, candidate) == self.identity
                and self.operation(candidate, element) == self.identity
            ):
                return candidate

        raise ValueError(f"{element} has no inverse")

    def is_abelian(self) -> bool:
        """Does exchanging the operands always give the same result?"""
        return all(
            self.operation(a, b) == self.operation(b, a)
            for a in self.elements
            for b in self.elements
        )


@dataclass(frozen=True)
class Ring:
    """An abelian additive group with associative, distributive multiplication.

    Multiplication has an identity, called one.
    """

    additive_group: Group
    multiply: Callable[[int, int], int]
    one: int

    @property
    def elements(self) -> tuple[int, ...]:
        return self.additive_group.elements

    @property
    def zero(self) -> int:
        return self.additive_group.identity

    def add(self, a: int, b: int) -> int:
        return self.additive_group.operation(a, b)

    def subtract(self, a: int, b: int) -> int:
        return self.add(a, self.additive_group.inverse(b))


@dataclass(frozen=True)
class Field(Ring):
    """A commutative ring with zero != one and inverses for nonzero elements."""

    @property
    def multiplicative_group(self) -> Group:
        nonzero_elements = tuple(x for x in self.elements if x != self.zero)
        return Group(nonzero_elements, self.multiply, self.one)

    def divide(self, a: int, b: int) -> int:
        if b == self.zero:
            raise ZeroDivisionError("Zero has no multiplicative inverse")
        return self.multiply(a, self.multiplicative_group.inverse(b))


def integers_mod(modulus: int) -> Ring:
    """Integers modulo n form a ring. This example requires n >= 2."""
    if modulus < 2:
        raise ValueError("The modulus must be at least 2")

    elements = tuple(range(modulus))

    def add(a: int, b: int) -> int:
        return (a + b) % modulus

    def multiply(a: int, b: int) -> int:
        return (a * b) % modulus

    return Ring(Group(elements, add, identity=0), multiply, one=1)


def prime_field(modulus: int) -> Field:
    """Integers modulo n form a field exactly when n is prime."""
    ring = integers_mod(modulus)

    for divisor in range(2, modulus):
        if modulus % divisor == 0:
            other = modulus // divisor
            raise ValueError(
                f"Modulo {modulus} is not a field: "
                f"{divisor} * {other} = 0, even though both factors are nonzero"
            )

    return Field(ring.additive_group, ring.multiply, ring.one)
