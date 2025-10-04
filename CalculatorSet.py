
from Factory import Factory


class CalculatorSet:
    class InputBox:
        size = (80, 35)
        font_h = 20

    class MiniButton:
        size = (35, 35)

    class Text:
        font_h = 20

    class Table:
        width_columns = (400, 120, 120)
        row_spacing = 0
        table_spacing = 20

    class View:
        size = (950, 550)

    class Catalog:
        size = (700, 300)

    class FuncBtn:
        size = (200, 35)
        x = 725
        y_first = 50
        spacing = 10
        font_h = 20


class CalculatorFactory:
    @staticmethod
    def Create_Int_InputBox(surface, x, y, string=None, active=True):
        box = Factory.Input.Create_Int_InputBox(surface, x, y, *CalculatorSet.InputBox.size, CalculatorSet.InputBox.font_h)
        if string is not None:
            box.set_string(string)
        if not active:
            box.active_false()
        return box

    @staticmethod
    def Create_Float_InputBox(surface, x, y, string=None, active=True):
        box = Factory.Input.Create_Float_InputBox(surface, x, y, *CalculatorSet.InputBox.size,
                                                  CalculatorSet.InputBox.font_h)
        if string is not None:
            box.set_string(string)
        if not active:
            box.active_false()
        return box

    @staticmethod
    def Create_Mini_Change_Button(surface, x, y):
        return Factory.Input.Create_PictureButton(surface, x, y, *CalculatorSet.MiniButton.size,
                                                  img_directory='Style//CalculateIcon.png',
                                                  colorkey=(255, 255, 255), stroke=0)

    @staticmethod
    def Create_Mini_Calculate_Button(surface, x, y):
        return Factory.Input.Create_PictureButton(surface, x, y, *CalculatorSet.MiniButton.size,
                                                  img_directory='Style//CalculateIcon.png',
                                                  colorkey=(255, 255, 255), stroke=0)

    @staticmethod
    def Create_Text_Between_Tables(surface, y, string):
        return Factory.Output.Create_Text(surface, 0, y, sum(CalculatorSet.Table.width_columns),
                                          string=string, font_h=20, bold=1)

    @staticmethod
    def Create_Func_Btn(surface, x, y, string):
        return Factory.Input.Create_TextButton(surface, x, y, *CalculatorSet.FuncBtn.size, string,
                                               font_h=CalculatorSet.FuncBtn.font_h)
