from enum import Enum

class Constant(Enum):
    KEY_CODE_MAPPING_SHIFT_DOWN = {
        0x00 : 'a',
        0x01 : 's',
        0x02 : 'd',
        0x03 : 'f',
        0x04 : 'h',
        0x05 : 'g',
        0x06 : 'z',
        0x07 : 'x',
        0x08 : 'c',
        0x09 : 'v',
        0x0B : 'b',
        0x0C : 'q',
        0x0D : 'w',
        0x0E : 'e',
        0x0F : 'r',
        0x10 : 'y',
        0x11 : 't',
        0x12 : '1',
        0x13 : '2',
        0x14 : '3',
        0x15 : '4',
        0x16 : '6',
        0x17 : '5',
        0x18 : '=',
        0x19 : '9',
        0x1A : '7',
        0x1B : '-',
        0x1C : '8',
        0x1D : '0',
        0x1E : ']',
        0x1F : 'o',
        0x20 : 'u',
        0x21 : '[',
        0x22 : 'i',
        0x23 : 'p',
        0x25 : 'l',
        0x26 : 'j',
        0x27 : "'",
        0x28 : 'k',
        0x29 : ';',
        0x2A : '\\',
        0x2B : ',',
        0x2C : '/',
        0x2D : 'n',
        0x2E : 'm',
        0x2F : '.',
        0x31 : ' ',
    }

    KEY_CODE_MAPPING_SHIFT_UP = {
        0x00 : 'A',
        0x01 : 'S',
        0x02 : 'D',
        0x03 : 'F',
        0x04 : 'H',
        0x05 : 'G',
        0x06 : 'Z',
        0x07 : 'X',
        0x08 : 'C',
        0x09 : 'V',
        0x0B : 'B',
        0x0C : 'Q',
        0x0D : 'W',
        0x0E : 'E',
        0x0F : 'R',
        0x10 : 'Y',
        0x11 : 'T',
        0x12 : '!',
        0x13 : '@',
        0x14 : '#',
        0x15 : '$',
        0x16 : '^',
        0x17 : '%',
        0x18 : '+',
        0x19 : '(',
        0x1A : '&',
        0x1B : '_',
        0x1C : '*',
        0x1D : ')',
        0x1E : '}',
        0x1F : 'O',
        0x20 : 'U',
        0x21 : '{',
        0x22 : 'I',
        0x23 : 'P',
        0x25 : 'L',
        0x26 : 'J',
        0x27 : '"',
        0x28 : 'K',
        0x29 : ':',
        0x2A : '|',
        0x2B : '<',
        0x2C : '?',
        0x2D : 'N',
        0x2E : 'M',
        0x2F : '>',
        0x31 : ' ',
    }

    SHIFT_KEY_CODE = 0x38
    RIGHT_SHIFT_KEY_CODE = 0x3c
    DELETE_KEY_CODE = 0x33
    DELETE_KEY = "del"
    MAX_SIZE_ABBR = 10
    PREFIX = "!"
    SHIFT = [SHIFT_KEY_CODE, RIGHT_SHIFT_KEY_CODE]