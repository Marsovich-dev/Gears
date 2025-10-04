class TextHandler():
    @staticmethod
    def remove_spaces(string):
        string = string.replace(' ', '')
        return string

    @staticmethod
    def replace_comma(string):
        string = string.replace(',', '.')
        return string

    @classmethod
    def float(cls, string):
        try:
            string = cls.remove_spaces(string)
            string = cls.replace_comma(string)
            return float(string)
        except:
            return False

    @classmethod
    def int(cls, string):
        try:
            string = cls.remove_spaces(string)
            string = cls.replace_comma(string)
            return int(string)
        except:
            return False