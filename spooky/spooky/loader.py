

def data_loader(data_path):
	print("loading data ...")

	import pandas as pd
	import os
	"""Just take a data path as input and render original datasets"""
	load = lambda x: pd.read_csv(x,compression="zip")
	data_files = os.listdir(data_path)
	test, train = [load(os.path.join(data_path,i)) for i in data_files]

	return test, train
	
