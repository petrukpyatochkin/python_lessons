class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Двигун {self.brand} {self.model} {self.year} року запущено.\n")

