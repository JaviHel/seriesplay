class AsciiFrame:
    """ Encierra el texto del terminal en una caja ASCII"""
    def __init__(self, width):
        self.width = width
        self.ver = "║"
        self.hor = "═"
        self.tl = "╔"
        self.tr = "╗"
        self.bl = "╚"
        self.br = "╝"
        self.ul = "╠"
        self.ur = "╣"
        self.separator = " "
        
 
    def __top(self):
        box = ""
        
        for i in range(self.width):
            if i == 0:
                box += self.tl
            elif i == self.width-1:
                box += self.tr
            else:
                box += self.hor
        
        return box
    
    
    def __union(self): # Union Top and Bottom
        box = ""
        for i in range(self.width):
            if i == 0:
                box += self.ul
            elif i == self.width-1:
                box += self.ur
            else:
                box += self.hor
        
        return box
        
    
    def __bottom(self):
        box = ""
        
        for i in range(self.width):
            if i == 0:
                box += self.bl
            elif i == self.width-1:
                box += self.br
            else:
                box += self.hor
        
        return box    
        
        
    def __middle(self, message, separator=" "):
        """ 
        Prints the message center aligned
        """
        box = ""
        indent = (self.width-len(message)-1)//2
        message_length = len(message)
        
        for i in range(self.width-message_length):
            if i == 0  or i == self.width-message_length-1:
                box += self.ver
                
            if i == indent:
                box += message
            elif i < self.width-message_length-1:
                box += separator
        return box
        
            
    def __middle_left(self, message, separator=" "):
        """
        Prints the message aligned to the left
        """
        box = ""
        message_length = len(message)
        
        for i in range(self.width-message_length):
            if i == 0  or i == self.width-message_length-1:
                box += self.ver   
                
            if i == 0:
                box += message
            elif i < self.width-message_length-1:
                box += separator
                
        return box
        
        
    def __middle_right(self, message, separator=" "):
        """
        Prints the message aligned to the right
        """
        box = ""
        message_length = len(message)
        
        for i in range(self.width):
            if i == 0  or i == self.width-1:
                box += self.ver
                
            if i == self.width-message_length-1:
                box += message
            elif 0 < i < self.width-message_length-1:
                box += separator
                
        return box
    
    
    def print_space(self, separator=" "):
        """ Adds Vertical Space with borders """
        if len(separator) > 1: 
            separator = separator[0]
        elif len(separator) <= 0:
            separator = " "
        print(self.__middle("", separator))
        
            
    def print_box(self, side="top"):
        """ Prints the selected side of the box """
        if side.upper() == "TOP" or side.upper() == "T":
            print(self.__top())
            return True
        
        elif side.upper() == "CENTER" or side.upper() == "C":
            print(self.__union())
            return True
            
        elif side.upper() == "BOTTOM" or side.upper() == "B":
            print(self.__bottom())
            return True
        
        return False    
        
        
    def print_text(self, text, indent="left", separator=" "):
        
        if len(separator) > 1:    separator = separator[0]
        elif len(separator) <= 0: separator = " "
        
        if indent.upper() == "LEFT" or indent.upper() == "L":
            print(self.__middle_left(text, separator))
            return True
        
        elif indent.upper() == "CENTER" or indent.upper() == "C":
            print(self.__middle(text, separator))
            return True
        
        elif indent.upper() == "RIGHT" or indent.upper() == "R":
            print(self.__middle_right(text, separator))
            return True
         
        return False


        



