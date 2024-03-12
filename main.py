from lab_25_task_1.bankAccount import BankAccount
from lab_25_task_1.book import Book
from lab_25_task_1.car import Car
from lab_25_task_1.circle import Circle
from lab_25_task_1.student import Student

student = Student("Іван", 20)
student.print_info()

circle = Circle(10)
print(f"Радіус {circle.area()}\n")

book = Book("2010", "Hello World", "test")
book.display_info()

car = Car("Toyota", "Camry", 2020)
car.start_engine()

account = BankAccount("Василь Петрович", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)