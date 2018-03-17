# Key character class

class key_character:
    
    def __init__(self, keycode, height, width, bitmap)
        self.keycode = keycode;
        self.height = height;
        self.width = width;
        self.bitmap = bitmap;
        
    def get_keycode(self)
        return self.keycode
        
    def get_height(self)
        return self.height
    
    def get_width(self)
        return self.width
        
    def get_bitmap(self)
        return self.bitmap