from binaryNeural import RSINeural
from makeExcel import RSIExcel
from strategy import strategybinary
from tools import indicators

filename = '50ETF'
indicator = ['MA','RSI']
type = 'rsi'

indicators.getIndicators(filename, *indicator)
RSIExcel.makeExcel(filename)
RSINeural.stockNeural(filename)
# stockNeural2.stockNeural(filename)
strategybinary.strategy(filename)