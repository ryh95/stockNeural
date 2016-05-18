import talib
import pandas as pd
from talib.abstract import *
import numpy as np

real_data = [135.01, 133.0, 134.0, 131.0, 133.0, 131.0]
float_data = [float(x) for x in real_data]
np_float_data = np.array(float_data)
np_out = talib.MA(np_float_data,3)
print np_out
# outputMA = talib.MA(close,timeperiod=3)
# # outputMACD = talib.MACD(close,timeperiod=3)
# outputRSI = talib.RSI(close,timeperiod=3)
# print type(close)
# print outputMA
# # print outputMACD
# print outputRSI
# print close
