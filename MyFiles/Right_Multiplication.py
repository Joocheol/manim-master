from manimlib.imports import *

class a2020080105(Scene):
    def construct(self):

        r_1 = Matrix([[1, 2], [3, 4]])
        r_2 = Matrix([[1, 2], [3, 5]])
        r_3 = VGroup(r_1, r_2).arrange()

        self.play(Write(r_3[0][0][0]), Write(r_3[0][0][2]))
        self.wait()

        v_1 = VGroup(r_3[0][0][0], r_3[0][0][2])

        # v_2 = SurroundingRectangle(v_1)
        v_2 = BackgroundRectangle(v_1, color=YELLOW)
        self.add(v_2)
        self.wait()

        c = Circle()
        mm_1 = MobjectMatrix(c)
        self.play(ShowCreation(mm_1))

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