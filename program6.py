class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        rl = self.real + other.real
        img = self.imag + other.imag
        return f'Addition of Complex Numbers --> ({rl}+{img}i)'

    def __sub__(self, other):
        rl = self.real - other.real
        img = self.imag - other.imag
        return f'Subtraction of Complex Numbers --> ({rl}+{img}i)'

    def __mul__(self, other):
        rl = (self.real * other.real) - (self.imag * other.imag)
        img = (self.real * other.imag) + (self.imag * other.real)
        return f'Multiplication of Complex Numbers --> ({rl}+{img}i)'


cmp1 = Complex(5, 3)
print(f'Real and Imaginary Values for cmp1  --> ({cmp1.real}+{cmp1.imag}i)')
cmp2 = Complex(4, 2)
print(f'Real and Imaginary Values for cmp2  --> ({cmp2.real}+{cmp2.imag}i)')
print(cmp1+cmp2)  
print(cmp1-cmp2)
print(cmp1*cmp2)

