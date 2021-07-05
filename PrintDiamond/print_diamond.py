class Diamond:
    def print_diamond(self, charecter, line):

        line_of_diamond = (ord(charecter) - 64) - (1 - (ord(charecter) - 64))
        first_line = str((ord(charecter) - 64) - 1)
        space = "." * int(first_line)
        return f"{space}A{space}"

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
