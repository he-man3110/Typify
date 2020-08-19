import speech_recognition as sr 
import ctypes
import time
from pynput.keyboard import Key, Controller 

__author__ = "Rooney3110"
__version__ = "2.0"

Virtual_Keyboard = Controller()

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



_alphanum = [' ','0','1','2','3','4','5','6','7','8','9',
                'q','w','e','r','t','y','u','i','o','p',
                '[',']','\\','a','s','d','f','g','h','j',
                'k','l',';','\'','`','z','x','c','v','b',
                'n','m',',','.','/','*','-','=','+']
_scan_code = [ 0x39,0x0B,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,
                0x10,0x11,0x12,0x13,0x14,0x15,0x16,0x17,0x18,0x19,
                0x1A,0x1B,0x2B,0x1E,0x1F,0x20,0x21,0x22,0x23,0x24,
                0x25,0x26,0x27,0x28,0x29,0x2C,0x2D,0x2E,0x2F,0x30,
                0x31,0x32,0x33,0x34,0x35,0x37,0x0C,0x0D,0x4E]

def _translate(val):
    try:
        itr = 0
        while str(val) != _alphanum[itr]:
            itr += 1
        return _scan_code[itr]
    except :
        return 0x39

'''
def StartWriting(string_obj, speed=0.5):
    try:
        for letter in string_obj:
            time.sleep(speed)
            if letter.isupper():
                letter = letter.lower()
            hexky = _translate(letter)
            PressKey(hexky)
        return True
    except:
        return False 

'''
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        google_response = r.recognize_google(audio)
        return google_response   
    except:
        return ""

def record_active(active_signal):
    string_info = []
    while active_signal == False:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        try:
            google_response = r.recognize_google(audio)
            string_info.append(google_response)   
        except:
            pass
    for each_string in string_info:
        StartWriting(each_string)

def StartWriting(string_obj):
    try:
        for letter in string_obj:
            if letter == " ":
                time.sleep(0.3)
            else:
                time.sleep(0.1)
            if letter.isupper():
                letter = letter.lower()
            #hexky = _translate(letter)
            Virtual_Keyboard.press(letter)
            Virtual_Keyboard.release(letter)
            #PressKey(hexky)
        return True
    except:
        return False 


if __name__ == "__main__":
    pass