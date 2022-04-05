from flask import Flask
import pandas

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route("/")
def hello_values():
   app.logger.info("Received request for value")
   #df = pandas.read_excel('./app/ipca-t.xlsx','Sheet1' ).tail(12)
   df = pandas.read_excel('./app/ipca.xlsx','Sheet1').tail(12)
   app.logger.info("File readed")
   values_column = df['valor'].astype(float)
   total = 0
   for i in list(values_column):
      total += i
   app.logger.info("Total calculated, returning value of %s", total)
   return format(total, '.2f').replace('.', ',')