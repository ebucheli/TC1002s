#io_utilities.py

def read_vanilla(filepath):
    with open(filepath, 'r') as fp:
        data_unsorted = fp.read()
    data_lines = data_unsorted.split('\n')
    data = [f.split(',') for f in data_lines]
    return data
