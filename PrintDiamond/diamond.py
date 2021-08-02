class Diamond:
    def number_of_left_right(self, charector, line):
        if line == 2:
            return ord(charector) - 66
        return ord(charector) - 65