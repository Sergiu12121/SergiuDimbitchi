class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        return f"The car accelerated to {self.speed} mph."

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        return f"The car decelerated to {self.speed} mph."

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

