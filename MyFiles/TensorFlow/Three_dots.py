from manimlib.imports import *


class Three_Dots(GraphScene):
    def construct(self):
        self.setup_axes()
        self.wait()

        dot_01 = Dot().move_to(self.coords_to_point(2, 3))
        dot_02 = Dot().move_to(self.coords_to_point(5, 9))
        dot_03 = Dot().move_to(self.coords_to_point(7, 8))
        self.add(*[dot_01, dot_02, dot_03])
        self.wait()

        tracker_01 = ValueTracker(-1)
        tracker_02 = ValueTracker(5)

        def func_01():
            m = tracker_01.get_value()
            b = tracker_02.get_value()
            graph = self.get_graph(lambda x: m * x + b)
            graph.set_color(color=YELLOW)
            return graph

        graph_01 = always_redraw(func_01)
        self.play(ShowCreation(graph_01))
        self.wait()
        self.play(tracker_01.set_value, 4/3, tracker_02.set_value, 3-(8/3), rate_func=smooth, run_time=5)
        self.wait()

        formula_01 = TexMobject(r"y = m x + b").move_to(RIGHT*3)
        self.play(Write(formula_01))
        self.wait()


