import pandas as pd
import numpy as np
import random
import csv

Portfolio = pd.read_csv('stocks.csv')
todayReturn = round(random.uniform(-.05, .05), 3)
print('Market return: ' + str(todayReturn))
print('Return over market:')
for k in Portfolio:
	StockReturn = round(random.uniform(-.07, .07), 3)
	ReturnOverMarket = round(StockReturn - todayReturn, 3)
	if ReturnOverMarket >= .02:
		print(k + ': ' + str(ReturnOverMarket) + ' --> INCREASE POSITION')
	elif ReturnOverMarket <= -.02:
		print(k + ': ' + str(ReturnOverMarket) + ' --> SELL POSITION')
	else:
		print(k + ': ' + str(ReturnOverMarket) + ' --> HOLD POSITION')
#hello
