# Key character class
# Letter is a plain text representation of the key

class key_character:
    
    def __init__(self, keycode, height, width, bitmap, letter):
        self.keycode = keycode
        self.height = height
        self.width = width
        self.bitmap = bitmap
        self.letter = letter
        
    def get_keycode(self):
        return self.keycode
        
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
        
    def get_bitmap(self):
        return self.bitmap

    def get_letter(self):
        return self.letter