"""Binary polynomials: each bit is a coefficient, so 0b101 represents x^2 + 1."""


def polynomial_multiply(a: int, b: int) -> int:
    """Multiply over F_2. Adding terms uses XOR, so there are no carries."""
    if a < 0 or b < 0:
        raise ValueError("Binary polynomials must be nonnegative")

    product = 0
    while b:
        if b & 1:
            product ^= a
        a <<= 1
        b >>= 1
    return product


def polynomial_divmod(a: int, b: int) -> tuple[int, int]:
    """Return the quotient and remainder from polynomial long division over F_2."""
    if a < 0 or b < 0:
        raise ValueError("Binary polynomials must be nonnegative")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by the zero polynomial")

    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        quotient ^= 1 << shift
        a ^= b << shift  # Subtract the multiple that cancels the leading term.
    return quotient, a


def polynomial_egcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (d, u, v) with d = gcd(a, b) = u*a + v*b over F_2 polynomials."""
    raise NotImplementedError("Implement polynomial EGCD")


def polynomial_inverse(a: int, modulus: int) -> int:
    """Return the multiplicative inverse of a modulo a binary polynomial."""
    if modulus < 2:
        raise ValueError("The modulus must be a nonconstant binary polynomial")
    a = polynomial_divmod(a, modulus)[1]
    if a == 0:
        raise ZeroDivisionError("Zero has no multiplicative inverse")
    d, u, _ = polynomial_egcd(a, modulus)
    if d != 1:
        raise ValueError(f"{a} has no inverse modulo {modulus}")
    return polynomial_divmod(u, modulus)[1]


def is_irreducible(polynomial: int) -> bool:
    """A reducible polynomial has a factor of degree at most half its degree."""
    if polynomial < 2:
        return False

    degree = polynomial.bit_length() - 1
    for factor_degree in range(1, degree // 2 + 1):
        for factor in range(1 << factor_degree, 1 << (factor_degree + 1)):
            if polynomial_divmod(polynomial, factor)[1] == 0:
                return False
    return True


def format_polynomial(polynomial: int) -> str:
    """Write a binary polynomial in descending powers of x."""
    if polynomial < 0:
        raise ValueError("Binary polynomials must be nonnegative")

    terms = []
    for degree in range(polynomial.bit_length() - 1, -1, -1):
        if polynomial & (1 << degree):
            if degree == 0:
                terms.append("1")
            elif degree == 1:
                terms.append("x")
            else:
                terms.append(f"x^{degree}")
    return " + ".join(terms) or "0"
