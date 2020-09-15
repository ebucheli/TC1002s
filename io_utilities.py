# io_utilities.py

def read_vanilla(filepath):
    with open(filepath,'r') as fp:
    	data = fp.read()

    dataLines = data.split('\n')
    dataFinal = []

    for line in dataLines:
    	dataFinal.append(line.split(','))
    	
    return dataFinal
