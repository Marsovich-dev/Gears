
import numpy
import pygame
from AbsMainClasses import MainProgram
from Calculator import CalculatorV1
from Design import Style
from Saver import SaverV1
from SelectionV1 import SelectionV1
from ToolBar import ToolBar


class MainProgramV1(MainProgram):
    program_offset = (50, 50)
    program_size = (1000, 600)
    def __init__(self, surface, x, y):
        self.surface = surface
        self.set_xy(x, y)
        self.set_size(*self.program_size)
        self.__my_surf = pygame.Surface(self.get_size())
        self.__selection = SelectionV1(self.__my_surf, *self.program_offset, 850, 550)
        self.__selection.ready_event += self.update_choice
        self.__calculator = CalculatorV1(self.__my_surf, *self.program_offset)
        self.__calculator.get_save_btn().event_down += self.saver_btn_func
        self.__saver = SaverV1(self.__my_surf, *self.program_offset)
        self.__current_program = self.__selection
        self.__toolbar = ToolBar(self.__my_surf, x, y)
        self.__toolbar.set_selection_btn_func(self.selection_btn_func)
        self.__toolbar.set_calculator_btn_func(self.calculator_btn_func)
        self.__toolbar.set_saver_btn_func(self.saver_btn_func)

    def update_choice(self):
        self.__calculator.set_choice(self.__selection.get_choice())
        self.__calculator.update()
        self.__current_program = self.__calculator
        self.__toolbar.horizont_toolbar.set_calculator_btn_bold_stroke()
        self.__toolbar.vertical_toolbar.set_calculator_btn_bold_stroke()

    def draw(self):
        self.__my_surf.fill(Style.background)
        self.__toolbar.draw()
        self.__current_program.draw()
        self.surface.blit(self.__my_surf, self.get_xy())

    def event_handler(self, event, pos=None):
        pos = self.get_event_pos(event, pos)
        if pos is not None:
            pos = tuple(numpy.array(pos) - numpy.array(self.get_xy()))
        self.__toolbar.event_handler(event, pos)
        self.__current_program.event_handler(event, pos)

    def selection_btn_func(self):
        self.__current_program = self.__selection

    def calculator_btn_func(self):
        self.__current_program = self.__calculator

    def saver_btn_func(self):
        self.__current_program = self.__saver
        self.__saver.set_model(self.__calculator.get_model())
        self.__toolbar.horizont_toolbar.set_saver_btn_bold_stroke()
        self.__toolbar.vertical_toolbar.set_saver_btn_bold_stroke()
