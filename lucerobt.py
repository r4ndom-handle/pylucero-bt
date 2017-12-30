import pygatt
import time
import sys

class lucerobt:
    def __init__(self, address):
        self.address = address
        self.adapter = pygatt.GATTToolBackend()
        self.adapter.start()
        self.device = self.adapter.connect(address)
        self.defaultcolor = [0xFF,0xFF,0xFF,0xFF]
    def changecolor(self, color=[0xFF,0xFF,0xFF,0xFF]):
        #concatenate a magic byte (0x56) with the RGBW color bytes and the trailer.  Colors can be controlled with individual byte values at other handles, but this is cleaner
        self.device.char_write_handle(0x002E, [0x56] + color + [0xF0,0xAA])
    def blink(self, numblinks,color):
        for i in range(0,numblinks):
            self.changecolor([0x00,0x00,0x00,0x00])
            time.sleep(.5)
            self.changecolor(color)
            time.sleep(.1)
            self.changecolor([0x00,0x00,0x00,0x00])
    def disconnect(self):
        self.device.disconnect()
    def connect(self):
        self.device.connect(self.address)
    def morse(self,message,timings={'.':.2, '-':.5,'p':.2,' ':.5}):
        #Define default 'dit', 'da', element pause, and word pause timings, respectively.  Everything else goes in the dictionary below.
        morse_dictionary={
                'a':'.-',
                'b':'-...',
                'c':'-.-.',
                'd':'-..',
                'e':'.',
                'f':'..-.',
                'g':'--.',
                'h':'....',
                'i':'..',
                'j':'.---',
                'k':'-.-',
                'l':'.-..',
                'm':'--',
                'n':'-.',
                'o':'---',
                'p':'.--.',
                'q':'--.-',
                'r':'.-.',
                's':'...',
                't':'-',
                'u':'..-',
                'v':'...-',
                'w':'.--',
                'x':'-..-',
                'y':'-.--',
                'z':'--..',
                '1':'----',
                '2':'..---',
                '3':'...--',
                '4':'...._',
                '5':'.....',
                '6':'-....',
                '7':'--...',
                '8':'---..',
                '9':'----.',
                '0':'-----',
                ',':'--..--',
                '?':'..--..',
                '-':'-....-',
                '"':'.-..-.',
                '(':'-.--.',
                ')':'-.--.-',
                '=':'-...-',
                '*':'-..-',
                '+':'.-.-.',
                '@':'.--.-.',
                '\'':'.----.',
                '/':'-..-.',
                ';':'-.-.-.',
                '.':'.-.-.-'
                }
        self.changecolor([0x00,0x00,0x00,0x00])
        for letter in message:
            if letter == ' ':
                time.sleep(timings[' '])
            for signal in morse_dictionary[letter]:
                self.changecolor(color=[0xFF,0xFF,0xFF,0xFF])
                time.sleep(timings[signal])
                self.changecolor([0x00,0x00,0x00,0x00])
                time.sleep(timings['p'])
