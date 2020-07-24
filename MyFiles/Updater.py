from manimlib.imports import *


class manim_updater(Scene):
    def construct(self):
        x_axis = NumberLine(x_min=-5, x_max=5)
        dot = Dot(color=YELLOW, radius=0.15).move_to(x_axis.get_left())
        number = DecimalNumber(-5, color=YELLOW).next_to(dot, UP)

        vt = ValueTracker(-3)
        number.add_updater(lambda m: m.next_to(dot, UP))
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        dot.add_updater(lambda m: m.move_to(RIGHT*vt.get_value()))

        self.add(x_axis, dot, number)
        self.play(vt.set_value, 10, rate_func=there_and_back, run_time=10)
        # self.play(dot.shift, RIGHT * 10, rate_func=there_and_back, run_time=10)
        self.wait()


class manim_updater2(Scene):
    def construct(self):
        x_axis = NumberLine(x_min=-5, x_max=5)
        dot = Dot(color=YELLOW, radius=0.15).move_to(x_axis.get_left())
        number = DecimalNumber(-5, color=YELLOW).next_to(dot, UP)

        vt = ValueTracker(-3)

        self.add(x_axis, dot, number)
        self.wait()
