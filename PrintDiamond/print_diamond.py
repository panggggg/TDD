class Diamond:
    def print_diamond(self, charecter, line):

        line_of_diamond = (ord(charecter) - 64) - (1 - (ord(charecter) - 64))

        if line == 1:
            number_space_of_first_line = (ord(charecter) - 64) - 1
            first_line = "." * int(number_space_of_first_line)
            return f"{first_line}A{first_line}"

        if charecter == "B":
            if line == 1:
                return ".A."
            if line == 2:
                return "B.B"

        if charecter == "C":
            if line == 1:
                return "..A.."
            if line == 2:
                return ".B.B."
            if line == 3:
                return "C...C"

        if charecter == "D":
            if line == 1:
                return "...A..."
            if line == 2:
                return "..B.B.."
            if line == 3:
                return ".C...C."
            if line == 4:
                return "D.....D"

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
