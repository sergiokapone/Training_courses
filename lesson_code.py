"""Урок. Об'єктно орієнтоване програмування в Python"""


class Dog:
    name: str = "Кубик"
    age: int = 15


bobik: Dog = Dog()

print(bobik.name)
print(bobik.age)

bobik.name = "Бобік"
bobik.age = 5

print(bobik.name)
print(bobik.age)
