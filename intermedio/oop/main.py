from maths import Complex

first = Complex(3, 4)
second = Complex(5, 12)

print(
    first,
    second,
    first.modulus(),
    second.modulus(),
    first.conjugate(),
    second.conjugate(),
    first + second,
    first * second,
    sep = "\n"
)