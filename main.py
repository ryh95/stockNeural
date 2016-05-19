import produceIndicators
from strategy import strategyOne
from makeExcel import RSIExcel
from realNeural import RSINeural
filename = '50ETF'

# produceIndicators.getAllMAandRSI(filename)
# RSIExcel.makeExcel(filename)
# RSINeural.stockNeural(filename)
# # stockNeural2.stockNeural(filename)
strategyOne.strategy(filename)