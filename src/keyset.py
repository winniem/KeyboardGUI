# Stores a set of keys

class keyset:
    
    def __init__(self, keylist)
        self.keylist = keylist;
        
    def get_keylist(self)
        return self.keylist;
        
    def update_key(self, index, keycharacter)
        self.keylist[index] = keycharacter;