from manimlib.imports import *


class Game(Scene):
    def construct(self):
        self.add_game([1, 2, 3])

    def add_game(self, num):
        self.add(num[0])
