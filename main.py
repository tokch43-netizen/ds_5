import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000
        self.alive = True

    def to_study(self):
        print("навчання")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Спатки, спатки")
        self.gladness += 3

    def to_chill(self):
        print("Чіл тайм")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 100

    def to_work(self):
        print("Час працювати")
        self.money += 500
        self.gladness -= 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Втомлений")
            self.alive = False
        elif self.gladness <= 0:
            print("Дуже втомлений")
            self.alive = False
        elif self.progress > 4:
            print("Кінець навчання")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя = {self.gladness}")
        print(f"Прогрес = {round(self.progress, 2)}")
        print(f"Мані тайм = {self.money}")

    def live(self, day):
        day = "День " + str(day) + " з життя " + self.name
        print(day)

        if self.money < 100:
            self.to_work()
        else:
            live_cube = random.randint(1, 3)

            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()

        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")

for day in range(365):
    if nick.alive == False:
        break

    nick.live(day)