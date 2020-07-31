from manimlib.imports import *


class a2020073105(Scene):
    def construct(self):
        text_01 = TextMobject(
            r'''$n$ linear equations, $n$ unknowns'''
        )

        text_02 = TextMobject(
            r'''Row picture'''
        )
        text_02.next_to(text_01, DOWN)

        text_03 = TextMobject(
            r'''(*) Column picture'''
        )
        text_03.next_to(text_02, DOWN)

        text_04 = TextMobject(
            r'''Matrix form'''
        )
        text_04.next_to(text_03, DOWN)

        vg_1 = VGroup(text_01, text_02, text_03, text_04)
        vg_1.move_to(ORIGIN)

        self.play(Write(vg_1))


class a2020073106(Scene):
    def construct(self):
        formula_1 = TexMobject(r'''
            2x  - y = 0 \\
            -x  + 2y = 3
        ''')

        self.play(Write(formula_1))

        self.play(formula_1[0][12].move_to, TOP)


class a2020073111(GraphScene):
    CONFIG = {
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "x_axis_width": FRAME_WIDTH,
        "x_leftmost_tick": int(-FRAME_X_RADIUS),
        "y_min": -FRAME_Y_RADIUS,
        "y_max": FRAME_Y_RADIUS,
        "y_axis_height": FRAME_HEIGHT,
        "graph_origin": ORIGIN,
    }

    def construct(self):

        def eq_1(x):
            return 2 * x

        self.setup_axes()
        g_1 = self.get_graph(eq_1)
        print(self.coords_to_point(0, 1))
        print(self.input_to_graph_point(0, g_1))
        dot = Dot().move_to(self.input_to_graph_point(0, g_1))
        self.play(ShowCreation(g_1))
        self.play(ShowCreation(dot))
        self.wait()

class a2020073112(GraphScene):
    def construct(self):
        plane = NumberPlane()
        self.play(ShowCreation(plane))
