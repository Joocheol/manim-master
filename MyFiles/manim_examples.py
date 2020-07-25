from manimlib.imports import *

class manim_examples(GraphScene):
    def construct(self):
        self.setup_axes()

        def graph_to_be_drawn(x):
            return (1 / 2) * x ** 2 - 3

        vt = ValueTracker(0)

        graph_1 = self.get_graph(graph_to_be_drawn, x_min=-2)

        def moving_dot():
            x = vt.get_value()
            d = Dot().move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
            return d

        dd = always_redraw(moving_dot)

        self.add(dd, graph_1)
        self.play(vt.set_value, 5, rate_func=there_and_back, run_time=5)
        self.wait()
