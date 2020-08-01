from manimlib.imports import *


class a2020080115(Scene):
    def construct(self):
        mm = self.row_matrix(5, 3)
        rm = self.col_matrix(1, 5)
        c = self.columns(3)
        r = self.rows(3)
        g = VGroup(mm, c, r, rm).arrange()
        self.play(ShowCreation(g))
        self.wait()


    def rows(self, m):
        rec = Rectangle(height=0.25, width=1.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g = VGroup(*[rec.copy() for i in range(m)]).arrange((DOWN))
        gg = self.add_brackets(g)
        return gg

    def columns(self, m):
        rec= Rectangle(height=2.3, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g= VGroup(*[rec.copy() for i in range(m)]).arrange((RIGHT))
        gg = self.add_brackets(g)
        return gg

    def col_matrix(self, m, n):
        rec = Rectangle(height=0.25, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g = VGroup(*[rec.copy() for i in range(n)]).arrange(DOWN)
        gg = VGroup(*[g.copy() for i in range(m)]).arrange(RIGHT)
        ggg = self.add_brackets(gg)
        return ggg


    def row_matrix(self, m, n):
        rec = Rectangle(height=0.25, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g = VGroup(*[rec.copy() for i in range(m)]).arrange(RIGHT)
        gg = VGroup(*[g.copy() for i in range(n)]).arrange(DOWN)
        ggg = self.add_brackets(gg)
        return ggg

    def add_brackets(self, mobj):
        bracket_pair = TexMobject("\\big[", "\\big]")
        bracket_pair.scale(2)
        bracket_pair.stretch_to_fit_height(
            mobj.get_height() + 2 * 0.1
        )
        l_bracket, r_bracket = bracket_pair.split()
        l_bracket.next_to(mobj, LEFT, .2)
        r_bracket.next_to(mobj, RIGHT, .2)
        #self.add(l_bracket, mobj, r_bracket)
        #self.brackets = VGroup(l_bracket, mobj, r_bracket)
        return VGroup(l_bracket, mobj, r_bracket)


class a2020080111(Scene):
    def construct(self):

        rec = Rectangle(height=0.25, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g = VGroup(*[rec.copy() for i in range(3)]).arrange(RIGHT)
        gg = VGroup(*[g.copy() for i in range(5)]).arrange(DOWN)

        self.add(gg)
        self.add_brackets(gg)
        self.wait()
        gg.save_state()

        rec_2 = Rectangle(height=0.25, width=1.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g_2 = VGroup(*[rec_2.copy() for i in range(5)]).arrange((DOWN))
        self.play(ReplacementTransform(gg, g_2))
        self.wait()

        gg.restore()
        self.play(ReplacementTransform(g_2, gg))
        self.wait()

        rec_0 = Rectangle(height=0.25, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g_0 = VGroup(*[rec_0.copy() for i in range(5)]).arrange(DOWN)
        gg_0 = VGroup(*[g_0.copy() for i in range(3)]).arrange(RIGHT)

        # self.add(gg_0)
        # self.add_brackets(gg_0)
        # self.wait()
        # gg.save_state()
        # self.play(ReplacementTransform(g_2, gg_0))
        # self.wait()

        self.play(ReplacementTransform(gg, gg_0))

        rec_3 = Rectangle(height=2.3, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)
        g_3 = VGroup(*[rec_3.copy() for i in range(3)]).arrange((RIGHT))
        self.play(ReplacementTransform(gg, g_3))
        self.wait()

        gg.restore()
        self.play(ReplacementTransform(g_3, gg))

        self.play(ShowCreation(gg[0][0]))

    def add_brackets(self, mobj):
        bracket_pair = TexMobject("\\big[", "\\big]")
        bracket_pair.scale(2)
        bracket_pair.stretch_to_fit_height(
            mobj.get_height() + 2 * 0.1
        )
        l_bracket, r_bracket = bracket_pair.split()
        l_bracket.next_to(mobj, LEFT, .2)
        r_bracket.next_to(mobj, RIGHT, .2)
        self.add(l_bracket, r_bracket)
        self.brackets = VGroup(l_bracket, r_bracket)
        return self

class a2020080110(Scene):
    def construct(self):

        # self.right()
        self.left()

    def left(self):
        m12 = Matrix([["-", "-"]])
        m22 = Matrix([["-", "-"], ["-", "-"]])
        m32 = Matrix([["-", "-"], ["-", "-"], ["-", "-"]])
        m42 = Matrix([["-", "-"], ["-", "-"], ["-", "-"], ["-", "-"]])
        g = VGroup(m12, m22, m32, m42).arrange()
        self.play(Write(g))

    def right(self):
        m21 = Matrix([["-"], ["-"]])
        m22 = Matrix([["-", "-"], ["-", "-"]])
        m23 = Matrix([["-", "-", "-"], ["-", "-", "-"]])
        m24 = Matrix([["-", "-", "-", "-"], ["-", "-", "-", "-"]])
        g = VGroup(m21, m22, m23, m24).arrange()
        self.play(Write(g))


class a2020080109(Scene):
    def construct(self):
        m_1 = Matrix([[1, 2], [3, 4]])
        self.play(Write(m_1))

        b_1 = Brace(m_1, LEFT)
        self.play(ShowCreation(b_1))

        num_1 = TexMobject("2")
        num_1.next_to(b_1, LEFT)
        self.play(Write(num_1))

        b_2 = Brace(m_1, UP)
        self.play(ShowCreation(b_2))

        num_2 = TexMobject("2")
        num_2.next_to(b_2, UP)
        self.play(Write(num_2))

        f_1 = TexMobject(r"2 \times 2")
        f_1.next_to(m_1, 2*DOWN)

        self.play(TransformFromCopy(num_1, f_1[0][0]))
        self.play(TransformFromCopy(num_2, f_1[0][2]))
        self.add(f_1)
        self.play(
            FadeOut(b_1),
            FadeOut(b_2),
            FadeOut(num_1),
            FadeOut(num_2),
        )

        f_2 = TexMobject(r"2 \times n")
        f_2.next_to(f_1, 5 * RIGHT)
        self.play(Write(f_2), f_2[0][0].set_color, "#FF00FF", f_1[0][2].set_color, YELLOW)

        f_3 = TexMobject(r"m \times 2")
        f_3.next_to(f_1, 5 * LEFT)
        self.play(Write(f_3), f_3[0][2].set_color, "#00FF00", f_1[0][0].set_color, "#0000FF")





class a2020080105(Scene):
    def construct(self):

        d = Circle()
        r_1 = Matrix([[d, "-"], [3, 4]])
        r_2 = Matrix([[1, 2], [3, 5]])
        t_1 = TexMobject(r"a \times ")
        r_3 = VGroup(r_1, t_1, r_2).arrange()

        # self.play(Write(r_3[0][0][0]), Write(r_3[0][0][2]))
        self.play(Write(r_3))
        self.wait()

        v_1 = VGroup(r_3[0][0][0], r_3[0][0][2])

        # v_2 = SurroundingRectangle(v_1)
        v_2 = BackgroundRectangle(v_1, color=YELLOW)
        self.add(v_2)
        self.wait()

        c = Circle()
        # mm_1 = MobjectMatrix(c)
        # self.play(ShowCreation(mm_1))

class Right_Multiplication(Scene):
    def construct(self):
        m_1 = TexMobject(r'''
            \begin{bmatrix}
            1 & 2 & 3 \\
            4 & 5 & 6 \\
            7 & 8 & 9 
            \end{bmatrix}
            \begin{bmatrix}
            a\\
            b\\
            c 
            \end{bmatrix}
            =
            \begin{bmatrix}
            \alpha \\
            \beta \\
            \gamma 
            \end{bmatrix}
        ''')

        m_1[0][2].set_color(RED)
        m_1[0][5].set_color(RED)
        m_1[0][8].set_color(RED)
        m_1[0][15].set_color(RED)

        m_1[0][3].set_color(YELLOW)
        m_1[0][6].set_color(YELLOW)
        m_1[0][9].set_color(YELLOW)
        m_1[0][16].set_color(YELLOW)

        m_1[0][4].set_color(BLUE)
        m_1[0][7].set_color(BLUE)
        m_1[0][10].set_color(BLUE)
        m_1[0][17].set_color(BLUE)


        self.play(Write(m_1))
        self.wait()
        self.play(FadeOut(m_1))

        m_2 = TexMobject(r'''
                    \begin{bmatrix}
                    a & b & c 
                    \end{bmatrix}
                    \begin{bmatrix}
                    1 & 2 & 3 \\
                    4 & 5 & 6 \\
                    7 & 8 & 9 
                    \end{bmatrix}
                    =
                    \begin{bmatrix}
                    \alpha & \beta & \gamma 
                    \end{bmatrix}
                ''')

        m_2[0][1].set_color(RED)
        m_2[0][7].set_color(RED)
        m_2[0][8].set_color(RED)
        m_2[0][9].set_color(RED)

        m_2[0][2].set_color(YELLOW)
        m_2[0][10].set_color(YELLOW)
        m_2[0][11].set_color(YELLOW)
        m_2[0][12].set_color(YELLOW)

        m_2[0][3].set_color(BLUE)
        m_2[0][13].set_color(BLUE)
        m_2[0][14].set_color(BLUE)
        m_2[0][15].set_color(BLUE)

        self.play(Write(m_2))
        self.wait()
        self.play(FadeOut(m_2))

        m_21 = TexMobject(r'''
                            \begin{bmatrix}
                            a & b & c 
                            \end{bmatrix}
                            \begin{bmatrix}
                            1 & 2 & 3 \\
                            4 & 5 & 6 \\
                            7 & 8 & 9 
                            \end{bmatrix}
                            =
                            \begin{bmatrix}
                            a \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \\
                            + \\
                            b \begin{bmatrix} 4 & 5 & 6 \end{bmatrix} \\
                            + \\
                            c \begin{bmatrix} 7 & 8 & 9 \end{bmatrix} \\
                            \end{bmatrix}
                        ''')

        m_21[0][28].set_color(YELLOW)

        self.play(Write(m_21))
        self.wait()