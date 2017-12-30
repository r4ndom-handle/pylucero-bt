import lucerobt
import sys

devaddr = sys.argv[1]
lucerobulb = lucerobt.lucerobt(devaddr)
lucerobulb.morse('helloworld.')

