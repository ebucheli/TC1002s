# io_utilities.py
def read_vanilla(filename):
    with open(filepath, 'r') as fp:
        data = fp.read()
    data_lines = data.split('\n')
    data_f = [d.split(',') for d in data_lines]
    return data_f
