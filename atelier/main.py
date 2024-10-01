import duckdb

with duckdb.connect("datalake.db") as con:
    con.sql("CREATE TABLE test (i INTEGER)")
    con.sql("INSERT INTO test VALUES (42)")
    con.table("test").show()
    # the context manager closes the connection automatically
    
    


duckdb.sql("CREATE OR REPLACE TABLE Bordeaux_agenda AS SELECT * FROM read_csv_auto('./atelier/data/Bordeaux_agenda.csv',normalize_names=True)")
duckdb.table('Bordeaux_agenda').show()