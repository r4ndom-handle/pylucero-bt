import lucerobt
import sys

devaddr = sys.argv[1]
lucerobulb = lucerobt.lucerobt(devaddr)
lucerobulb.pulse_sinewave([0x00,0xFF,0x00,0x00],[0x00,0x00,0x00,0x00],10)
lucerobulb.morse('hello world.')

