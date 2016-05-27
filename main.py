from neural import stockNeural
from strategy import strategy
from tools import excel
from tools import indicators

filename = '50ETF'
indicator = ['MA','RSI']
type = 'binary'

indicators.getIndicators(filename, *indicator)
excel.makeExcel(filename, type=type, indicator='RSI')
stockNeural.predict(filename,type=type,indicator='RSI')

strategy.getProfit(filename,type=type,indicator='RSI')