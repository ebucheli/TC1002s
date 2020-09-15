import pandas as pd

def readvanilla():
    # Reads Dataset and stores results in dictionary
    # Only for python3.8
    data = {"S_L":[],"S_W":[],"P_L":[],"P_W":[],"CL":[]}
    filepath = "data/iris.data"
    with open(filepath,"r") as f:
        while (line:=f.readline().strip("\n").split(",")) and len(line) == len(data.keys()):
            for idx,key in enumerate(data.keys()):
                try:
                    data[key].append(float(line[idx]))
                except ValueError as e:
                    data[key].append(line[idx])
    return data


def read_pandas(filepath, names):
    """
    Read a csv in pandas
    returns a pandas dataframe
    """
    df = pd.read_csv(
        filepath,
        names=names,
    )

    return df


if __name__ == "__main__":
    filepath = "./data/iris.data"
    names = ['sepal_length','sepal_width','petal_length','petal_width','class']
    df = read_pandas(filepath, names)
    # print(df.head(10))
    #
    # sepal_length = df['sepal_length'].to_list()
    # print(sepal_length)
    #
    # df['sl+pl'] = df['sepal_length'] + df['petal_length']
    #
    # print(df.head())

    df_filtered = df[df['sepal_length']<4.55]

    print(df_filtered)

    print(df_filtered['sepal_width'].std())
