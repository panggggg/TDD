class Diamond:
    def number_of_left_right(self, charector, line):

        line_of_diamond = ord(charector) - 64 + (ord(charector) - 65)

        if line < (line_of_diamond + 1) / 2:
            return ord(charector) - (64 + line)
        if charector == "B":
            return line - 2
        if charector == "C":
            return line - 3
        if charector == "D":
            return line - 4    
        return 0
        