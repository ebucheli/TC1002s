
filepath = './data/iris.data'

def read_vanilla(filepath):
    with open(filepath,'r') as fp:
        data = fp.read()
    data_lines = data.split('\n')
    data_half = [f.split(',') for f in data_lines]
    data_final = ''.join([str(val) for val in data_half])
    print(data_final)

   
    
    

    

    
        
