from flask import Flask
import pandas

app = Flask(__name__)

@app.route("/")
def hello_world():
   df = pandas.read_excel('./ipca.xlsx','Sheet1').tail(12)
   total = 0
   values_column = df['valor']
   
   for i in list(values_column):
      total += i
   
   return str(format(total, '.2f'))