import pandas as pd
import numpy as np
import yfinance as yf
from datetime import date
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.stats import norm


def main(this_symbol, i):
	export = {}
	close_prices = get_prices(symbol=this_symbol)
	ln_return = get_ln_returns(close_prices)
	drift, stdev = get_drift(ln_return)
	for x in tqdm(range(i)):
		export[x] = monte_carlo(close_prices, stdev, drift).mean(axis=1).values
	dti = pd.date_range(date.today(), periods=len(export[0]), freq='D')
	export = pd.DataFrame(export, index=dti)
	return export


def get_prices(symbol='BTC-USD', start_date='2018-02-01', end_date=date.today()):
	# df = yf.download(symbol, start=start_date, end=end_date)
	# df.to_json(path_or_buf=f'datasets/jsons/{symbol}.json', orient='table')
	# print('done')
	df = pd.read_json(path_or_buf=f'datasets/jsons/{symbol}.json', orient='table')
	close_prices = df['Adj Close'].dropna(how='all', axis=0)
	return close_prices


def get_ln_returns(returns):
	ln_returns = np.log(1 + returns.pct_change())

	return ln_returns


def get_drift(returns):
	mean_return = returns.mean()
	var_return = returns.var()

	return mean_return - (0.5 * var_return), returns.std()


def monte_carlo(prices, this_stdev, drift, t_intervals=1500, iterations=10000):
	rand = norm.ppf(np.random.rand(t_intervals, iterations))
	daily_returns = np.exp(drift + this_stdev * rand)
	price_list = np.zeros_like(daily_returns)
	S0 = prices.iloc[-1]
	price_list[0] = S0
	for x in range(1, t_intervals):
		price_list[x] = price_list[x-1] * daily_returns[x]
	dti = pd.date_range(date.today(), periods=len(price_list), freq='D')
	export = pd.DataFrame(price_list, index=dti)
	return export


if __name__ == '__main__':
	name = 'BTC-USD'
	i = 10
	all_simulated_prices = main(name, i)
	print(all_simulated_prices)
	plt.figure(figsize=(10, 6))
	plt.plot(all_simulated_prices)
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(name)
	plt.yticks()
	plt.show()
