from manimlib.imports import *


class to_edge_example(Scene):
    def construct(self):

        c = Circle()
        vt = ValueTracker(0)

        # self.add(c)
        number = DecimalNumber(-5, color=RED).next_to(c, UP)

        number.add_updater(lambda m: m.next_to(c, UP))
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        self.play(c.shift, RIGHT * 10, rate_func=there_and_back, run_time=10)
        self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        self.play(c.shift, RIGHT * -10, rate_func=there_and_back, run_time=10)
        self.wait()
