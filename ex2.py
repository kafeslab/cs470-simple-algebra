from algebra import integers_mod


def main():
    ring = integers_mod(6)

    print("2. A ring need not be a field (modulo 6)")
    print("Elements:", ring.elements)
    print("An inverse of 2 would satisfy 2 * b = 1 (mod 6).")
    print("Try every possible b:")

    for b in ring.elements:
        print(f"2 * {b} mod 6 =", ring.multiply(2, b))

    print("No result is 1, so 2 has no multiplicative inverse.")
    print("A field requires an inverse for every nonzero element.")
    print("This is a ring, but it is not a field.")


if __name__ == "__main__":
    main()
