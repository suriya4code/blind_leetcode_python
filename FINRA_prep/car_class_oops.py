from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name:str, model:str, make:str):
        self.name = name
        self.model = model
        self.make = make

    def __str__(self):
        return f'This is {self.name} of {self.make} and model {self.model}'

    @abstractmethod
    def engine_type(self) -> str:
        """Each brand must say what engine it uses."""
        ...


class Audi(Car):
    def __init__(self, name, model):
        super().__init__(name, model, "Audi")

    def __str__(self):
        return super().__str__()

    def engine_type(self) -> str:
        return "TFSI petrol"


a = Audi("F4", "R-Line")
print(a)
print(a.engine_type())

# Car("x", "y", "z")  # TypeError: Can't instantiate abstract class Car