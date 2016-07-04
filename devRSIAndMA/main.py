import strategy
from devRSIAndMA import stockNeural

stockNeural.predict('binary',input_dim=56)
strategy.getProfit('50ETF','binary','RSIAndMA')