from manim import *
import math

from numpy import array, number

class DrawScooter(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(dot.animate.shift(LEFT * 2))
        self.wait()
        self.play(dot.animate.shift((UP + LEFT) * math.sin(math.pi/180 * 45)))
        self.play(dot.animate.shift(DOWN * math.sin(math.pi/180 * 45) + LEFT * math.sin(math.pi/180 * 45)/math.tan(math.pi/180 * 70)))
        self.play(dot.animate.shift(RIGHT * 3 * math.cos(math.pi/180 * 70) + UP * 3 * math.sin(math.pi/180 * 70)))
        self.wait()

class Scooter(Scene):
    def construct(self):
        model = Tex(r"Modelo do Patinete")
        detail1 = Tex(r"Modelo Geométrico", ).to_corner(UP + RIGHT)

        self.play(
            Write(model)
        )

        self.wait()

        self.play(
            model.animate.to_corner(UP + LEFT),
            Write(detail1)
        )

        self.wait()

        dot_A = Dot(point=RIGHT * 2 + DOWN * 2)
        dot_B = Dot(point=LEFT + DOWN * 2)
        dot_C = Dot(point=((UP + LEFT) * math.sin(math.pi/180 * 45)) + LEFT + DOWN * 2)
        dot_E = Dot(point=((DOWN * math.sin(math.pi/180 * 45) + LEFT * math.sin(math.pi/180 * 45)/math.tan(math.pi/180 * 70)) + (UP + LEFT) * math.sin(math.pi/180 * 45) + LEFT + DOWN * 2))
        dot_D = Dot(point=((DOWN * math.sin(math.pi/180 * 45) + LEFT * math.sin(math.pi/180 * 45)/math.tan(math.pi/180 * 70)) + (UP + LEFT) * math.sin(math.pi/180 * 45) + LEFT + RIGHT * 3 * math.cos(math.pi/180 * 70) + UP * 3 * math.sin(math.pi/180 * 70) + DOWN * 2))
        line_AB = Line(dot_A.get_center(), dot_B.get_center())
        line_BC = Line(dot_B.get_center(), dot_C.get_center())
        line_CD = Line(dot_C.get_center(), dot_D.get_center())
        line_CE = Line(dot_C.get_center(), dot_E.get_center())
        self.play(
            Write(dot_A),
            Write(line_AB)
        )
        self.play(
            Write(dot_B),
            Write(line_BC)
        )
        self.play(
            Write(line_CD),
            Write(line_CE)
        )
        self.play(
            Write(dot_D),
            Write(dot_E)
        )

        self.wait()

        label_A = Tex(r"A", font_size=24).next_to(dot_A, 0.5 * RIGHT)
        label_B = Tex(r"B", font_size=24).next_to(dot_B, 0.5 * DOWN)
        label_C = Tex(r"C", font_size=24).next_to(dot_C, 0.3 * UL)
        label_D = Tex(r"D", font_size=24).next_to(dot_D, 0.5 * UL)
        label_E = Tex(r"E", font_size=24).next_to(dot_E, 0.5 * LEFT)

        self.play(
            Write(label_A),
            Write(label_B),
            Write(label_C),
            Write(label_D),
            Write(label_E)
        )

        self.wait()

        label_l1 = MathTex(r"l_1", font_size=24).next_to(line_AB, DOWN * 0.5)
        label_l2 = MathTex(r"l_2", font_size=24).next_to(line_BC, UP * 0.1).shift(DOWN * 0.3 + RIGHT * 0.1)
        label_l3 = MathTex(r"l_3", font_size=24).next_to(line_CD, LEFT * 0.1).shift(RIGHT * 0.27 + UP * 0.1)
        label_l4 = MathTex(r"l_4", font_size=24).next_to(line_CE, LEFT * 0.3).shift(UP * 0.1 + RIGHT * 0.1)

        self.play(
            Write(label_l1),
            Write(label_l2),
            Write(label_l3),
            Write(label_l4)
        )

        self.wait()

        dashed_line = DashedLine(dot_E, dot_B, dash_length=0.05)

        self.play(
            Write(dashed_line)
        )

        alpha = Angle(line_BC, dashed_line, radius=0.2, quadrant=(1, -1))
        beta = Angle(line_CE, dashed_line, radius=0.2, quadrant=(-1, 1), other_angle=True)

        self.play(
            Write(alpha),
            Write(beta)
        )

        alpha_label = MathTex(r"\alpha").scale(0.4).next_to(alpha, LEFT * 0.2 - DOWN * 0.01)
        beta_label = MathTex(r"\beta").scale(0.4).next_to(beta, RIGHT * 0.2 + UP * 0.001)

        self.play(
            Write(alpha_label),
            Write(beta_label)
        )

        self.wait()

        F = Arrow(start=(dot_D.get_center() + UP), end=dot_D.get_center(), buff=0.1, max_tip_length_to_length_ratio=0.2, color=BLUE)

        def getArrow(dot, deslocation):
            return Arrow(start=(dot.get_center() + UP * 0.75 + RIGHT * 0.5 * deslocation), end=dot.get_center() + RIGHT * 0.5 * deslocation, buff=0.1, max_tip_length_to_length_ratio=0.15, color=BLUE)

        f_0 = getArrow(dot_B, 0)
        f_1 = getArrow(dot_B, 1)
        f_2 = getArrow(dot_B, 2)
        f_3 = getArrow(dot_B, 3)
        f_4 = getArrow(dot_B, 4)
        f_5 = getArrow(dot_B, 5)
        f_6 = getArrow(dot_B, 6)

        f_line = Line(f_0.get_start(), f_6.get_start(), color=BLUE)

        detail2 = Tex(r"Forças Externas", color=BLUE).to_corner(UP + RIGHT)

        self.play(
            Transform(detail1, detail2),
            Write(F),
            Write(f_0),
            Write(f_1),
            Write(f_2),
            Write(f_3),
            Write(f_4),
            Write(f_5),
            Write(f_6),
            Write(f_line)
        )

        self.wait()

        label_F = MathTex(r"F", font_size=24, color=BLUE).next_to(F, 0.5 * RIGHT)
        label_f = MathTex(r"q", font_size=24, color=BLUE).next_to(f_6, 0.5 * RIGHT + 0.01 * UP)

        self.play(
            Write(label_F),
            Write(label_f)
        )

        self.wait()

        joint_1 = Triangle(color=ORANGE).scale(0.2).next_to(dot_E, DOWN * 0.1)
        joint_2 = Triangle(color=ORANGE).scale(0.15).next_to(dot_A, DOWN * 0.075)

        joint1_line = Line(color=ORANGE).scale(0.3).next_to(joint_1, DOWN * 0.01)
        joint2_line = Line(color=ORANGE).scale(0.3).next_to(joint_2, DOWN * 0.5)

        joint1_line1 = Line(start=LEFT + DOWN * 3, color=ORANGE).scale(0.04).next_to(joint_1, DOWN * 0.01).shift(LEFT * 0.3)
        joint1_line2 = Line(start=LEFT + DOWN * 3, color=ORANGE).scale(0.04).next_to(joint_1, DOWN * 0.01).shift(LEFT * 0.2)
        joint1_line3 = Line(start=LEFT + DOWN * 3, color=ORANGE).scale(0.04).next_to(joint_1, DOWN * 0.01).shift(LEFT * 0.1)


        detail3 = Tex(r"Definições dos Vínculos", color=ORANGE).to_corner(UP + RIGHT)

        self.play(
            Transform(detail1, detail3),
            Write(joint_1),
            Write(joint_2),
            Write(joint1_line),
            Write(joint2_line),
            Write(joint1_line1),
            Write(joint1_line2),
            Write(joint1_line3)
        )

        self.wait()

        Y_E = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(joint1_line, DOWN)
        Y_A = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(joint2_line, DOWN)
        X_E = Arrow(start=LEFT * 0.075, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(dot_E, LEFT * 1.5) 

        detail4 = Tex(r"Reações Vinculares", color=ORANGE).to_corner(UP + RIGHT)

        self.play(
            Transform(detail1, detail4),
            Write(Y_E),
            Write(Y_A),
            Write(X_E)
        )

        self.wait()

        label_YE = MathTex(r"Y_E", font_size=24, color=ORANGE).next_to(Y_E, 0.4 * LEFT)
        label_YA = MathTex(r"Y_A", font_size=24, color=ORANGE).next_to(Y_A, 0.4 * LEFT)
        label_XE = MathTex(r"X_E", font_size=24, color=ORANGE).next_to(X_E, 0.4 * DOWN)

        self.play(
            Write(label_YE),
            Write(label_YA),
            Write(label_XE)
        )

        self.wait()

        scooter = VGroup(dot_A, dot_B, dot_D, dot_E, line_AB, line_BC, line_CD, line_CE, label_A, label_B, label_C, label_D, label_E, 
        label_l1, label_l2, label_l3, label_l4, dashed_line, alpha, beta, alpha_label, beta_label, F, f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_line,
        label_F, label_f, joint_1, joint_2, joint1_line, joint2_line, joint1_line1, joint1_line2, joint1_line3, Y_E, Y_A, X_E, label_YE, label_YA, label_XE)

        self.play(
            scooter.animate.shift(4 * LEFT).scale(0.8)
        )

        self.wait()


class Equilibrium(Scene):
    def construct(self):
        title = Tex(r"Impondo o Equilíbrio na Estrutura")
        F = MathTex(r"\sum \Vec{F} = \Vec{0}")
        M = MathTex(r"\sum M_A = 0")
        F.font_size = 32
        M.font_size = 32
        VGroup(title, F, M).arrange(DOWN)
        self.play(
            Write(title),
            Write(F),
            Write(M)
        )
        self.wait()

        transform_F = MathTex(r"\sum \Vec{F} = \Vec{0} \Longrightarrow \left\{\begin{array}{lc}\sum F_x = 0 \Longrightarrow X_E = 0 \\\sum F_y = 0 \Longrightarrow Y_E + Y_A = q\cdot l_1 + F \end{array}\right.")
        transform_M = MathTex(r"\sum M_A = 0 \Longrightarrow q\cdot l_1 + F\cdot (l_1+l_2\cdot \cos{\alpha}-l_3\cdot \cos{\beta}) = Y_E \cdot (l_1 + l_2\cdot\cos{\alpha} + l_4\cdot\cos{\beta})")
        transform_F.font_size = 32
        transform_M.font_size = 32
        VGroup(transform_F, transform_M).arrange(DOWN)
        self.play(
            title.animate.to_corner(UP + LEFT),
            Transform(F, transform_F),
            Transform(M, transform_M)
        )
        self.wait()