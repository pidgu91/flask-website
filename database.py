from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import random
import pandas as pd

engine = create_engine("mysql+pymysql://root:password@0.0.0.0:3306/quotes", pool_pre_ping=True)

random_number = random.randint(1,2)
query = f' SELECT * FROM quotes_tbl WHERE id = {random_number}'
sql_query = pd.read_sql(query, engine)
sql_query_quotes = sql_query['quotes']
print(sql_query_quotes[0])


#with engine.connect() as conn:
 #   random_number = random.randint(1,2)
  #  result = conn.execute(text(f"select quotes from quotes_tbl WHERE id = {random_number}"))
   # print(result.all())
    


