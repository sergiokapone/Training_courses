"""Урок. Об'єктно орієнтоване програмування в Python"""

class Animal:
    name: str 
    age: int
    phrase: str

    def voice(self):
        return self.phrase
 
class Mammal(Animal):
    phrase: str = "Дай молоко!"
    def run(self):
        return f"{self.name} is moving"


class Bird(Animal):
    phrase: str = "Цвірінь! Цвірінь Цвірінь!"
    def fly(self):
        return f"{self.name} is moving"

class Dog(Mammal):
    phrase = "Гав! Гав! Гав"

class Cat(Mammal):
    phrase = "Няв! Няв! Няв"

class Bat(Mammal, Bird):
    pass

bat = Bat()
print(bat.voice())

