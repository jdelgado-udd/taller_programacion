class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other: Complex) -> Complex:
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other: Complex) -> Complex:
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other: Complex) -> Complex:
        denominator = other.real ** 2 + other.imaginary ** 2
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / denominator, (self.imaginary * other.real - self.real * other.imaginary) / denominator)

    def modulus(self) -> float:
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self) -> Complex:
        return Complex(self.real, -self.imaginary)

    def __str__(self) -> str:
        if self.imaginary == 0 and self.real == 0:
            return "0"

        if self.imaginary == 0:
            return str(self.real)

        if self.real == 0:
            return f"{self.imaginary}i"

        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"

        return f"{self.real} + {self.imaginary}i"