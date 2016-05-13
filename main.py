import makeCSV
import makeExcel
import stockNeural2
import strategy

filename = '50ETF1000'

makeCSV.makeCSV(filename)
makeExcel.makeExcel(filename)
stockNeural2.stockNeural(filename)
strategy.strategy(filename)