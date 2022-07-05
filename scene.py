from multiprocessing.reduction import ACKNOWLEDGE
from telnetlib import DO
from manim import *
import math

from numpy import array, number

class Scooter(Scene):
    def construct(self):

        dicipline = Tex(r"PEF3208 - Fundamentos de Mecânica das Estruturas", font_size=32)

        group_num = Tex(r"Grupo 12 - Turma 01", font_size=32)

        hess = Text(r"Gustavo Hess Vaz de Lima - 12550601", font_size=20)
        assme = Text(r"Henrique de Andrade Assme - 11339822", font_size=20)
        bressan = Text(r"Pedro Henrique Marinho Bressan - 12551540", font_size=20)
        lucio = Text(r"Tiago Mariotto Lucio - 12550556", font_size=20)

        names = VGroup(hess, assme, bressan, lucio).arrange(DOWN)

        info_container = VGroup(dicipline, group_num, names).arrange(DOWN * 2)

        basic_description0 = Tex(r"Da caracterização estrutural de um patinete", font_size=36)
        basic_description1 = Tex(r"Uma análise dos esforços envolvidos e implicações para tensões de segurança", font_size=32)

        descriptions = VGroup(basic_description0, basic_description1).arrange(DOWN)

        first_page = VGroup(descriptions, info_container).arrange(DOWN * 6).scale(0.8)

        banner = ManimBanner().scale(0.2).to_corner(DR).shift(LEFT)

        self.play(
            Write(first_page), banner.create(), run_time=3
        )
        self.play(banner.expand())
        self.wait(2)
        self.play(Unwrite(banner))

        self.wait()

        self.play(
            FadeOut(
                first_page
            )
        )

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
            Write(line_AB), run_time=0.5
        )
        self.play(
            Write(dot_B),
            Write(line_BC), run_time=0.5
        )
        self.play(
            Write(line_CD),
            Write(line_CE), run_time=0.5
        )
        self.play(
            Write(dot_D),
            Write(dot_E), run_time=0.5
        )

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
            Write(label_E), run_time=0.5
        )

        label_l1 = MathTex(r"l_1", font_size=24).next_to(line_AB, DOWN * 0.5)
        label_l2 = MathTex(r"l_2", font_size=24).next_to(line_BC, UP * 0.1).shift(DOWN * 0.3 + RIGHT * 0.1)
        label_l3 = MathTex(r"l_3", font_size=24).next_to(line_CD, LEFT * 0.1).shift(RIGHT * 0.27 + UP * 0.1)
        label_l4 = MathTex(r"l_4", font_size=24).next_to(line_CE, LEFT * 0.3).shift(UP * 0.1 + RIGHT * 0.1)

        self.play(
            Write(label_l1),
            Write(label_l2),
            Write(label_l3),
            Write(label_l4), run_time=0.5
        )

        dashed_line = DashedLine(dot_E, dot_B, dash_length=0.05)

        self.play(
            Write(dashed_line), run_time=0.5
        )

        alpha = Angle(line_BC, dashed_line, radius=0.2, quadrant=(1, -1))
        beta = Angle(line_CE, dashed_line, radius=0.2, quadrant=(-1, 1), other_angle=True)

        self.play(
            Write(alpha),
            Write(beta), run_time=0.5
        )

        alpha_label = MathTex(r"\alpha").scale(0.4).next_to(alpha, LEFT * 0.2 - DOWN * 0.01)
        beta_label = MathTex(r"\beta").scale(0.4).next_to(beta, RIGHT * 0.2 + UP * 0.001)

        self.play(
            Write(alpha_label),
            Write(beta_label), run_time=0.5
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
            Write(f_line), run_time=0.5
        )

        label_F = MathTex(r"F", font_size=24, color=BLUE).next_to(F, 0.5 * RIGHT)
        label_f = MathTex(r"q", font_size=24, color=BLUE).next_to(f_6, 0.5 * RIGHT + 0.01 * UP)

        self.play(
            Write(label_F),
            Write(label_f), run_time=0.5
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
            Write(joint1_line3), run_time=0.5
        )

        Y_E = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(joint1_line, DOWN)
        Y_A = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(joint2_line, DOWN)
        X_E = Arrow(start=LEFT * 0.075, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(dot_E, LEFT * 1.5) 

        self.wait()

        detail4 = Tex(r"Reações Vinculares", color=ORANGE).to_corner(UP + RIGHT)

        self.play(
            Transform(detail1, detail4),
            Write(Y_E),
            Write(Y_A),
            Write(X_E), run_time=0.5
        )

        label_YE = MathTex(r"Y_E", font_size=24, color=ORANGE).next_to(Y_E, 0.4 * LEFT)
        label_YA = MathTex(r"Y_A", font_size=24, color=ORANGE).next_to(Y_A, 0.4 * LEFT)
        label_XE = MathTex(r"X_E", font_size=24, color=ORANGE).next_to(X_E, 0.4 * DOWN)

        self.play(
            Write(label_YE),
            Write(label_YA),
            Write(label_XE), run_time=0.5
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

        Sum_F2 = MathTex(r"\sum \Vec{F} = \Vec{0}", r"\Longrightarrow \left\{\begin{array}{lc}\sum F_x = 0 \Longrightarrow X_E = 0 \\ \sum F_y = 0 \Longrightarrow Y_E + Y_A = q\cdot l_1 + F \end{array}\right. } }", font_size=20)
        Sum_M2 = MathTex(r"\sum M_A = 0", r"\Longrightarrow", r"q\cdot l_1 + F\cdot (l_1+l_2\cdot \cos{\alpha}-l_3\cdot \cos{\beta}) =", r"{{ Y_E }}", r"\cdot (l_1 + l_2\cdot\cos{\alpha} + l_4\cdot\cos{\beta})", font_size=20)

        eqs2 = VGroup(Sum_F2, Sum_M2).arrange(DOWN).next_to(scooter, RIGHT + UP * 0.5, buff=1)

        self.play(
            TransformMatchingTex(Sum_F1, Sum_F2),
            TransformMatchingTex(Sum_M1, Sum_M2)
        )

        eq_XE = MathTex(r"X_E = 0", font_size=20)
        eq_YE = MathTex(r"{{ Y_E }}", r"= \dfrac{\dfrac{q\cdot l_1^2}{2} + F\cdot (l_1+l_2\cdot \cos{\alpha}-l_3\cdot \cos{\beta})}{l_1 + l_2\cdot\cos{\alpha} + l_4\cdot\cos{\beta}}", font_size=20)
        eq_YA = MathTex(r"{{ Y_A }}", r"= \dfrac{\dfrac{q\cdot l_1^2}{2} + F\cdot \cos{\beta} \cdot (l_3 + l_4) + q\cdot l_1\cdot (l_2\cdot \cos{\alpha} + l_4\cdot\cos{\beta})}{l_1 + l_2\cdot \cos{\alpha} + l_4\cdot \cos{\beta}}", font_size=20)

        eqs3 = VGroup(eq_XE, eq_YE, eq_YA).arrange(DOWN * 2).next_to(eqs2, DOWN, buff=1)

        self.play(
            Write(eq_XE),
            Write(eq_YE),
            Write(eq_YA), run_time=0.95
        )

        self.wait()

        framebox1 = SurroundingRectangle(eq_XE, buff = .1)
        framebox2 = SurroundingRectangle(eq_YE, buff=.1)
        framebox3 = SurroundingRectangle(eq_YA, buff=.1)

        self.play(
            Create(framebox1),
            Create(framebox2),
            Create(framebox3), run_time=0.8
        )

        self.play(
            FadeOut(framebox1),
            FadeOut(framebox2),
            FadeOut(framebox3), run_time=0.8
        )

        self.wait(2)

        title2 = Tex(r"Cortes na Estrutura").to_corner(UL)

        self.play(
            Transform(model, title2),
            FadeOut(eqs2),
            FadeOut(eqs3)
        )

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
            Write(label_C1), run_time=0.95
        )
        self.play(
            Write(C_2),
            Write(label_C2), run_time=0.95
        )
        self.play(
            FadeOut(label_l4),
            FadeOut(beta),
            FadeOut(beta_label),
            Write(C_3),
            Write(label_C3), run_time=0.95
        )
        self.play(
            FadeOut(label_l2),
            FadeOut(alpha),
            FadeOut(alpha_label),
            Write(C_4),
            Write(label_C4), run_time=0.95
        )

        self.wait()

        retangle_c1 = SurroundingRectangle(Line(start=C_1.get_center(), end=dot_A.get_center()))

        self.play(
            Create(retangle_c1), run_time=0.95
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
            Write(line_AC1), run_time=0.95
        )

        self.play(
            Write(dot_C1),
            Write(label_A2),
            Write(label_C1_2), run_time=0.95
        )

        self.play(
            Create(Y_A2),
            Write(label_YA2), run_time=0.95
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
            Create(label_f2), run_time=0.95
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
            Create(M_1), run_time=0.95
        )

        self.play(
            Write(label_N1),
            Write(label_V1),
            Write(label_M1), run_time=0.95
        )

        self.wait()

        x1_base = Line(UP, DOWN).scale(0.2).next_to(Y_A2, DOWN)
        x1_axis = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1).scale(0.5).next_to(x1_base, LEFT).shift(0.25 * RIGHT)
        label_x1 = MathTex(r"x_1", font_size=24).next_to(x1_axis, 0.4 * UP)

        self.play(
            Create(x1_base),
            Create(x1_axis), 
            Write(label_x1), run_time=0.95
        )

        cut_c1 = VGroup(dot_A2, dot_C1, line_AC1, label_A2, label_C1_2, Y_A2, label_YA2, f_0_2, f_1_2, f_2_2, f_3_2, f_4_2,
        f_5_2, f_6_2, f_7_2, f_8_2, f_line2, label_f2, N_1, V_1, M_1, label_N1, label_V1, label_M1, x1_base, x1_axis, label_x1)

        self.wait()

        self.play(
            cut_c1.animate.to_corner(UR).scale(0.6)
        )

        self.wait()

        subtitle1 = Tex(r"Impondo Equilíbrio na Subestrutura", font_size=24).next_to(cut_c1, 2 * DOWN)

        eq_N1 = MathTex(r"N_1 = 0", font_size=20)
        eq_V1 = MathTex(r"V_1 = q\cdot x_1 - Y_A", font_size=20)
        eq_M1 = MathTex(r"M_1 = Y_A\cdot x_1 - \dfrac{q\cdot x_1^2}{2}", font_size=20)

        eqs_C1 = VGroup(eq_N1, eq_V1, eq_M1).arrange(DOWN).next_to(subtitle1, 2 * DOWN)

        self.play(
            Write(subtitle1), run_time=0.95            
        )

        self.play(
            Write(eqs_C1), run_time=0.95
        )

        self.wait()

        framebox4 = SurroundingRectangle(eqs_C1, buff = .1)

        self.play(
            Create(framebox4), run_time=0.95
        )

        self.play(
            FadeOut(framebox4), run_time=0.95
        )

        self.wait()

        self.play(
            FadeOut(eqs_C1),
            FadeOut(cut_c1),
            FadeOut(subtitle1),
            FadeOut(retangle_c1), run_time=0.95
        )

        self.wait()

        retangle_c2 = SurroundingRectangle(Line(start=C_2.get_center(), end=dot_D.get_center())).rotate(-PI * 20/180)

        self.play(
            Create(retangle_c2), run_time=0.95
        )

        dot_D2 = Dot()
        dot_C2 = Dot().next_to(dot_D2, LEFT * 15)
        line_DC2 = Line(start=dot_D2.get_center(), end=dot_C2.get_center())

        VGroup(dot_D2, dot_C2, line_DC2).next_to(scooter, RIGHT * 15)

        label_D2 = Tex(r"D", font_size=20).next_to(dot_D2, 0.5 * DL)
        label_C2_2 = MathTex(r"C_2", font_size=20).next_to(dot_C2, 0.5 * DOWN)

        self.play(
            Write(dot_D2), Write(line_DC2), Write(dot_C2), Write(label_D2), Write(label_C2_2), run_time=0.95
        )

        F2_X = Arrow(start=RIGHT * 0.5, end=LEFT * 0.5, max_tip_length_to_length_ratio=0.2, color=BLUE).scale(2).next_to(dot_D2, 0.5 * RIGHT)
        F2_Y = Arrow(start=UP * 0.5, end=DOWN * 0.5, max_tip_length_to_length_ratio=0.2, color=BLUE).scale(2 / math.tan(70 * math.pi/180)).next_to(dot_D2, 0.5 * UP)

        label_F2X = MathTex(r"F\cdot \sin{\beta}", font_size=20, color=BLUE).next_to(F2_X, 0.5 * DOWN)
        label_F2Y = MathTex(r"F\cdot \cos{\beta}", font_size=20, color=BLUE).next_to(F2_Y, 0.5 * LEFT)

        self.play(
            Create(F2_X),
            Create(F2_Y),
            Write(label_F2X),
            Write(label_F2Y), run_time=0.95
        )

        self.wait()

        N_2 = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1, color=RED).scale(0.8).next_to(dot_C2, LEFT * 0.5, buff=.5)
        V_2 = Arrow(start=DOWN, end=UP, max_tip_length_to_length_ratio=0.1, color=GREEN).scale(0.8).next_to(dot_C2, LEFT * 0.5).shift(0.5 * UP)
        M_2 = CurvedArrow(1.2 * DOWN, 1.2 * UP, radius= -2, color=PURPLE).scale(0.6).next_to(dot_C2, LEFT).shift(0.4 * LEFT)

        label_N2 = MathTex(r"N_2", font_size=24, color=RED).next_to(N_2, 0.5 * LEFT)
        label_V2 = MathTex(r"V_2", font_size=24, color=GREEN).next_to(V_2, 0.5 * UP)
        label_M2 = MathTex(r"M_2", font_size=24, color=PURPLE).next_to(M_2, 0.5 * UP).shift(0.2 * LEFT)
        
        self.play(
            Create(N_2),
            Create(V_2),
            Create(M_2), run_time=0.95
        )

        self.play(
            Write(label_N2),
            Write(label_V2),
            Write(label_M2), run_time=0.95
        )

        x2_base = Line(UP, DOWN).scale(0.2).next_to(dot_D2, 2 * DOWN)
        x2_axis = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1).scale(0.5).next_to(x2_base, LEFT).shift(0.25 * RIGHT)
        label_x2 = MathTex(r"x_2", font_size=24).next_to(x2_axis, 0.4 * UP)

        self.play(
            Create(x2_base),
            Create(x2_axis),
            Write(label_x2), run_time=0.95
        )

        cut_c2 = VGroup(dot_D2, dot_C2, line_DC2, label_D2, label_C2_2, F2_X, F2_Y, label_F2X, label_F2Y, 
        N_2, V_2, M_2, label_N2, label_V2, label_M2, x2_base, x2_axis, label_x2)

        self.wait()

        self.play(
            cut_c2.animate.to_corner(UR).scale(0.6)
        )

        self.wait()

        subtitle2 = Tex(r"Impondo Equilíbrio na Subestrutura", font_size=24).next_to(cut_c2, 2 * DOWN)

        eq_N2 = MathTex(r"N_2 = - F\cdot \sin{\beta}", font_size=20)
        eq_V2 = MathTex(r"V_2 = F\cdot \cos{\beta}", font_size=20)
        eq_M2 = MathTex(r"M_2 = -F\cdot \cos{\beta}\cdot x_2", font_size=20)

        eqs_C2 = VGroup(eq_N2, eq_V2, eq_M2).arrange(DOWN).next_to(subtitle2, 2 * DOWN)

        self.play(
            Write(subtitle2), run_time=0.95            
        )

        self.play(
            Write(eqs_C2), run_time=0.95
        )

        self.wait()

        framebox5 = SurroundingRectangle(eqs_C2, buff = .1)

        self.play(
            Create(framebox5), run_time=0.95
        )

        self.play(
            FadeOut(framebox5), run_time=0.95
        )

        self.wait()

        self.play(
            FadeOut(eqs_C2),
            FadeOut(cut_c2),
            FadeOut(subtitle2),
            FadeOut(retangle_c2), run_time=0.95
        )

        self.wait()

        retangle_c3 = SurroundingRectangle(Line(start=C_3.get_center(), end=dot_E.get_center())).rotate(-PI * 20/180)

        self.play(
            Create(retangle_c3), run_time=0.95
        )

        dot_C3 = Dot()
        dot_E2 = Dot().next_to(dot_C3, LEFT * 15)
        line_C3E = Line(start=dot_C3.get_center(), end=dot_E2.get_center())

        VGroup(dot_C3, dot_E2, line_C3E).next_to(scooter, RIGHT * 10)

        label_E2 = Tex(r"E", font_size=20).next_to(dot_E2, 0.5 * DL)
        label_C3_2 = MathTex(r"C_3", font_size=20).next_to(dot_C3, 0.5 * DOWN)

        self.play(
            Write(dot_E2), Write(line_C3E), Write(dot_C3), Write(label_E2), Write(label_C3_2), run_time=0.95
        )

        Y_E2 = Arrow(start=DOWN * 0.5, end=UP * 0.5, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(dot_E2, DOWN)
        X_E2 = Arrow(start=LEFT * 0.075, max_tip_length_to_length_ratio=0.2, color=ORANGE).next_to(dot_E2, LEFT * 1.5) 

        label_YE2 = MathTex(r"Y_E", font_size=24, color=ORANGE).next_to(Y_E2, 0.4 * LEFT)
        label_XE2 = MathTex(r"X_E", font_size=24, color=ORANGE).next_to(X_E2, 0.4 * DOWN)

        self.play(
            Create(Y_E2),
            Create(X_E2),
            Write(label_YE2),
            Write(label_XE2), run_time=0.95
        )

        self.wait()

        N_3 = Arrow(start=LEFT, end=RIGHT, max_tip_length_to_length_ratio=0.1, color=RED).scale(0.8).next_to(dot_C3, RIGHT * 0.5, buff=.5)
        V_3 = Arrow(start=UP, end=DOWN, max_tip_length_to_length_ratio=0.1, color=GREEN).scale(0.8).next_to(dot_C3, RIGHT * 0.5).shift(0.5 * DOWN)
        M_3 = CurvedArrow(1.2 * DOWN, 1.2 * UP, radius= 2, color=PURPLE).scale(0.6).next_to(dot_C3, RIGHT).shift(0.4 * RIGHT)

        label_N3 = MathTex(r"N_3", font_size=24, color=RED).next_to(N_3, 0.5 * RIGHT)
        label_V3 = MathTex(r"V_3", font_size=24, color=GREEN).next_to(V_3, 0.5 * DOWN)
        label_M3 = MathTex(r"M_3", font_size=24, color=PURPLE).next_to(M_3, 0.5 * UP).shift(0.2 * RIGHT)
        
        self.play(
            Create(N_3),
            Create(V_3),
            Create(M_3), run_time=0.95
        )

        self.play(
            Write(label_N3),
            Write(label_V3),
            Write(label_M3), run_time=0.95
        )

        x3_base = Line(UP, DOWN).scale(0.2).next_to(Y_E2, DOWN)
        x3_axis = Arrow(start=LEFT, end=RIGHT, max_tip_length_to_length_ratio=0.1).scale(0.5).next_to(x3_base, RIGHT).shift(0.25 * LEFT)
        label_x3 = MathTex(r"x_3", font_size=24).next_to(x3_axis, 0.4 * UP)

        self.play(
            Create(x3_base),
            Create(x3_axis),
            Write(label_x3), run_time=0.95
        )

        cut_c3 = VGroup(dot_E2, dot_C3, line_C3E, label_E2, label_C3_2, Y_E2, X_E2, label_YE2, label_XE2, 
        N_3, V_3, M_3, label_N3, label_V3, label_M3, x3_base, x3_axis, label_x3)

        self.wait()

        self.play(
            cut_c3.animate.to_corner(UR).scale(0.6)
        )

        self.wait()

        subtitle3 = Tex(r"Impondo Equilíbrio na Subestrutura", font_size=24).next_to(cut_c3, 2 * DOWN)

        eq_N3 = MathTex(r"N_3 = - Y_E\cdot \sin{\beta}", font_size=20)
        eq_V3 = MathTex(r"V_3 = Y_E\cdot \cos{\beta}", font_size=20)
        eq_M3 = MathTex(r"M_3 = Y_E\cdot \cos{\beta}\cdot x_3", font_size=20)

        eqs_C3 = VGroup(eq_N3, eq_V3, eq_M3).arrange(DOWN).next_to(subtitle3, 2 * DOWN)

        self.play(
            Write(subtitle3), run_time=0.95            
        )

        self.play(
            Write(eqs_C3), run_time=0.95
        )

        self.wait()

        framebox6 = SurroundingRectangle(eqs_C3, buff = .1)

        self.play(
            Create(framebox6), run_time=0.95
        )

        self.play(
            FadeOut(framebox6), run_time=0.95
        )

        self.wait()

        self.play(
            FadeOut(eqs_C3),
            FadeOut(cut_c3),
            FadeOut(subtitle3),
            FadeOut(retangle_c3), run_time=0.95
        )

        self.wait()

        retangle_c4 = SurroundingRectangle(Line(start=C_4.get_center(), end=dot_B.get_center())).rotate(-PI * 45/180)

        self.play(
            Create(retangle_c4), run_time=0.95
        )

        dot_B2 = Dot()
        dot_C4 = Dot().next_to(dot_B2, LEFT * 10)
        line_BC4 = Line(start=dot_B2.get_center(), end=dot_C4.get_center())

        VGroup(dot_B2, dot_C4, line_BC4).next_to(scooter, RIGHT * 10)

        label_B2 = Tex(r"B", font_size=20).next_to(dot_B2, 0.5 * DL)
        label_C4_2 = MathTex(r"C_4", font_size=20).next_to(dot_C4, 0.5 * DOWN)

        self.play(
            Write(dot_B2), Write(line_BC4), Write(dot_C4), Write(label_B2), Write(label_C4_2), run_time=0.95
        )

        N_aux = Arrow(start=LEFT, end=RIGHT, max_tip_length_to_length_ratio=0.1, color=RED).scale(0.8).next_to(dot_B2, RIGHT * 0.5, buff=.5)
        V_aux = Arrow(start=UP, end=DOWN, max_tip_length_to_length_ratio=0.1, color=GREEN).scale(0.8).next_to(dot_B2, RIGHT * 0.5).shift(0.5 * DOWN)
        M_aux = CurvedArrow(1.2 * DOWN, 1.2 * UP, radius= 2, color=PURPLE).scale(0.6).next_to(dot_B2, RIGHT).shift(0.4 * RIGHT)

        label_Naux = MathTex(r"(q\cdot l_1 - Y_A) \cdot \sin{\alpha}", font_size=24, color=RED).next_to(N_aux, 0.5 * RIGHT)
        label_Vaux = MathTex(r"(q\cdot l_1 - Y_A) \cdot \cos{\alpha}", font_size=24, color=GREEN).next_to(V_aux, 0.5 * DOWN)
        label_Maux = MathTex(r"Y_A\cdot l_1 - \dfrac{q\cdot l_1^2}{2}", font_size=24, color=PURPLE).next_to(M_aux, 0.5 * UP).shift(0.2 * RIGHT)

        self.play(
            Create(N_aux),
            Create(V_aux),
            Create(M_aux),
            Write(label_Naux),
            Write(label_Vaux),
            Write(label_Maux), run_time=0.95 
        )

        self.wait()

        N_4 = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1, color=RED).scale(0.8).next_to(dot_C4, LEFT * 0.5, buff=.5)
        V_4 = Arrow(start=DOWN, end=UP, max_tip_length_to_length_ratio=0.1, color=GREEN).scale(0.8).next_to(dot_C4, LEFT * 0.5).shift(0.5 * UP)
        M_4 = CurvedArrow(1.2 * DOWN, 1.2 * UP, radius= -2, color=PURPLE).scale(0.6).next_to(dot_C4, LEFT).shift(0.4 * LEFT)

        label_N4 = MathTex(r"N_4", font_size=24, color=RED).next_to(N_4, 0.5 * LEFT)
        label_V4 = MathTex(r"V_4", font_size=24, color=GREEN).next_to(V_4, 0.5 * UP)
        label_M4 = MathTex(r"M_4", font_size=24, color=PURPLE).next_to(M_4, 0.5 * UP).shift(0.2 * LEFT)
        
        self.play(
            Create(N_4),
            Create(V_4),
            Create(M_4), run_time=0.95
        )

        self.play(
            Write(label_N4),
            Write(label_V4),
            Write(label_M4), run_time=0.95
        )

        x4_base = Line(UP, DOWN).scale(0.2).next_to(dot_B2, 2 * DOWN)
        x4_axis = Arrow(start=RIGHT, end=LEFT, max_tip_length_to_length_ratio=0.1).scale(0.5).next_to(x4_base, LEFT).shift(0.25 * RIGHT)
        label_x4 = MathTex(r"x_4", font_size=24).next_to(x4_axis, 0.4 * UP)

        self.play(
            Create(x4_base),
            Create(x4_axis),
            Write(label_x4), run_time=0.95
        )

        cut_c4 = VGroup(dot_B2, dot_C4, line_BC4, label_B2, label_C4_2, N_aux, V_aux, M_aux, label_Naux, label_Vaux, label_Maux,
        N_4, V_4, M_4, label_N4, label_V4, label_M4, x4_base, x4_axis, label_x4)

        self.wait()

        self.play(
            cut_c4.animate.to_corner(UR).scale(0.6)
        )

        self.wait()

        subtitle4 = Tex(r"Impondo Equilíbrio na Subestrutura", font_size=24).next_to(cut_c4, 2 * DOWN)

        eq_N4 = MathTex(r"N_4 = (q\cdot l_1 - Y_A) \cdot \sin{\alpha}", font_size=20)
        eq_V4 = MathTex(r"V_4 = (q\cdot l_1 - Y_A) \cdot \cos{\alpha}", font_size=20)
        eq_M4 = MathTex(r"M_4 = Y_A\cdot l_1 - \dfrac{q\cdot l_1^2}{2} - (q\cdot l_1 - Y_A)\cdot \cos{\alpha}\cdot x_4", font_size=20)

        eqs_C4 = VGroup(eq_N4, eq_V4, eq_M4).arrange(DOWN).next_to(subtitle4, 2 * DOWN)

        self.play(
            Write(subtitle4), run_time=0.95            
        )

        self.play(
            Write(eqs_C4), run_time=0.95
        )

        self.wait()

        framebox7 = SurroundingRectangle(eqs_C4, buff = .1)

        self.play(
            Create(framebox7), run_time=0.95
        )

        self.play(
            FadeOut(framebox7), run_time=0.95
        )

        self.wait()

        self.play(
            FadeOut(eqs_C4),
            FadeOut(cut_c4),
            FadeOut(subtitle4),
            FadeOut(retangle_c4), run_time=0.95
        )

        self.wait()

        title3 = Tex(r"Momentos Fletores Máximos por Subestrutura").to_corner(UL)

        self.play(
            Transform(model, title3)
        )

        M_max1 = MathTex(r"M_{max_1} = \dfrac{Y_A^2}{2\cdot q}", font_size=20)
        M_max2 = MathTex(r"M_{max_2} = -F\cdot \sin{\beta}\cdot l_3", font_size=20)
        M_max3 = MathTex(r"M_{max_3} = Y_E\cdot \cos{\beta}\cdot l_4", font_size=20)
        M_max4 = MathTex(r"M_{max_4} = Y_A\cdot l_1 - \dfrac{q\cdot l_1^2}{2}", font_size=20)

        M_maxs = VGroup(M_max1, M_max2, M_max3, M_max4).arrange(DOWN).next_to(scooter, RIGHT * 10)

        self.play(
            Write(M_maxs)
        )
 
        framebox8 = SurroundingRectangle(M_maxs, buff = .1)

        self.play(
            Create(framebox8), run_time=0.95
        )

        self.play(
            FadeOut(framebox8), run_time=0.95
        )

        self.wait()

        self.play(
            FadeOut(M_maxs)
        )

        title4 = Tex(r"Exemplo com Valores Concretos").to_corner(UL)

        self.play(
            Transform(model, title4)
        )

        v_l1 = MathTex(r"l_1 = 0,765\ m", font_size=20)
        v_l2 = MathTex(r"l_2 = 0,440\ m", font_size=20)
        v_l3 = MathTex(r"l_3 = 0,845\ m", font_size=20)
        v_l4 = MathTex(r"l_4 = 0,362\ m", font_size=20)
        v_alpha = MathTex(r"\alpha = 54^\circ", font_size=20)
        v_beta = MathTex(r"\beta = 81^\circ", font_size=20)
        v_F = MathTex(r"F = 50\ N", font_size=20)
        v_q1 = MathTex(r"q = 1242\ N/m", font_size=20)

        vs1 = VGroup(v_l1, v_l2, v_l3, v_l4).arrange(DOWN).next_to(scooter, 6 * RIGHT)
        vs2 = VGroup(v_alpha, v_beta, v_F, v_q1).arrange(DOWN).next_to(vs1, 4 * RIGHT)

        v_P = MathTex(r"P = 1000\ N\ ", r"\textrm{(peso da pessoa)}", font_size=20).next_to(VGroup(vs1, vs2), DOWN * 2)
        v_q2 = MathTex(r"q = \dfrac{P - F}{l_1} \Longrightarrow", font_size=20).next_to(v_P, DOWN)
        v_q3 = MathTex(r"q = 1,242\ N/m", font_size=20).next_to(v_q2, RIGHT)

        self.play(
            Write(vs1),
            Write(v_alpha),
            Write(v_beta),
            Write(v_F), run_time=0.95
        )

        self.play(
            Write(v_P), run_time=0.95
        )

        self.play(
            Write(v_q2),
            Write(v_q3), run_time=0.95
        )

        self.wait()

        self.play(
            TransformMatchingTex(v_q3, v_q1), run_time=0.95
        )

        self.wait()

        framebox9 = SurroundingRectangle(VGroup(vs1, vs2), color=WHITE, buff = .1)

        self.play(
            Create(framebox9), run_time=0.95
        )

        vss = VGroup(vs1, vs2, framebox9)

        self.play(
            vss.animate.to_corner(UR),
            FadeOut(v_P),
            FadeOut(v_q2)
        )

        subtitle5 = Tex(r"Reações de Apoio", color=ORANGE, font_size=20).to_corner(UL)

        eq_YE2 = MathTex(r"Y_E = 377,7\ N", color=ORANGE, font_size=20)
        eq_YA2 = MathTex(r"Y_A = 622,4\ N", color=ORANGE, font_size=20)
        eq_XE2 = MathTex(r"X_E = 0", color=ORANGE, font_size=20)

        subtitle6 = Tex(r"Momento Fletor Máximo", color=PURPLE, font_size=20).to_corner(UL)

        eq_Mmax = MathTex(r"M_{max} = 156\ N", color=PURPLE, font_size=20)

        reactions = VGroup(subtitle5, eq_YE2, eq_YA2, eq_XE2).arrange(DOWN)
        moment = VGroup(subtitle6, eq_Mmax).arrange(DOWN)

        equations = VGroup(reactions, moment).arrange(2 * DOWN).next_to(scooter, 4 * RIGHT).shift(2 * UP)

        framebox10 = SurroundingRectangle(dot_B, color=PURPLE, buff=.1).shift(RIGHT * 0.85)
        arrow_toB = CurvedArrow(eq_Mmax.get_bottom() + 0.1 * DOWN, framebox10.get_corner(DR) + 0.1 * DR, radius= -4, color=PURPLE)

        self.play(
            Write(subtitle5), run_time=0.95
        )

        self.play(
            Write(eq_YE2),
            Write(eq_YA2),
            Write(eq_XE2), run_time=0.95
        )

        self.wait()

        self.play(
            Write(subtitle6), run_time=0.95
        )

        self.play(
            Write(eq_Mmax), run_time=0.95
        )

        self.play(
            Create(framebox10),
            Create(arrow_toB), run_time=0.95
        )

        self.wait()

        title7 = Tex(r"Diagramas de Esforços Solicitantes").to_corner(UL)

        self.play(
            Transform(model, title7),
            FadeOut(scooter),
            FadeOut(vss),
            FadeOut(C_1),
            FadeOut(C_2),
            FadeOut(C_3),
            FadeOut(C_4),
            FadeOut(label_C1),
            FadeOut(label_C2),
            FadeOut(label_C3),
            FadeOut(label_C4),
            FadeOut(equations),
            FadeOut(framebox10),
            FadeOut(arrow_toB)
        )

        label_dN = MathTex(r"N\ [N]", font_size=24)
        diagram_N = SVGMobject('./svg/scooterN.svg').scale(2.3)
        label_dV = MathTex(r"V\ [N]", font_size=24)
        diagram_V = SVGMobject('./svg/scooterV.svg').scale(2.3)
        label_dM = MathTex(r"M\ [N\cdot m]", font_size=24)
        diagram_M = SVGMobject('./svg/scooterM.svg').scale(2.3)

        dN = VGroup(label_dN, diagram_N).arrange(DOWN)
        dV = VGroup(label_dV, diagram_V).arrange(DOWN)
        dM = VGroup(label_dM, diagram_M).arrange(DOWN)

        diagrams = VGroup(dN, dV, dM).arrange(2 * RIGHT)

        self.add(
            diagrams
        )

        self.wait(4)

        self.play(
            FadeOut(model),
            FadeOut(diagrams)
        )

        ty = Tex(r"Agradecemos pela atenção!", font_size=60).to_corner(UP).shift(DOWN)

        git = Tex(r"Animação disponível em: https://github.com/TiagoMLucio/PEF3208", font_size=24).next_to(ty, 2 * DOWN)

        acknowledgments0 = Tex(r"Music by Vincent Rubinetti", font_size=20)
        acknowledgments3 = Tex(r"Stream the music on Spotify:", font_size=20)
        acknowledgments1 = Tex(r"Download the music on Bandcamp:", font_size=20)
        acknowledgments2 = Tex(r"https://vincerubinetti.bandcamp.com/album/the-music-of-3blue1brown", font_size=20)
        acknowledgments3 = Tex(r"Stream the music on Spotify:", font_size=20)
        acknowledgments4 = Tex(r"https://open.spotify.com/album/1dVyjwS8FBqXhRunaG5W5u", font_size=20)

        VGroup(acknowledgments0, acknowledgments1, acknowledgments2, acknowledgments3, acknowledgments4).arrange(DOWN).to_corner(DL)

        banner = ManimBanner().to_corner(DR).scale(0.25)
        self.play(Write(ty), run_time=0.5)
        self.play(banner.create(), Write(acknowledgments0), Write(git), run_time=0.5)
        self.play(banner.expand(), Write(acknowledgments1), Write(acknowledgments2), run_time=0.5)
        self.play(Write(acknowledgments3), Write(acknowledgments4), run_time=0.5)

        self.wait(4)
