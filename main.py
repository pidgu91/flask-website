from flask import Flask, render_template
from sqlalchemy import create_engine, text
import pandas as pd
import random

app = Flask(__name__)

#connect to database
engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/quotes", pool_pre_ping=True)


@app.route('/')
def homepage():
    random_number = random.randint(1,2)
    query = f' SELECT * FROM quotes_tbl WHERE id = {random_number}'
    sql_query = pd.read_sql(query, engine)
    sql_query_quotes = sql_query['quotes']
    
    return render_template('index.html', data=sql_query_quotes.values[0])
    

if __name__ == "__main__":
    app.run(debug=True)




