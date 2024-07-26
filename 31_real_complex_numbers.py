# Construct a class called ComplexNumber which stores two properties

# real - The real part
# imaginary - The imaginary part

class ComplexNumber:

    real = 0 
    imaginary = 0
    
    # Define constructor here
    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary


    def add(self, x: "ComplexNumber")->"ComplexNumber":
        self.real += x.real
        self.imaginary += x.imaginary
        return self
    
    def subtract(self, x: "ComplexNumber")->"ComplexNumber":
        self.real -= x.real
        self.imaginary -= x.imaginary
        return self
        
        
    def multiply(self, x: "ComplexNumber")->"ComplexNumber":
        self.real = self.real * x.real - self.imaginary * x.imaginary
        return self
    
    
    def divide(self, x: "ComplexNumber")->"ComplexNumber":
        self.real = (self.real * x.real + self.imaginary * x.imaginary) / (x.real ** 2 + x.imaginary ** 2)
        self.imaginary = (self.imaginary * x.real - self.real * x.imaginary) / (x.real ** 2 + x.imaginary ** 2)
        return self
    
    
        
a = ComplexNumber(10, 5)
b = ComplexNumber(2, 3)
c1 = a.add(b) 
c2 = a.subtract(b)
c3 = a.multiply(b)
c4 = a.divide(b)
print(c1.real, c1.imaginary)
print(c2.real, c2.imaginary)
print(c3.real, c3.imaginary)
print(c4.real, c4.imaginary)
# Output: 12 8