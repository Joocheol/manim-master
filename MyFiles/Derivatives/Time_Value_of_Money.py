from manimlib.imports import *

class Title(Scene):
    def construct(self):
        text_01 = TextMobject(*["Time ", "Value ", "of ", "Money"]).scale(2)
        self.play(Write(text_01))
        self.wait()

class intro_03(Scene):
    def construct(self):
        nline = NumberLine(x_min=0, x_max=4.1, unit_size=2, number_at_center=2, include_numbers=True)
        d = Dot()
        c_arrow_01 = CurvedArrow(np.array([-4, -0.6, 0]), np.array([-2, -0.6, 0]))
        c_arrow_02 = CurvedArrow(np.array([-2, -0.6, 0]), np.array([0, -0.6, 0]))
        c_arrow_03 = CurvedArrow(np.array([0, -0.6, 0]), np.array([2, -0.6, 0]))
        c_arrow_04 = CurvedArrow(np.array([2, -0.6, 0]), np.array([4, -0.6, 0]))

        self.play(ShowCreation(d.move_to([-4, 0, 0])))

        self.play(ShowCreation(nline))

        self.play(ShowCreation(c_arrow_01))
        self.play(ShowCreation(c_arrow_02))
        self.play(ShowCreation(c_arrow_03))
        self.play(ShowCreation(c_arrow_04))

        self.wait()

class intro_02(Scene):
    def construct(self):
        text_01 = TextMobject("1. Simple interest")
        text_02 = TextMobject("2. Compound interest")
        g_01 = VGroup(text_01, text_02).arrange(direction=DOWN, aligned_edge=LEFT)

        self.play(Write(g_01))
        self.wait()

class intro_01(Scene):
    def construct(self):
        formula_01 = TexMobject(*['10', r"\cdot", '(1+r)', '=', '11'])
        formula_02 = TexMobject(*['10', '=', r"{{11}", r"\over", r"{1 + r}}"])
        formula_03 = TexMobject(*['10', r"\cdot", '(1+r)', '=', '11'])

        self.play(
            Write(formula_01)
        )
        self.wait()

        self.play(
            ReplacementTransform(formula_01[0], formula_02[0]),
            ReplacementTransform(formula_01[1], formula_02[3]),
            ReplacementTransform(formula_01[2], formula_02[4]),
            ReplacementTransform(formula_01[3], formula_02[1]),
            ReplacementTransform(formula_01[4], formula_02[2]),
        )
        self.wait()

        self.play(
            ReplacementTransform(formula_02[0], formula_03[0]),
            ReplacementTransform(formula_02[3], formula_03[1]),
            ReplacementTransform(formula_02[4], formula_03[2]),
            ReplacementTransform(formula_02[1], formula_03[3]),
            ReplacementTransform(formula_02[2], formula_03[4]),
        )
        self.wait()

class Money(Scene):
    def construct(self):
        formula_01 = TexMobject(*[r"10", r"\neq", r"11"])
        formula_02 = TexMobject(*[r"\$ 10", r"\neq", r"\$ 11"])
        path_01 = ArcBetweenPoints(formula_02[0].get_center(), LEFT * 4)
        path_02 = ArcBetweenPoints(formula_02[2].get_center(), RIGHT * 4)
        line = DashedLine(start=TOP, end=BOTTOM)
        text_01 = TextMobject(r"Present")
        text_02 = TextMobject(r"Future")
        c_arrow_01 = CurvedArrow(LEFT * 4 + 0.5 * DOWN, RIGHT * 4 + 0.5 * DOWN)
        c_arrow_02 = CurvedArrow(RIGHT * 4 + 0.5 * UP, LEFT * 4 + 0.5 * UP)

        self.play(
            Write(formula_01[0]),
        )
        self.wait()

        self.play(
            Write(formula_01[2]),
        )
        self.wait()

        self.play(
            Write(formula_01[1]),
        )
        self.wait()

        self.play(
            ReplacementTransform(formula_01[0], formula_02[0]),
            ReplacementTransform(formula_01[2], formula_02[2]),
        )
        self.wait()

        self.play(
            FadeOut(formula_01[1]),
            ShowCreation(line),
            MoveAlongPath(formula_02[0], path_01),
            MoveAlongPath(formula_02[2], path_02),
            Write(text_01.move_to(LEFT * 4 + UP * 3)),
            Write(text_02.move_to(RIGHT * 4 + UP * 3)),
        )
        self.wait()

        self.play(
            ShowCreation(c_arrow_01),
        )
        self.wait()

        self.play(
            ShowCreation(c_arrow_02),
        )
        self.wait()

