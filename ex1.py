from algebra import integers_mod


def main():
    group = integers_mod(6).additive_group

    print("1. Addition forms a group (modulo 6)")
    print("Elements:", group.elements)
    print("Identity:", group.identity)
    print("4 + 5 =", group.operation(4, 5))
    print("Additive inverse of 2:", group.inverse(2))
    print("2 + its inverse =", group.operation(2, group.inverse(2)))
    print("Abelian:", group.is_abelian())


if __name__ == "__main__":
    main()
