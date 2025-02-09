from constant import Constant

import keyboard
import buffer_manager
import json

class Xpandr:
    def __init__(self, bm: buffer_manager.BufferManager):
        self.keyboard = keyboard
        self.buffer_manager = bm
        self.is_shift = False
        self.alias = {}
    
    def delete_n(self, n: int):
        for _ in range(n):
            self.keyboard.press(Constant.DELETE_KEY.value)
    
    def write(self, text: str):
        assert isinstance(text, str)
        self.keyboard.write(text)
    
    def shift_up(self):
        self.is_shift = True
    
    def shift_down(self):
        self.is_shift = False
    
    def get_character(self, code):
        if self.is_shift:
            return Constant.KEY_CODE_MAPPING_SHIFT_UP.value.get(code)
        else:
            return Constant.KEY_CODE_MAPPING_SHIFT_DOWN.value.get(code)
    
    def expand(self):
        for abbr in self.alias:
            if self.buffer_manager.is_in_buffer(abbr):
                meaning = self.alias[abbr]
                self.delete_n(len(abbr))
                self.buffer_manager.clear()
                self.write(meaning)
    
    def populate_alias(self):
        with open('map.json') as f:
            m = json.load(f)
            for i in m:
                self.alias[i["abbr"]] = i["meaning"]
        pass
    
    def callback(self, event: keyboard.KeyboardEvent):
        assert isinstance(event, keyboard.KeyboardEvent)

        if event.event_type == keyboard.KEY_DOWN:
            if event.scan_code in Constant.SHIFT.value:
                self.shift_up()
            else:
                if event.scan_code == Constant.DELETE_KEY_CODE.value:
                    self.buffer_manager.delete_last()
                else:
                    char = self.get_character(event.scan_code)
                    if char:
                        self.buffer_manager.add_last(char)
                self.expand()

        else:
            if event.scan_code in Constant.SHIFT.value:
                self.shift_down()
    
    def keyboard_hook(self):
        self.keyboard.hook(self.callback, True)
    
    def keyboard_listen(self):
        self.keyboard.wait()
    
    def start(self):
        self.populate_alias()
        self.keyboard_hook()
        self.keyboard_listen()