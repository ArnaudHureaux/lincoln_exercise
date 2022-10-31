from flask import Flask
import pandas as pd
import datetime

app = Flask(__name__)

input_path='titanic.csv'
folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
output_path='output_'+folder_time+'.csv'

df=pd.read_csv(input_path)
df['New_column']=1
df.to_csv(output_path,header=True,index=False)


@app.route('/')
def hello_world():
    text='Il y a '+str(len(df.columns))+' colonnes et '+str(len(df))+' lignes.'
    return text

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)