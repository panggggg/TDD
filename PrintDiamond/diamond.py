class Diamond:
    def number_of_left_right(self, charector, line):

        order_of_alphabet = (ord(charector) - 64)
        line_of_diamond =  order_of_alphabet * 2 - 1

        if self._is_first_half(line=line, line_of_diamond=line_of_diamond):
            return order_of_alphabet - line
        else:
            return line - order_of_alphabet  

    def number_of_middle(self, charector, line):

        return line + (line - 3)
        

    def _is_first_half(self, line, line_of_diamond):
        return line <= (line_of_diamond + 1) / 2
        
        