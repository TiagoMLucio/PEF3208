from telnetlib import DO
from manim import *
import math

from numpy import array, number

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
            FadeOut(detail1),
            scooter.animate.shift(4 * LEFT).scale(0.8)
        )

        title1 = Tex(r"Impondo o Equilíbrio na Estrutura").to_corner(UL)
        Sum_F1 =  MathTex(r"{{ \sum \Vec{F} = \Vec{0} }}", font_size=20)
        Sum_M1 = MathTex(r"{{ \sum M_A = 0 }}", font_size=20)

        eqs1 = VGroup(Sum_F1, Sum_M1).arrange(DOWN).next_to(scooter, RIGHT + UP * 0.5, buff=1)

        self.play(
            Transform(model, title1),
            Write(eqs1)
        )

        self.wait(2)

        Sum_F2 = MathTex(r"\sum \Vec{F} = \Vec{0}", r"\Longrightarrow \left\{\begin{array}{lc}\sum F_x = 0 \Longrightarrow X_E = 0 \\ \sum F_y = 0 \Longrightarrow Y_E + Y_A = q\cdot l_1 + F \end{array}\right. } }", font_size=20)
        Sum_M2 = MathTex(r"\sum M_A = 0", r"\Longrightarrow", r"q\cdot l_1 + F\cdot (l_1+l_2\cdot \cos{\alpha}-l_3\cdot \cos{\beta}) =", r"{{ Y_E }}", r"\cdot (l_1 + l_2\cdot\cos{\alpha} + l_4\cdot\cos{\beta})", font_size=20)

        eqs2 = VGroup(Sum_F2, Sum_M2).arrange(DOWN).next_to(scooter, RIGHT + UP * 0.5, buff=1)

        self.play(
            TransformMatchingTex(Sum_F1, Sum_F2),
            TransformMatchingTex(Sum_M1, Sum_M2)
        )

        self.wait()

        eq_XE = MathTex(r"X_E = 0", font_size=20)
        eq_YE = MathTex(r"{{ Y_E }}", r"= \dfrac{\dfrac{q\cdot l_1^2}{2} + F\cdot (l_1+l_2\cdot \cos{\alpha}-l_3\cdot \cos{\beta})}{l_1 + l_2\cdot\cos{\alpha} + l_4\cdot\cos{\beta}}", font_size=20)
        eq_YA = MathTex(r"{{ Y_A }}", r"= \dfrac{\dfrac{q\cdot l_1^2}{2} + F\cdot \cos{\beta} \cdot (l_3 - l_4) + q\cdot l_1\cdot (l_2\cdot \cos{\alpha} + l_4\cdot\cos{\beta})}{l_1 + l_2\cdot \cos{\alpha} + l_4\cdot \cos{\beta}}", font_size=20)

        eqs3 = VGroup(eq_XE, eq_YE, eq_YA).arrange(DOWN * 2).next_to(eqs2, DOWN, buff=1)

        self.play(
            Write(eq_XE),
            Write(eq_YE),
            Write(eq_YA)
        )

        self.wait()

        framebox1 = SurroundingRectangle(eq_XE, buff = .1)
        framebox2 = SurroundingRectangle(eq_YE, buff=.1)
        framebox3 = SurroundingRectangle(eq_YA, buff=.1)

        self.play(
            Create(framebox1)
        )

        self.play(
            Create(framebox2)
        )

        self.play(
            Create(framebox3)
        )

        self.play(
            FadeOut(framebox1),
            FadeOut(framebox2),
            FadeOut(framebox3)
        )

        self.wait(5)

        title2 = Tex(r"Cortes na Estrutura").to_corner(UL)

        self.play(
            Transform(model, title2),
            FadeOut(eqs1),
            FadeOut(eqs2),
            FadeOut(eqs3)
        )
        
        self.wait()

        C_1 = Line(start=UP, end=DOWN, color=PINK).scale(0.1).next_to(dot_A.get_center()).shift(0.8 * LEFT)
        C_2 = Line(start=(-1 * (RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70))), end=(RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70)), color=PINK).scale(0.1).next_to(dot_D.get_center(), -1.5 * (RIGHT * math.cos(math.pi/180 * 70) + UP * math.sin(math.pi/180 * 70))).shift(0.1 * (RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70)))
        C_3 = Line(start=(-1 * (RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70))), end=(RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70)), color=PINK).scale(0.1).next_to(dot_D.get_center(), -8 * (RIGHT * math.cos(math.pi/180 * 70) + UP * math.sin(math.pi/180 * 70))).shift(0.1 * (RIGHT * math.sin(math.pi/180 * 70) - UP * math.cos(math.pi/180 * 70)))
        C_4 = Line(start=((DOWN + LEFT) * math.cos(math.pi/180 * 45)), end=((UP + RIGHT) * math.cos(math.pi/180 * 45)), color=PINK).scale(0.1).next_to(dot_B.get_center(), (UP + LEFT) * math.sin(math.pi/180 * 45))

        label_C1 = MathTex(r"C_1", font_size=20, color=PINK).next_to(C_1, 0.4 * DOWN)
        label_C2 = MathTex(r"C_2", font_size=20, color=PINK).next_to(C_2, 0.4 * UL)
        label_C3 = MathTex(r"C_3", font_size=20, color=PINK).next_to(C_3, 0.4 * UL)
        label_C4 = MathTex(r"C_4", font_size=20, color=PINK).next_to(C_4, 0.4 * UP)

        self.play(
            Write(C_1),
            Write(label_C1)
        )
        self.play(
            Write(C_2),
            Write(label_C2)
        )
        self.play(
            FadeOut(label_l4),
            FadeOut(beta),
            FadeOut(beta_label),
            Write(C_3),
            Write(label_C3)
        )
        self.play(
            FadeOut(label_l2),
            FadeOut(alpha),
            FadeOut(alpha_label),
            Write(C_4),
            Write(label_C4)
        )

        self.wait(2)

        retangle_c1 = SurroundingRectangle(Line(start=C_1.get_center(), end=dot_A.get_center()))

        self.play(
            Create(retangle_c1)
        )

        dot_A2 = Dot()
        dot_C1 = Dot().next_to(dot_A2, LEFT * 15)
        line_AC1 = Line(start=dot_A2.get_center(), end=dot_C1.get_center())

        VGroup(dot_A2, dot_C1, line_AC1).next_to(scooter, RIGHT * 15)

        label_A2 = Tex(r"A", font_size=20).next_to(dot_A2, 0.5 * RIGHT)
        label_C1_2 = MathTex(r"C_1", font_size=20).next_to(dot_C1, 0.5 * DOWN)

        Y_A2 = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(dot_A2, DOWN)
        label_YA2 = MathTex(r"Y_A", font_size=24, color=ORANGE).next_to(Y_A2, 0.4 * LEFT)

        f_0_2 = getArrow(dot_A2, 0)
        f_1_2 = getArrow(dot_A2, -1)
        f_2_2 = getArrow(dot_A2, -2)
        f_3_2 = getArrow(dot_A2, -3)
        f_4_2 = getArrow(dot_A2, -4)
        f_5_2 = getArrow(dot_A2, -5)
        f_6_2 = getArrow(dot_A2, -6)
        f_7_2 = getArrow(dot_A2, -7)
        f_8_2 = getArrow(dot_A2, -8)


        f_line2 = Line(f_0_2.get_start(), f_8_2.get_start(), color=BLUE)
        label_f2 = MathTex(r"q", font_size=24, color=BLUE).next_to(f_0_2, 0.5 * RIGHT + 0.01 * UP)

        self.play(
            Write(dot_A2), 
            Write(line_AC1)
        )

        self.play(
            Write(dot_C1),
            Write(label_A2),
            Write(label_C1_2),
        )

        self.play(
            Create(Y_A2),
            Write(label_YA2)
        )

        self.play(
            Create(f_0_2),
            Create(f_1_2),
            Create(f_2_2),
            Create(f_3_2),
            Create(f_4_2),
            Create(f_5_2),
            Create(f_6_2),
            Create(f_7_2),
            Create(f_8_2),
            Create(f_line2),
            Create(label_f2)
        )

        N_1 = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1, color=RED).scale(0.8).next_to(dot_C1, LEFT * 0.5, buff=.5)
        V_1 = Arrow(start=DOWN, end=UP, max_tip_length_to_length_ratio=0.1, color=GREEN).scale(0.8).next_to(dot_C1, LEFT * 0.5).shift(0.5 * UP)
        M_1 = CurvedArrow(1.2 * DOWN, 1.2 * UP, radius= -2, color=PURPLE).scale(0.6).next_to(dot_C1, LEFT).shift(0.4 * LEFT)

        label_N1 = MathTex(r"N_1", font_size=24, color=RED).next_to(N_1, 0.5 * LEFT)
        label_V1 = MathTex(r"V_1", font_size=24, color=GREEN).next_to(V_1, 0.5 * UP)
        label_M1 = MathTex(r"M_1", font_size=24, color=PURPLE).next_to(M_1, 0.5 * UP).shift(0.2 * LEFT)


        self.play(
            Create(N_1),
            Create(V_1),
            Create(M_1)
        )

        self.play(
            Write(label_N1),
            Write(label_V1),
            Write(label_M1)
        )

        self.wait()

        x1_base = Line(UP, DOWN).scale(0.2).next_to(Y_A2, DOWN)
        x1_axis = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1).scale(0.5).next_to(x1_base, LEFT).shift(0.25 * RIGHT)
        label_x1 = MathTex(r"x_1", font_size=24).next_to(x1_axis, 0.4 * UP)

        self.play(
            Create(x1_base),
            Create(x1_axis),
        )

        self.play(
            Write(label_x1)
        )

        cut_c1 = VGroup(dot_A2, dot_C1, line_AC1, label_A2, label_C1_2, Y_A2, label_YA2, f_0_2, f_1_2, f_2_2, f_3_2, f_4_2,
        f_5_2, f_6_2, f_7_2, f_8_2, f_line2, label_f2, N_1, V_1, M_1, label_N1, label_V1, label_M1, x1_base, x1_axis, label_x1)

        self.wait(2)

        self.play(
            cut_c1.animate.to_corner(UR).scale(0.6)
        )

        self.wait()

        subtitle1 = Tex(r"Impondo Equilíbrio na Subestrutura", font_size=24).next_to(cut_c1, 2 * DOWN)

        eq_N1 = MathTex(r"N_1 = 0", font_size=20)
        eq_V1 = MathTex(r"V_1 = q\cdot x_1 - Y_A", font_size=20)
        eq_M1 = MathTex(r"M_1 = \dfrac{q\cdot x_1^2}{2}", font_size=20)

        eqs_C1 = VGroup(eq_N1, eq_V1, eq_M1).arrange(DOWN).next_to(subtitle1, 2 * DOWN)

        self.play(
            Write(subtitle1)            
        )

        self.play(
            Write(eqs_C1)
        )

        self.wait()

        framebox4 = SurroundingRectangle(eqs_C1, buff = .1)

        self.play(
            Create(framebox4)
        )

        self.play(
            FadeOut(framebox4)
        )

        self.wait(2)





