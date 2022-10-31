import pandas as pd
import json
import ast


def exportFileLocal(df, file_name):
    df.to_csv('data/'+file_name, header=True, index=False)


def importFileLocal(file_name):
    return pd.read_csv('data/'+file_name)


def exportFileLocalJson(dicte, file_name):
    with open('data/'+file_name, 'w') as f:
        json.dump(dicte, f)


def importFileLocalJson(file_name):
    with open('data/'+file_name) as f:
        json_str = f.read()
        dicte = ast.literal_eval(json_str)
        dicte = {'data': dicte}
        return dicte
