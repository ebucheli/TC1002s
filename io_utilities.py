# io_utilities.py
import pandas as pd

def read_vanilla(filepath):
    with open(filepath,'r') as fp:
    	data = fp.read()

    dataLines = data.split('\n')
    dataFinal = []

    for line in dataLines:
    	dataFinal.append(line.split(','))
    	
    return dataFinal

def read_panda(filepath):
	names = ['sepal_length','sepal_width']
	df = pd.read_csv(filepath, names=names)

	df_filtered = df[df['sepal_length']>4.55]

	print(df_filtered)

	return df_filtered

if __name__ == '__main__':
	read_panda('./iris.data')