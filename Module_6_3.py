import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0] 
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        if dz * self.speed < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, I'm attacking you 0_0")
        else:
            print("Sorry, I'm peaceful :)")

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("This animal doesn't make any sound")


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here {'is' if eggs == 1 else 'are'} {eggs} egg{'s' if eggs > 1 else ''} for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed
        if self._cords[2] < 0:
            self._cords[2] = 0
            print("You reached the maximum depth!")


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(AquaticAnimal, Bird, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = max(AquaticAnimal._DEGREE_OF_DANGER, PoisonousAnimal._DEGREE_OF_DANGER)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(3)
db.get_cords()

db.lay_eggs()
