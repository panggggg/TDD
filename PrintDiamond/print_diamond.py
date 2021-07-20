class Diamond:
    def print_diamond(self, charecter, line):

        convert_charecter_to_int = ord(charecter)

        line_of_diamond = self.get_line_of_diamond(
            convert_charecter_to_int=convert_charecter_to_int
        )

        number_of_charecter = self.get_number_of_charecter(
            convert_charecter_to_int=convert_charecter_to_int,
            line=line,
        )

        ### Alphabet ###
        if self.is_first_half(line=line, line_of_diamond=line_of_diamond):
            alphabet = chr(number_of_charecter)
            number_of_left_right = self.get_number_of_left_right(
                convert_charecter_to_int=convert_charecter_to_int, line=line
            )
            space_left_right = "." * int(number_of_left_right)

            number_of_middle = self.get_number_of_middle(line=line)
            space_middle = "." * int(number_of_middle)

        else:
            alphabet = self.get_invert_alphabet(
                convert_charecter_to_int=convert_charecter_to_int,
                number_of_charecter=number_of_charecter,
            )

            number_of_left_right = self.get_invert_number_of_left_right(
                convert_charecter_to_int=convert_charecter_to_int, line=line
            )
            space_left_right = "." * int(number_of_left_right)

            number_of_middle = self.get_invert_number_of_middle(
                line=line, line_of_diamond=line_of_diamond
            )
            space_middle = "." * int(number_of_middle)

        if line == 1 or line == line_of_diamond:
            number_space_of_first_line = (convert_charecter_to_int - 64) - 1
            first_line = "." * int(number_space_of_first_line)
            return f"{first_line}{alphabet}{first_line}"

        return f"{space_left_right}{alphabet}{space_middle}{alphabet}{space_left_right}"

    def count_space(self, charecter, type, line):

        number_of_charecter = ord(charecter) - 64
        if type == "middle":
            return self.count_middle(line=line, number_of_charecter=number_of_charecter)
        else:
            return self.count_left(
                number_of_charecter=number_of_charecter, line=line, charecter=charecter
            )

    def count_left(self, line, number_of_charecter, charecter):
        if line - number_of_charecter > 0:
            return line - number_of_charecter
        return number_of_charecter - 1

    def count_middle(self, line, number_of_charecter):
        if line == 1:
            return 0
        if line - number_of_charecter > 0:
            number_of_line = number_of_charecter - (line - number_of_charecter)
        else:
            number_of_line = line
        return (number_of_line - 2) * 2 + 1

    def is_first_half(self, line, line_of_diamond):
        return line <= (line_of_diamond + 1) / 2

    def get_line_of_diamond(self, convert_charecter_to_int):
        return (convert_charecter_to_int - 64) - (1 - (convert_charecter_to_int - 64))

    def get_number_of_charecter(self, convert_charecter_to_int, line):
        return ((convert_charecter_to_int - 1) * 2 + line) - (
            64
            + (
                self.get_line_of_diamond(
                    convert_charecter_to_int=convert_charecter_to_int
                )
                - 1
            )
        )

    def get_number_of_left_right(self, convert_charecter_to_int, line):
        return (convert_charecter_to_int - 64) - line

    def get_number_of_middle(self, line):
        return (line - 2) * 2 + 1

    def get_invert_alphabet(self, convert_charecter_to_int, number_of_charecter):
        return chr(convert_charecter_to_int * 2 - number_of_charecter)

    def get_invert_number_of_left_right(self, convert_charecter_to_int, line):
        return abs((convert_charecter_to_int - 64) - line)

    def get_invert_number_of_middle(self, line, line_of_diamond):
        return (line_of_diamond - line) * 2 - 1