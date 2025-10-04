from InputBox import InputBox
from Design import Style
from TextButton import TextButton
from PictureButton import PictureButton
from Text import Text
from Picture import Picture

int_num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
float_num = (*int_num, '.', ',')

class Factory():
    class Input():
        @staticmethod
        def Create_InputBox(surface, x, y, width, height, font_h):
            return InputBox(surface, x, y, width, height, font_h)

        @staticmethod
        def Create_Float_InputBox(surface, x, y, width, height, font_h):
            inputbox = InputBox(surface, x, y, width, height, font_h)
            inputbox.set_valid_characters(float_num)
            return inputbox

        @staticmethod
        def Create_Int_InputBox(surface, x, y, width, height, font_h):
            inputbox = InputBox(surface, x, y, width, height, font_h)
            inputbox.set_valid_characters(int_num)
            return inputbox

        @staticmethod
        def Create_TextButton(surface, x, y, width, height, string=None, font_h=Style.Button.font_h,
                              mouse_hover=False, bold=False, italic=False,
                              stroke=Style.Button.stroke):
            return TextButton(surface, x, y, width, height, string, font_h, mouse_hover, bold, italic, stroke)

        @staticmethod
        def Create_PictureButton(surface, x, y, width, height,
                                 img_directory=None, mouse_hover=False,
                                 stroke=Style.Button.stroke, colorkey=None):
            return PictureButton(surface, x, y, width, height, img_directory, mouse_hover, stroke, colorkey)

    class Output():
        @staticmethod
        def Create_Text(surface, x, y, width, height=None,
                        string=None, font_h=None, line_spacing=0,
                        font_style=Style.font_style, bg_stroke=0,
                        bold=False, italic=False):
            return Text(surface, x, y, width, height, string, font_h, line_spacing, font_style, bg_stroke, bold, italic)

        @staticmethod
        def Create_Picture(surface, x, y, width_lim, height_lim, img_directory, center=False, colorkey=None):
            return Picture(surface, x, y, width_lim, height_lim, img_directory, center, colorkey)
