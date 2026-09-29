from algebra import prime_field


def main():
    field = prime_field(7)
    inverse = field.multiplicative_group.inverse(2)
    quotient = field.divide(3, 2)

    print("4. Division is multiplication by an inverse (modulo 7)")
    print("Multiplicative inverse of 2:", inverse)
    print("3 * the inverse of 2 =", field.multiply(3, inverse))
    print("3 / 2 =", quotient)
    print("Check: 2 * the quotient =", field.multiply(2, quotient))

    try:
        field.divide(3, 0)
    except ZeroDivisionError as error:
        print("3 / 0:", error)


if __name__ == "__main__":
    main()
