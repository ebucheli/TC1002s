# io_utilities.py

# io_utilities.py

filepath = './data/iris.data' #r de read

def read_vanilla(filepath):
with open (filepath ,'r') as fp:
    data = fp.read()

data_lines = data.split('\n')
data_final = [f.split(',')for f in data_lines]

print (data_final)
