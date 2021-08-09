class Diamond:
    def number_of_left_right(self, charector, line):

        line_of_diamond = ord(charector) - 64 + (ord(charector) - 65)

        if line <= (line_of_diamond + 1) / 2:
            return ord(charector) - (64 + line)
        return line - (ord(charector) - 64)    
        
        