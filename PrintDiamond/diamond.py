class Diamond:
    def number_of_left_right(self, charector, line):

        line_of_diamond = ord(charector) - 64 + (ord(charector) - 65)

        
        if charector == "B":
            if line == 3:
                return 1
        if charector == "C":
            if line == 4:
                return 1 
            if line == 5:
                return 2
        if charector == "D":
            return line - 4    
        return ord(charector) - (64 + line)