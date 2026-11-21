import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I'll sleep")
        self.gladness += 3

    def to_chill(self):
        print("rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 100

    def to_work(self):
        print("Time to work")
        self.money += 500
        self.gladness -= 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Past out....")
            self.alive = False
        elif self.gladness <= 0:
            print("Too tired")
            self.alive = False
        elif self.progress > 4:
            print("Passed externally..")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "day " + str(day) + " of " + self.name + " life"
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