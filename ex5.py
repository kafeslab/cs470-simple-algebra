from algebra import prime_field


def main():
    field = prime_field(2)

    print("5. Bits form a field (modulo 2)")
    print("a b | a + b | a * b")
    for a in field.elements:
        for b in field.elements:
            print(f"{a} {b} |   {field.add(a, b)}   |   {field.multiply(a, b)}")
    print("Addition is XOR; multiplication is AND.")
    print("1 + 1 =", field.add(1, 1))
    print("But zero and one are distinct:", field.zero != field.one)


if __name__ == "__main__":
    main()
