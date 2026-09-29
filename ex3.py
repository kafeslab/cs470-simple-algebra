from algebra import prime_field


def main():
    field = prime_field(7)
    addition = field.additive_group
    multiplication = field.multiplicative_group

    print("3. A field contains two groups (modulo 7)")
    print("Additive group:", addition.elements)
    print("Multiplicative group:", multiplication.elements)
    print("Additive identity:", addition.identity)
    print("Multiplicative identity:", multiplication.identity)
    print("Additive inverse of 2:", addition.inverse(2))
    print("Multiplicative inverse of 2:", multiplication.inverse(2))


if __name__ == "__main__":
    main()
