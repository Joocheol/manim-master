from manimlib.imports import *

EXAMPLE_TRANFORM = [[0, 1], [-1, 1]]
TRANFORMED_VECTOR = [[2], [3]]

class ExampleTransformation(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.add_vector(np.array(TRANFORMED_VECTOR).flatten())
        self.apply_matrix(EXAMPLE_TRANFORM)
        self.wait()

class LinearAlgebraIntuitions(Scene):
    def construct(self):
        title = TextMobject("Preview of core visual intuitions")
        title.to_edge(UP)
        h_line = Line(FRAME_X_RADIUS*LEFT, FRAME_X_RADIUS*RIGHT)
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
            run_time = 2
        )

        for count, intuition in enumerate(intuitions, 3):
            intuition += " (details coming in chapter %d)"%count
            mob = TextMobject(intuition)
            mob.scale(0.7)
            mob.next_to(h_line, DOWN)
            self.play(FadeIn(mob))
            self.wait(4)
            self.play(FadeOut(mob))
            self.remove(mob)
        self.wait()
