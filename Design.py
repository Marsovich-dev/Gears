import pygame
pygame.init()
class NoneColors():
    class Normal():
        color_main = None
        color_stroke = None
        color_text = None

    class Click():
        color_main = None
        color_stroke = None
        color_text = None

    class Lock():
        color_main = None
        color_stroke = None
        color_text = None

    class Mouse_Hover():
        color_main = None
        color_stroke = None
        color_text = None

    class Error():
        color_main = None
        color_stroke = None
        color_text = None


class Design():
    # сюда вписывать переменные, равные во всех дочерних классах:
    font_style = "Courier New"
    ################################################

    background = (50, 50, 50)

    class Surface(NoneColors):
        class Normal():
            color_main = (50, 50, 50)
            color_stroke = (255, 255, 255)

    class Slider(NoneColors):
        stroke = 0
        width = 15
        strip_color = (150, 150, 150)
        class Normal():
            color_main = (100, 100, 100)
            color_stroke = None
        class Click():
            color_main = (40, 40, 40)
            color_stroke = None
        class Lock():
            color_main = (24, 24, 24)
            color_stroke = None
        class Mouse_Hover():
            color_main = (70, 70, 70)
            color_stroke = None

    class Input_Field():
        font_h = 25
        stroke = 1
        bold_stroke = 3
        class Normal():
            color_main = (25, 25, 25)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Click():
            color_main = (100, 100, 100)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Lock():
            color_main = (24, 24, 24)
            color_stroke = (100, 100, 100)
            color_text = (100, 100, 100)

        class Mouse_Hover():
            color_main = (150, 150, 150)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Error():
            color_main = (25, 25, 25)
            color_stroke = (255, 0, 0)
            color_text = (255, 255, 255)


    class Text():
        color_main = None
        color_stroke = None
        color_text = (255, 255, 255)


    class Button():
        font_h = 25
        stroke = 1
        bold_stroke = 4
        class Normal():
            color_main = (25, 25, 25)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Click():
            color_main = (70, 70, 70)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Lock():
            color_main = (50, 50, 50)
            color_stroke = (100, 100, 100)
            color_text = (90, 90, 90)

        class Mouse_Hover():
            color_main = (50, 50, 50)
            color_stroke = (255, 255, 255)
            color_text = (255, 255, 255)

        class Error():
            color_main = (25, 25, 25)
            color_stroke = (255, 0, 0)
            color_text = (255, 255, 255)

Style = Design
