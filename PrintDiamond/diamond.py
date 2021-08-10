class Diamond:
    def number_of_left_right(self, charector, line):

        order_of_alphabet = (ord(charector) - 64)
        line_of_diamond =  order_of_alphabet * 2 - 1

        if self._is_first_half(line=line, line_of_diamond=line_of_diamond):
            return order_of_alphabet - line
        else:
            return line - order_of_alphabet  

    def number_of_middle(self, charector, line):
        
        if line == 2:
            return 2 - 1
        if line == 3:
            return 3 + 0
        if line == 4:
            return 4 + 1
        if charector == "C":
            return line + 0
        if charector == "D":
            return line + 1
        if charector == "E":
            return line + 2

    def _is_first_half(self, line, line_of_diamond):
        return line <= (line_of_diamond + 1) / 2
        
        