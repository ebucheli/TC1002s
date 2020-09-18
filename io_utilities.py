import pandas as pd

def load_data(filename):
    """
    Reads a csv file and returns a list of lists
    """
    with open(filename,'r') as fp:
        data = fp.read().split('\n')
    data_new = [f.split(',') for f in data if f != ""]
    data_formatted = []
    for instance in data_new:
        instance_new = []
        for value in instance:
            try:
                instance_new.append(float(value))
            except ValueError:
                instance_new.append(value)
        data_formatted.append(instance_new)
    return data_formatted
