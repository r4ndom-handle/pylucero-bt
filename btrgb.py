import time
import sys
import math
import random
from bluepy import btle

class btrgb:
    def __init__(self, address):
        self.address = address
        self.device = btle.Peripheral(self.address)
        self.defaultcolor = [0xFF,0xFF,0xFF,0xFF]
    def changecolor(self, color=[0xFF,0xFF,0xFF,0xFF]):
        #concatenate a magic byte (0x56) with the RGBW color bytes and the trailer.  Colors can be controlled with individual byte values at other handles, but this is cleaner
        cmd = [0x7e,0x07,0x05,0x03]+ color[0:3] + [0x00,0xef]
        strcmd = "".join(chr(e) for e in cmd)
        #strcmd = str(cmd)
        print(strcmd)
        self.device.writeCharacteristic(0x000e,strcmd, withResponse=False)
    def blink(self, numblinks,color):
        for i in range(0,numblinks):
            self.changecolor([0x00,0x00,0x00,0x00])
            time.sleep(.5)
            self.changecolor(color)
            time.sleep(.1)
            self.changecolor([0x00,0x00,0x00,0x00])
    def pulse_sinewave(self,mincolor,maxcolor,cycles):
        #starts at min-color, applies a sinewave to each color value, refreshes the color, goes on for the number of cycles.  -1 is infinite
        startcolor = [int((x+y)/2) for x,y in zip(mincolor,maxcolor)]
        deltacolor = [y-x for x,y in zip(mincolor,maxcolor)]
        offset=0
        c=0
        colors=[]
        for i in range(0,360):
            colors.append([int(.5*z*math.sin(math.radians(i))+q) for q,z in zip(startcolor,deltacolor)])
        while c <> cycles:
            self.changecolor(colors[offset])
            time.sleep(.0167)
            offset += 1
            if offset >= 360:
                offset = 0
                c += 1
        
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
            else:
                for signal in morse_dictionary[letter]:
                    self.changecolor(color=[0xFF,0xFF,0xFF,0xFF])
                    time.sleep(timings[signal])
                    self.changecolor([0x00,0x00,0x00,0x00])
                    time.sleep(timings['p'])
    def flood_timer(self):
        while 1:
            starttime=time.time()
            self.changecolor([random.randint(0,255), random.randint(0,255), random.randint(0,255),random.randint(0,255)])
            endtime=time.time()
            print endtime-starttime
    def random(self,interval):
        while 1:
            self.changecolor([random.randint(0,255), random.randint(0,255), random.randint(0,255),random.randint(0,255)])
            time.sleep(interval)
    def __del__(self):
        self.disconnect()

class bttzumi(btrgb):
    def __init__(self, address):
        self.address = address
        self.device = btle.Peripheral(self.address)
        self.defaultcolor = [0xFF,0xFF,0xFF,0xFF]
        self.colorattrib = 0x000e
    def changecolor(self, color=[0xFF,0xFF,0xFF,0xFF]):
        #concatenate magic bytes (0x7e,0x07,0x05,0x03) with the RGB color bytes and the trailer. Omits 4th color byte
        cmd = [0x7e,0x07,0x05,0x03]+ color[0:3] + [0x00,0xef]
        strcmd = "".join(chr(e) for e in cmd)
        print(strcmd)
        self.device.writeCharacteristic(self.colorattrib,strcmd, withResponse=False)
        
class btmonster(btrgb):
    def __init__(self, address):
        self.address = address
        self.device = btle.Peripheral(self.address)
        self.defaultcolor = [0xFF,0xFF,0xFF,0xFF]
        self.colorattrib = 0x0008
    def changecolor(self, color=[0xFF,0xFF,0xFF,0xFF]):
        #concatenate magic bytes (0x7e,0x07,0x05,0x03) with the RGB color bytes and the trailer. Omits 4th color byte
        cmd = [0x7e,0x07,0x05,0x03]+ color[0:3] + [0x00,0xef]
        strcmd = "".join(chr(e) for e in cmd)
        print(strcmd)
        self.device.writeCharacteristic(self.colorattrib,strcmd, withResponse=False)

class btlucero(btrgb):
    def __init__(self, address):
        self.address = address
        self.device = btle.Peripheral(self.address)
        self.defaultcolor = [0xFF,0xFF,0xFF,0xFF]
        self.colorattrib = 0x002E
    def changecolor(self, color=[0xFF,0xFF,0xFF,0xFF]):
        #concatenate a magic byte (0x56) with the RGBW color bytes and the trailer.  Colors can be controlled with individual byte values at other handles, but this is cleaner
        cmd = [0x56] + color + [0xF0,0xAA]
        strcmd = "".join(chr(e) for e in cmd)
        self.device.writeCharacteristic(0x002E,strcmd, withResponse=False)
