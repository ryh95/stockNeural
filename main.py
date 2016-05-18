import produceIndicators
from makeExcel import RSIExcel
from binaryNeural import RSINeural,MANeural
filename = '000905_close'

# produceIndicators.getAllMAandRSI(filename)
# RSIExcel.makeExcel(filename)
RSINeural.stockNeural(filename)
# # stockNeural2.stockNeural(filename)
# strategy.strategy(filename)