from neural import stockNeural
from strategy import strategy
from tools import excel
from tools import indicators

filename = '50ETF'
list_indicator = ['MA','RSI']
type = 'binary'
indicator = 'RSI'

indicators.getIndicators(filename, *list_indicator)
excel.makeExcel(filename, type=type, indicator=indicator)
stockNeural.predict(filename,type=type,indicator=indicator,input_dim=28)

strategy.getProfit(filename,type=type,indicator=indicator)