from manimlib.imports import *


class to_edge_example(Scene):
    def construct(self):
        c = Circle()
        vt = ValueTracker(0)

        # self.add(c)
        number = DecimalNumber(-5, color=RED).next_to(c, UP)

        # number.add_updater(lambda m: m.next_to(c, UP))
        # number.add_updater(lambda m: m.set_value(vt.get_value()))

        def func():
            number = DecimalNumber(-5, color=RED).next_to(c, UP)
            number.set_value(vt.get_value())
            return number

        number = always_redraw(func)
        self.add(number)
        self.play(c.shift, RIGHT * 10, rate_func=there_and_back, run_time=1)
        self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        self.play(c.shift, RIGHT * -10, rate_func=there_and_back, run_time=1)
        self.wait()


class another(Scene):
    def construct(self):

        vt = ValueTracker(0)

        def draw_target():
            c = Circle(radius=vt.get_value())
            # c = Circle(radius=dt)
            return c
        ci = always_redraw(draw_target)

        self.add(ci)
        self.play(vt.set_value, 5, rate_func=there_and_back, run_time=10)
        self.wait()


class a_1(Scene):
    def construct(self):

        c = Circle()

        self.play(c.move_to, RIGHT*5, rate_func=there_and_back, run_time=2)
        c.move_to(LEFT*3)
        self.add(c)


class a_2(Scene):
    def construct(self):

        c = Circle()
        c.scale(3)
        dot = Dot()

        # dot.move_to(c.point_from_proportion(0.8))

        self.t_offset = 0
        rate = 1

        def u_func(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(c.point_from_proportion(self.t_offset % 1))

        dot.add_updater(u_func)

        self.add(c, dot)
        self.wait(20)






