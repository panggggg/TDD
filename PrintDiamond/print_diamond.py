class Diamond:
    def print_diamond(self, charecter, line):

        line_of_diamond = (ord(charecter) - 64) - (1 - (ord(charecter) - 64))

        convert_charecter_to_int = ord(charecter) - 1

        ### Alphabet ###
        if line <= (line_of_diamond + 1) / 2:
            alphabet = chr(
                (convert_charecter_to_int * 2 + line) - (64 + (line_of_diamond - 1))
            )
        else:
            alphabet = "A"

        number_of_left_right = (ord(charecter) - 64) - line
        space_left_right = "." * int(number_of_left_right)

        number_of_middle = (line - 2) * 2 + 1
        space_middle = "." * int(number_of_middle)

        ###########################
        number_of_invert_middle = (line_of_diamond - line) * 2 - 1
        invert_space_middle = "." * int(number_of_invert_middle)

        invert_number_of_left_right = abs((ord(charecter) - 64) - line)
        invert_space_left_right = "." * int(invert_number_of_left_right)

        if line == 1 or line == line_of_diamond:
            number_space_of_first_line = (ord(charecter) - 64) - 1
            first_line = "." * int(number_space_of_first_line)
            return f"{first_line}{alphabet}{first_line}"

        if charecter == "B":
            if line == 1:
                return f"{space_left_right}{alphabet}{space_middle}{alphabet}{space_left_right}"
            if line == 2:
                return f"{space_left_right}{alphabet}{space_middle}{alphabet}{space_left_right}"

        if charecter == "C":
            if line == 1:
                return "..A.."
            if line == 2:
                return ".B.B."
            if line == 3:
                return f"{alphabet}{space_middle}{alphabet}"
            if line == 4:
                return ".B.B."

        if charecter == "D":
            if line == 1:
                return f"{space_left_right}{alphabet}{space_left_right}"
            # find invert middle
            if line == 5:
                return f"{invert_space_left_right}C{invert_space_middle}C{invert_space_left_right}"
            if line == 6:
                return f"{invert_space_left_right}B{invert_space_middle}B{invert_space_left_right}"
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
