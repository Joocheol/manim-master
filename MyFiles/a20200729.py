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

# class PauseAndPonder(Scene):
#     def construct(self):
#         pause = TexMobject("=").rotate(np.pi/2)
#         pause.stretch(0.5, 1)
#         pause.set_height(1.5)
#         bubble = ThoughtBubble().set_height(2)
#         pause.shift(LEFT)
#         bubble.next_to(pause, RIGHT, buff = 1)
#
#         self.play(FadeIn(pause))
#         self.play(ShowCreation(bubble))
#         self.wait()

class NumericToComputations(Scene):
    def construct(self):
        top = TextMobject("Numeric understanding")
        arrow = Arrow(UP, DOWN)
        bottom = TextMobject("Actual computations")
        top.next_to(arrow, UP)
        bottom.next_to(arrow, DOWN)

        self.add(top)
        self.play(ShowCreation(arrow))
        self.play(FadeIn(bottom))
        self.wait()

class ThoughtBubbleTransformation(LinearTransformationScene):
    def construct(self):
        self.setup()
        rotation = rotation_about_z(np.pi/3)
        self.apply_matrix(
            np.linalg.inv(rotation),
            path_arc = -np.pi/3,
        )
        self.apply_matrix([[0, 1], [-1, 1]])
        self.apply_matrix(
            rotation,
            path_arc = np.pi/3,
        )
        self.wait()

class SineApproximations(Scene):
    def construct(self):
        series = self.get_series()
        one_approx = self.get_approx_series("1", 1)
        one_approx.set_color(YELLOW)
        pi_sixts_approx = self.get_approx_series("\\pi/6", np.pi/6)
        pi_sixts_approx.set_color(RED)
        words = TextMobject("(How calculators compute sine)")
        words.set_color(GREEN)

        series.to_edge(UP)
        one_approx.next_to(series, DOWN, buff = 1.5)
        pi_sixts_approx.next_to(one_approx, DOWN, buff = 1.5)

        self.play(Write(series))
        self.wait()
        self.play(FadeIn(words))
        self.wait(2)
        self.play(FadeOut(words))
        self.remove(words)
        self.wait()
        self.play(Write(one_approx))
        self.play(Write(pi_sixts_approx))
        self.wait()

    def get_series(self):
        return TexMobject("""
            \\sin(x) = x - \\dfrac{x^3}{3!} + \\dfrac{x^5}{5!}
            + \\cdots + (-1)^n \\dfrac{x^{2n+1}}{(2n+1)!} + \\cdots
        """)

    def get_approx_series(self, val_str, val):
        #Default to 3 terms
        approximation = val - (val**3)/6. + (val**5)/120.
        return TexMobject("""
            \\sin(%s) \\approx 
            %s - \\dfrac{(%s)^3}{3!} + \\dfrac{(%s)^5}{5!} \\approx
            %.04f
        """%(val_str, val_str, val_str, val_str, approximation))

class LooseConnectionToTriangles(Scene):
    def construct(self):
        sine = TexMobject("\\sin(x)")
        triangle = Polygon(ORIGIN, 2*RIGHT, 2*RIGHT+UP)
        arrow = DoubleArrow(LEFT, RIGHT)
        sine.next_to(arrow, LEFT)
        triangle.next_to(arrow, RIGHT)

        q_mark = TextMobject("?").scale(1.5)
        q_mark.next_to(arrow, UP)

        self.add(sine)
        self.play(ShowCreation(arrow))
        self.play(ShowCreation(triangle))
        self.play(Write(q_mark))
        self.wait()

class PhysicsExample(Scene):
    def construct(self):
        title = TextMobject("Physics")
        title.to_corner(UP+LEFT)
        parabola = FunctionGraph(
            lambda x : (3-x)*(3+x)/4,
            x_min = -4,
            x_max = 4
        )

        self.play(Write(title))
        self.projectile(parabola)
        self.velocity_vector(parabola)
        self.approximate_sine()

    def projectile(self, parabola):
        dot = Dot(radius = 0.15)
        kwargs = {
            "run_time" : 3,
            "rate_func" : linear
        }
        self.play(
            MoveAlongPath(dot, parabola.copy(), **kwargs),
            ShowCreation(parabola, **kwargs)
        )
        self.wait()


    def velocity_vector(self, parabola):
        alpha = 0.7
        d_alpha = 0.01
        vector_length = 3

        p1 = parabola.point_from_proportion(alpha)
        p2 = parabola.point_from_proportion(alpha + d_alpha)
        vector = vector_length*(p2-p1)/get_norm(p2-p1)
        v_mob = Vector(vector, color = YELLOW)
        vx = Vector(vector[0]*RIGHT, color = GREEN_B)
        vy = Vector(vector[1]*UP, color = RED)
        v_mob.shift(p1)
        vx.shift(p1)
        vy.shift(vx.get_end())

        arc = Arc(
            angle_of_vector(vector),
            radius = vector_length / 4.
        )
        arc.shift(p1)
        theta = TexMobject("\\theta").scale(0.75)
        theta.next_to(arc, RIGHT, buff = 0.1)

        v_label = TexMobject("\\vec{v}")
        v_label.shift(p1 + RIGHT*vector[0]/4 + UP*vector[1]/2)
        v_label.set_color(v_mob.get_color())
        vx_label = TexMobject("||\\vec{v}|| \\cos(\\theta)")
        vx_label.next_to(vx, UP)
        vx_label.set_color(vx.get_color())
        vy_label = TexMobject("||\\vec{v}|| \\sin(\\theta)")
        vy_label.next_to(vy, RIGHT)
        vy_label.set_color(vy.get_color())

        for v in v_mob, vx, vy:
            self.play(
                ShowCreation(v)
            )
        self.play(
            ShowCreation(arc),
            Write(theta, run_time = 1)
        )
        for label in v_label, vx_label, vy_label:
            self.play(Write(label, run_time = 1))
        self.wait()

    def approximate_sine(self):
        approx = TexMobject("\\sin(\\theta) \\approx 0.7\\text{-ish}")
        #morty = Mortimer(mode = "speaking")
        #morty.flip()
        #morty.to_corner()
        #bubble = SpeechBubble(width = 4, height = 3)
        #bubble.set_fill(BLACK, opacity = 1)
        #bubble.pin_to(morty)
        #bubble.position_mobject_inside(approx)

        self.play(
            # FadeIn(morty),
            # ShowCreation(bubble),
            Write(approx),
            run_time = 2
        )
        self.wait()

class AboutPacing(Scene):
    def construct(self):
        words = TextMobject("About pacing...")
        dots = words.split()[-3:]
        words.remove(*dots)
        self.play(FadeIn(words))
        # self.play(Write(VMobject(*dots)))
        self.wait()

class NextVideo(Scene):
    def construct(self):
        title = TextMobject("Next video: Vectors, what even are they?")
        title.to_edge(UP)
        rect = Rectangle(width = 16, height = 9, color = BLUE)
        rect.set_height(6)
        rect.next_to(title, DOWN)

        self.add(title)
        self.play(ShowCreation(rect))
        self.wait()

