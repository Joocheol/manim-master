from manimlib.imports import *


class Plotting_a_line(GraphScene):
    def construct(self):
        self.setup_axes()
        self.wait()

        dot_01 = Dot().move_to(self.coords_to_point(3,4))
        self.play(ShowCreation(dot_01))

        # graph = FunctionGraph(
        #     lambda x: 0.5 * x + 1,
        #     x_min=-5,
        #     x_max=5,
        #     color=YELLOW,
        #     stroke_width=6,
        # )

        tracker_01 = ValueTracker(-1)
        tracker_02 = ValueTracker(5)

        def func_01():
            m = tracker_01.get_value()
            b = tracker_02.get_value()
            graph = self.get_graph(lambda t: t*m+b)
            graph.set_color(color=RED,)
            return graph

        graph_01 = always_redraw(func_01)
        self.play(ShowCreation(graph_01))
        self.play(tracker_01.set_value, 4, tracker_02.set_value, -3, rate_func=there_and_back, run_time=8)

