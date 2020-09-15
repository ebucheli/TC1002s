def readvanilla():
    filepath ='./iris.data'
    with open(filepath,'r') as fp:
        data = fp.read()

    data_lines = data.split('\n')

    data_final = [f.split(',') for f in data_lines]

    return data_final

if __name__ == '__main__':
    print(readvanilla())
