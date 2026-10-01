from algebra import binary_field
from polynomials import format_polynomial, is_irreducible, polynomial_multiply


def main():
    a = 0b101 # x^2 + 1
    b = 0b111 # x^2 + x + 1
    modulus = 0b1011 # x^3 + x + 1
    field = binary_field(modulus)
    inverse = field.multiplicative_group.inverse(a)

    print("6. Binary polynomials over F_2")
    print("a =", format_polynomial(a))
    print("b =", format_polynomial(b))
    print("f =", format_polynomial(modulus))
    print("f is irreducible:", is_irreducible(modulus))
    print("a is irreducible:", is_irreducible(a))
    print("a + b =", format_polynomial(field.add(a, b)))
    print("a * b =", format_polynomial(polynomial_multiply(a, b)))
    print("a * b mod f =", format_polynomial(field.multiply(a, b)))
    print("Inverse of a mod f =", format_polynomial(inverse))
    print("a * its inverse mod f =", format_polynomial(field.multiply(a, inverse)))


if __name__ == "__main__":
    main()
