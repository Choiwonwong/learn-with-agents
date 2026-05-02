from typing import override


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def turn_on(self):
        self._print_up()

    def turn_off(self):
        self._print_up()

    def _print_up(self):
        print({"make": self.make, "model": self.model, "year": self.year})

class ModelY(Car):
    @override
    def turn_on(self):
        super().turn_on()
        print("시동 시작")

    @override
    def turn_off(self):
        super().turn_off()
        print("시동 종료")


my_model_y = ModelY(
    "Tesla",
    "modelY",
    2020,
)

my_model_y.turn_on()
my_model_y.turn_off()