class Diamond:
    def number_of_left_right(self, charector, line):
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
