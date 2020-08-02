from manimlib.imports import *

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

