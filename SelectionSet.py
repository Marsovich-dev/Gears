from Factory import Factory
from Element import Element


class SelectView(Element):

    def draw(self):
        pass

    def event_handler(self, event, ev_pos=None):
        pass

    def update(self):
        pass


class SelectionSettings():
    btn_width = 700
    btn_height = 40
    txt_height = 50
    space = 10
    btn_font_h = 20
    txt_font_h = 25
    y = 20
    finish_btn_color_main = (80, 80, 80)

    @classmethod
    def get_full_height(cls, dictionary):
        y = cls.y
        for name_mech in dictionary:
            y += cls.txt_height + cls.space
            for name_calcul in dictionary[name_mech][1]:
                y += cls.btn_height + cls.space
        return y


class SelectionFactory():

    @staticmethod
    def Create_Select_Text(surface, x, y, string):
        return Factory.Output.Create_Text(surface, x, y, SelectionSettings.btn_width, SelectionSettings.btn_height,
                                          string, SelectionSettings.txt_font_h, bold=1, italic=0)

    @staticmethod
    def Create_Select_Button(surface, x, y, string):
        btn = Factory.Input.Create_TextButton(surface, x, y, SelectionSettings.btn_width, SelectionSettings.btn_height, string, SelectionSettings.btn_font_h, mouse_hover=0)
        btn.event_down += btn.repaint_to_click_color
        btn.event_down_out += btn.repaint_to_normal_color
        return btn




