from Design import Style
class Color():
    def set_style_text(self):
        self.set_normal_color(Style.Text.color_main,
                              Style.Text.color_stroke,
                              Style.Text.color_text)
        self.repaint_to_normal_color()


    def set_style_surface(self):
        self.set_normal_color(Style.Surface.Normal.color_main,
                              Style.Surface.Normal.color_stroke,
                              None)
        self.repaint_to_normal_color()


    def set_style_slider(self):
        self.set_normal_color(Style.Slider.Normal.color_main,
                              Style.Slider.Normal.color_stroke,
                              None)

        self.set_mouse_hover_color(Style.Slider.Mouse_Hover.color_main,
                                   Style.Slider.Mouse_Hover.color_stroke,
                                   None)

        self.set_click_color(Style.Slider.Click.color_main,
                             Style.Slider.Click.color_stroke,
                             None)

        self.set_lock_color(Style.Slider.Lock.color_main,
                            Style.Slider.Lock.color_stroke,
                            None)
        self.repaint_to_normal_color()


    def set_style_input_field(self):
        self.set_normal_color(Style.Input_Field.Normal.color_main,
                              Style.Input_Field.Normal.color_stroke,
                              Style.Input_Field.Normal.color_text)

        self.set_lock_color(Style.Input_Field.Lock.color_main,
                            Style.Input_Field.Lock.color_stroke,
                            Style.Input_Field.Lock.color_text)

        self.set_mouse_hover_color(Style.Input_Field.Mouse_Hover.color_main,
                                   Style.Input_Field.Mouse_Hover.color_stroke,
                                   Style.Input_Field.Mouse_Hover.color_text)

        self.set_click_color(Style.Input_Field.Click.color_main,
                             Style.Input_Field.Click.color_stroke,
                             Style.Input_Field.Click.color_text)

        self.set_error_color(Style.Input_Field.Error.color_main,
                             Style.Input_Field.Error.color_stroke,
                             Style.Input_Field.Error.color_text)

        self.repaint_to_normal_color()


    def set_style_button(self):
        self.set_normal_color(Style.Button.Normal.color_main,
                              Style.Button.Normal.color_stroke,
                              Style.Button.Normal.color_text)

        self.set_lock_color(Style.Button.Lock.color_main,
                            Style.Button.Lock.color_stroke,
                            Style.Button.Lock.color_text)

        self.set_mouse_hover_color(Style.Button.Mouse_Hover.color_main,
                                   Style.Button.Mouse_Hover.color_stroke,
                                   Style.Button.Mouse_Hover.color_text)

        self.set_click_color(Style.Button.Click.color_main,
                             Style.Button.Click.color_stroke,
                             Style.Button.Click.color_text)

        self.set_error_color(Style.Button.Error.color_main,
                             Style.Button.Error.color_stroke,
                             Style.Button.Error.color_text)

        self.repaint_to_normal_color()


    def set_normal_color(self, color_main, color_stroke, color_text):
        self.normal_color_main = color_main
        self.normal_color_stroke = color_stroke
        self.normal_color_text = color_text
        self.repaint_to_normal_color()

    def set_mouse_hover_color(self, color_main, color_stroke, color_text):
        self.mouse_hover_color_main = color_main
        self.mouse_hover_color_stroke = color_stroke
        self.mouse_hover_color_text = color_text

    def set_click_color(self, color_main, color_stroke, color_text):
        self.click_color_main = color_main
        self.click_color_stroke = color_stroke
        self.click_color_text = color_text

    def set_lock_color(self, color_main, color_stroke, color_text):
        self.lock_color_main = color_main
        self.lock_color_stroke = color_stroke
        self.lock_color_text = color_text


    def set_error_color(self, color_main, color_stroke, color_text):
        self.error_color_main = color_main
        self.error_color_stroke = color_stroke
        self.error_color_text = color_text


    def repaint_to_custom_color(self, color_main, color_stroke, color_text):
        self.color_main = color_main
        self.color_stroke = color_stroke
        self.color_text = color_text

    def repaint_to_normal_color(self):
        self.repaint_to_custom_color(self.normal_color_main, self.normal_color_stroke, self.normal_color_text)

    def repaint_to_click_color(self):
        self.repaint_to_custom_color(self.click_color_main, self.click_color_stroke, self.click_color_text)

    def repaint_to_mouse_hover_color(self):
        self.repaint_to_custom_color(self.mouse_hover_color_main, self.mouse_hover_color_stroke, self.mouse_hover_color_text)

    def repaint_to_lock_color(self):
        self.repaint_to_custom_color(self.lock_color_main, self.lock_color_stroke, self.lock_color_text)

    def repaint_to_error_color(self):
        self.repaint_to_custom_color(self.error_color_main, self.error_color_stroke, self.error_color_text)

