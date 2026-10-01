# cs470-simple-algebra

A minimal Python library for learning groups, rings, and fields through modular arithmetic. To assist Week 2 of CS470/519 at Bilkent University.

Read [algebra.py](algebra.py) and [polynomials.py](polynomials.py). Python 3.9+, no dependencies.

## Lecture versions

The polynomial lecture builds on the algebra lecture.

| Lecture | Content | Examples |
|---|---|---|
| [Algebra](<https://github.com/kafeslab/cs470-simple-algebra/releases/tag/week2-algebra>) | Groups, rings, and prime fields | ex1-ex5 |
| [Polynomials](<https://github.com/kafeslab/cs470-simple-algebra/releases/tag/week2-polynomials>) | Adds binary polynomials, extension fields | ex1-ex6 |

[See what changed between lectures](<https://github.com/kafeslab/cs470-simple-algebra/compare/week2-algebra...week2-polynomials>).

The main branch contains the latest version.

```sh
python3 ex1.py  # Additive groups
python3 ex2.py  # A ring that is not a field
python3 ex3.py  # Two groups inside a field
python3 ex4.py  # Division through inverses
python3 ex5.py  # Binary arithmetic: XOR and AND
python3 ex6.py  # Binary polynomials and inverses
```

Binary extension fields store polynomial coefficients as bits (e.g. x^2 + 1 as `0b101`):

```python
from algebra import binary_field
from polynomials import format_polynomial

field = binary_field(0b1011)  # Modulo x^3 + x + 1
print(format_polynomial(field.multiply(0b101, 0b111)))  # x^2 + x
print(format_polynomial(field.multiplicative_group.inverse(0b101)))  # x
```

Exercise: implement `integer_egcd` in `algebra.py` and `polynomial_egcd` in `polynomials.py`.
Field division and multiplicative inverses use them automatically, they do a linear search over all the elements to find the inverse if they raise `NotImplementedError`.
