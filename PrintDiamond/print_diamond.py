class Diamond:
    def print_diamond(self, charecter):
        pass

    def print_left_space(self, charecter):

        if charecter == "A":
            left_space = ""

        if charecter == "B":
            left_space = ".\n"

        if charecter == "C":
            left_space = "..\n.\n"

        if charecter == "D":
            left_space = "...\n..\n.\n"

        return left_space

    def print_right_space(self, charecter):
        if charecter == "A":
            right_space = ""

        if charecter == "B":
            right_space = ".\n"

        if charecter == "C":
            right_space = "..\n .\n"

        if charecter == "D":
            right_space = "...\n ..\n .\n"
        return right_space

    def print_middle_space(self, charecter):
        if charecter == "A":
            middle_space = ""

        if charecter == "B":
            middle_space = [0, 1]

        if charecter == "C":
            middle_space = [0, 1, 3]

        if charecter == "D":
            middle_space = [0, 1, 3, 5]
        return middle_space

    def count_space(self, charecter, type, line):

        if type == "middle":
            if line == 1:
                return 0
            if charecter == "C" and line == 4:
                return 1
            if charecter == "D" and line == 5:
                return 3
            if charecter == "D" and line == 6:
                return 1
            if charecter == "E" and line == 6:
                return 5
            return (line - 2) * 2 + 1
        return ord(charecter) - 65
