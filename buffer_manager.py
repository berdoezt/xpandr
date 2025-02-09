from constant import Constant

class BufferManager:

    def __init__(self):
        self.buffer = ""
    
    def delete_last(self):
        if len(self.buffer) > 0:
            self.buffer = self.buffer[:-1]
    
    def clear(self):
        self.buffer = ""
    
    def is_in_buffer(self, text):
        return text in self.buffer
    
    def add_last(self, char):
        if len(self.buffer) >= Constant.MAX_SIZE_ABBR.value or char == Constant.PREFIX.value:
            self.clear()
        
        self.buffer += char
    pass

