import numpy
import pygame
from CalculatorMessage import CalculatorMessage
from Design import Style
from Element import Element
from Factory import Factory


class SaverViewV1(Element):
    text_font_h = 25
    btn_font_h = 20
    btn_size = (300, 50)
    surf_size = (950, 550)

    def __init__(self, surface, x, y):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(*self.surf_size)
        self.__my_surf = pygame.Surface(self.get_size())
        self.__set_objects()

    def __set_objects(self):
        x = 20
        first_y = 20
        space = 10
        y = first_y
        self.__file_name_text = Factory.Output.Create_Text(self.__my_surf, x, y, self.width,
                                                     font_h=self.text_font_h, string='Название файла: ')
        y += self.btn_size[1] + space
        self.name_input_box = Factory.Input.Create_InputBox(self.__my_surf, x, y, *self.btn_size, font_h=self.btn_font_h)
        y += self.btn_size[1] + space
        self.__txt_text = Factory.Output.Create_Text(self.__my_surf, x, y, self.width,
                                                     font_h=self.text_font_h, string='Формат txt: ')
        y += self.btn_size[1] + space
        self.save_txt_btn = Factory.Input.Create_TextButton(self.__my_surf, x, y, *self.btn_size,
                                                            font_h=self.btn_font_h, string='Сохранить ')
        y += self.btn_size[1] + space
        self.save_and_replace_txt_btn = Factory.Input.Create_TextButton(self.__my_surf, x, y, *self.btn_size,
                                                                        font_h=self.btn_font_h,
                                                                        string='Сохранить/заменить при наличии ')
        y += self.btn_size[1] + space
        self.__message = CalculatorMessage(self.__my_surf, 0, y, self.get_size()[0], self.get_size()[1] - y)

    def set_message(self, message: str, degree_of_badness):
        self.__message.set_message(message, degree_of_badness)
        self.__message.update()

    def draw(self):
        self.__my_surf.fill(Style.background)
        self.__file_name_text.draw()
        self.name_input_box.draw()
        self.__txt_text.draw()
        self.save_txt_btn.draw()
        self.save_and_replace_txt_btn.draw()
        self.__message.draw()
        self.surface.blit(self.__my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = Element.get_event_pos(event, pos)
        if pos is not None:
            pos = tuple(numpy.array(pos) - numpy.array(self.get_xy()))
        self.name_input_box.event_handler(event, pos)
        self.save_txt_btn.event_handler(event, pos)
        self.save_and_replace_txt_btn.event_handler(event, pos)
        self.__message.event_handler(event, pos)
