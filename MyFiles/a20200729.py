from manimlib.imports import *


class a20200729(Scene):
    def construct(self):
        title = TextMobject("Preview of core visual intuitions")
        title.to_edge(UP)
        h_line = Line(FRAME_X_RADIUS * LEFT, FRAME_X_RADIUS * RIGHT)
        h_line.next_to(title, DOWN)
        h_line.set_color(BLUE_E)
        intuitions = [
            "Matrices transform space",
            "Matrix multiplication corresponds to applying " +
            "one transformation after another",
            "The determinant gives the factor by which areas change",
        ]

        self.play(
            Write(title),
            ShowCreation(h_line),
            run_time=2
        )

        for count, intuition in enumerate(intuitions, 3):
            intuition += " (details coming in chapter %d)" % count
            mob = TextMobject(intuition)
            mob.scale(0.7)
            mob.next_to(h_line, DOWN)
            self.play(FadeIn(mob))
            self.wait(4)
            self.play(FadeOut(mob))
            self.remove(mob)
        self.wait()

class MatricesAre(Scene):
    def construct(self):
        matrix = matrix_to_mobject([[1, -1], [1, 2]])
        matrix.set_height(1)
        arrow = Arrow(LEFT, RIGHT, stroke_width = 8, preserve_tip_size_when_scaling = False)
        arrow.scale(2)
        arrow.to_edge(RIGHT)
        matrix.next_to(arrow, LEFT)

        self.play(Write(matrix, run_time = 1))
        self.play(ShowCreation(arrow))
        self.wait()

class ExampleTransformationForIntuitionList(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.apply_matrix([[1, -1], [1, -2]])
        self.wait()

class ComposedTransformsForIntuitionList(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.apply_matrix([[1, -1], [1, 2]])
        self.wait()
        self.apply_matrix([[2, 1], [1, 2]])
        self.wait()

class PauseAndPonder(Scene):
    def construct(self):
        pause = TexMobject("=").rotate(np.pi/2)
        pause.stretch(0.5, 1)
        pause.set_height(1.5)
        bubble = ThoughtBubble().set_height(2)
        pause.shift(LEFT)
        bubble.next_to(pause, RIGHT, buff = 1)

        self.play(FadeIn(pause))
        self.play(ShowCreation(bubble))
        self.wait()
