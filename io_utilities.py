# io_utilities.py

def read_vanilla(filepath):
    with open(filepath,'r') as fp:
        data = fp.read()
    data_lines = data.split('\n')
    data_final = [f.split(',') for f in data_lines]

    return data_final

def main():
    filepath = './data/iris.data'
    data=read_vanilla(filepath)
    for f in data:
        print(f, "\n")

if __name__ == '__main__':
    main()
