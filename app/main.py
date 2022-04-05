from flask import Flask
import pandas

app = Flask(__name__)

@app.route("/")
def hello_values():
   #df = pandas.read_excel('./app/ipca-t.xlsx','Sheet1' ).tail(12)
   df = pandas.read_excel('./app/ipca.xlsx','Sheet1').tail(12)
   values_column = df['valor'].astype(float)
   total = 0
   for i in list(values_column):
      total += i
   
   return format(total, '.2f').replace('.', ',')