class intro_old(Scene):
    CONFIG = {
        "n_of_steps": 20,
        "width": 7,
        "height": 5,
        "radius": 0.1,
        "origin": np.array([-4, 0, 0])
    }

    def construct(self):

        nodes = [
            [Circle(radius=self.radius) for j in range(i + 1)] for i in range(self.n_of_steps + 1)
        ]

        for i in range(self.n_of_steps + 1):
            for j in range(i + 1):
                location = self.origin \
                           + np.array([self.width / self.n_of_steps * i, 0, 0]) \
                           + np.array([0, self.height / self.n_of_steps * (j - i / 2), 0])
                nodes[i][j].move_to(location)

        center = TextMobject("In this world, we have").scale(0.7)
        self.play(Write(center.shift(LEFT * 0.5)))

        nodes_g = VGroup(*[nodes[0][0]])
        self.play(Write(nodes_g), run_time=1)
        text_1 = TextMobject("Present").scale(0.7)
        self.play(Write(text_1.next_to(nodes[0][0], LEFT)))

        nodes_g = VGroup(*nodes[self.n_of_steps])
        self.play(Write(nodes_g), run_time=1)
        text_2 = TextMobject("Future").scale(0.7)
        brace = Brace(nodes_g, RIGHT)
        self.play(Write(brace))
        self.play(Write(text_2.next_to(brace, RIGHT)))

        center_1 = TextMobject("They are connected").scale(0.7)
        self.play(Transform(center, center_1.shift(LEFT * 0.5)))
        self.wait(2)
        self.play(FadeOut(center))

        nodes_g = VGroup(*[nodes[i][j] for i in range(1, self.n_of_steps) for j in range(i + 1)])
        self.play(ShowCreation(nodes_g), run_time=2)
        self.wait()
        self.play(FadeOut(nodes_g))
        text_3 = TextMobject("This is the binomial world").scale(0.7)
        self.play(Write(text_3.shift(LEFT * 0.5)))
        self.wait()
        self.play(ShowCreationThenFadeOut(nodes_g))
        self.wait()

class steps(Scene):
    CONFIG = {
        "n_of_steps": 20,
        "width": 7,
        "height": 5,
        "radius": 0.1,
        "origin": np.array([-4, 0, 0])
    }

    def construct(self):

        for i in [1, 2, 5, 10, 20]:
            self.my_tree(i)
            self.wait()

    def my_tree(self, steps):
        nodes = [
            [Circle(radius=self.radius) for j in range(i + 1)] for i in range(self.n_of_steps + 1)
        ]

        for i in range(steps + 1):
            for j in range(i + 1):
                location = self.origin \
                           + np.array([self.width / steps * i, 0, 0]) \
                           + np.array([0, self.height / steps * (j - i / 2), 0])
                nodes[i][j].move_to(location)

        nodes_g = VGroup(*[nodes[i][j] for i in range(steps + 1) for j in range(i + 1)])

        self.play(ShowCreation(nodes_g))
        self.wait()
        self.play(Uncreate(nodes_g))

    # def construct(self):

    #     nodes = [
    #         [Circle(radius = self.radius) for j in range(i+1)] for i in range(self.n_of_steps+1)
    #     ]

    #     for i in range(self.n_of_steps+1):
    #         for j in range(i+1):
    #             location = self.origin \
    #                 + np.array([self.width/self.n_of_steps * i, 0, 0])  \
    #                 + np.array([0, self.height/self.n_of_steps * (j-i/2), 0])
    #             nodes[i][j].move_to(location)

    #     center = TextMobject("It starts from").scale(0.7)
    #     self.play(Write(center.shift(LEFT*0.5)))

    #     nodes_g = VGroup(*[nodes[0][0]])
    #     self.play(Write(nodes_g), run_time=1)
    #     text_1 = TextMobject("Present").scale(0.7)
    #     self.play(Write(text_1.next_to(nodes[0][0], LEFT)))

    #     nodes_g = VGroup(*nodes[self.n_of_steps])
    #     self.play(Write(nodes_g), run_time=1)
    #     text_2 = TextMobject("Future").scale(0.7)
    #     brace = Brace(nodes_g, RIGHT)
    #     self.play(Write(brace))
    #     self.play(Write(text_2.next_to(brace, RIGHT)))

    #