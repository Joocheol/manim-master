from manimlib.imports import *


class a2020080620(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # self.set_camera_orientation()
        # self.play(ShowCreation(axes))
        # self.wait()
        self.set_camera_orientation(phi=PI / 10, theta=PI/3)
        self.play(ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=1)  # Start move camera
        # self.wait(5)
        # self.stop_ambient_camera_rotation()
        self.wait()