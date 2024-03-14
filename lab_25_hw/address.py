class Address:
    def __init__(self, city, country, address):
        self.city = city
        self.country = country
        self.address = address

    def update_address(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Поле '{key}' не існує в класі Address.")

    def display_address(self):
        for key, value in self.__dict__.items():
            if value is not None:
                print(f"{key.replace('_', ' ').capitalize()}: {value}")