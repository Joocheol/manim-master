from manimlib.imports import *


# mobject 좌우를 괄호로 감싸기
def add_brackets(mobj):
    bracket_pair = TexMobject("\\big[", "\\big]")
    bracket_pair.scale(2)
    bracket_pair.stretch_to_fit_height(
        mobj.get_height() + 2 * 0.1
    )
    l_bracket, r_bracket = bracket_pair.split()
    l_bracket.next_to(mobj, LEFT, .2)
    r_bracket.next_to(mobj, RIGHT, .2)
    return VGroup(l_bracket, mobj, r_bracket)


# 화면을 작은 사각형으로 채우기
rect_size = 0.25

def fill_rect(m=1, n=1, h=rect_size, w=rect_size, column=True):
    rect = Rectangle(height=h, width=w).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)

    if column:
        col = VGroup(*[rect.copy() for i in range(m)]).arrange(DOWN)
        result = VGroup(*[col.copy() for i in range(n)]).arrange(RIGHT)
    else:
        row = VGroup(*[rect.copy() for i in range(n)]).arrange(RIGHT)
        result = VGroup(*[row.copy() for i in range(m)]).arrange(DOWN)

    return result


def col_rect(m, n):
    h = rect_size * (2 * m - 1)
    return fill_rect(m=1, n=n, h=h, w=rect_size, column=False)


def row_rect(m, n):
    w = rect_size * (2 * n - 1)
    return fill_rect(m=m, n=1, h=rect_size, w=w, column=True)

