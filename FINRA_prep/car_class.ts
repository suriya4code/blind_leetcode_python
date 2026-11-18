abstract class Car {
    name: string;
    model: string;
    make: string;

    constructor(name: string, model: string, make: string) {
        this.name = name;
        this.model = model;
        this.make = make;
    }

    describe(): string {
        return `${this.make} ${this.model} (${this.name})`;
    }

    // Each brand must say what engine it uses
    abstract engineType(): string;
}


class Audi extends Car {
    constructor(name: string, model: string) {
        super(name, model, "Audi");
    }

    engineType(): string {
        return "TFSI petrol";
    }
}


const myCar = new Audi("My Ride", "A4");
console.log(myCar.describe()); // Audi A4 (My Ride)
console.log(myCar.engineType()); // TFSI petrol
console.log(myCar instanceof Car); // true

// new Car("x", "y", "z");  // compile error: Cannot create an instance of an abstract class.
