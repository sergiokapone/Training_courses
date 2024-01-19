"""Урок. Об'єктно орієнтоване програмування в Python"""


class Dog:
    name: str = "Кубик"
    age: int = 15

    def voice(self):
        print("Гав! Гав! Гав!")

bobik: Dog = Dog()


bobik.name = "Бобік"
bobik.age = 5



bobik.voice()
