from neural import stockNeural
from strategy import strategy
from tools import excel
from tools import indicators

filename = '50ETF'

type = 'binary'
list_para = [
    [12,26,9],
    [7,19,9],
    [5,35,5],
    [6,30,6],
    [6,30,9],
    [8,13,9],
    [5,10,30],
    [5,55,10],
    [6,30,3],
    [6,10,5],
    [5,34,21]
]


indicators.getAllMacdHist(filename, list_para)