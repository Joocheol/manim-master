from manimlib.imports import *


class to_edge_example(Scene):
    def construct(self):
        text = Text(r"\int x \, dx")

        self.add(text)
        self.play(text.shift, RIGHT*10, rate_func=there_and_back, run_time=10)
