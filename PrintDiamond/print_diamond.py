class Diamond:
    def print_diamond(self, charecter):
        pass

    def print_left_and_right_space(self, charecter):

        if charecter == "A":
            list_left_space = [0]

        if charecter == "B":
            list_left_space = [0, 1]

        if charecter == "C":
            list_left_space = [0, 1, 2]

        if charecter == "D":
            list_left_space = [0, 1, 2, 3]

        return list_left_space

    def print_middle_space(self, charecter):
        if charecter == "A":
            list_left_space = [0]

        if charecter == "B":
            list_left_space = [0, 1]

        if charecter == "C":
            list_left_space = [0, 1, 3]

        if charecter == "D":
            list_left_space = [0, 1, 3, 5]
        return list_left_space
