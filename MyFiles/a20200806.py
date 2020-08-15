from manimlib.imports import *


class a2020080620(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # self.set_camera_orientation()
        # self.play(ShowCreation(axes))
        # self.wait()
        c = Circle()
        self.set_camera_orientation(phi=120*DEGREES, theta=0)
        self.play(ShowCreation(axes), ShowCreation(c))

        self.begin_ambient_camera_rotation(rate=0.5)  # Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.wait()