import duckdb

with duckdb.connect("file.db") as con:
    con.sql("CREATE TABLE test (i INTEGER)")
    con.sql("INSERT INTO test VALUES (42)")
    con.table("test").show()
    # the context manager closes the connection automatically
    
    


duckdb.sql("CREATE OR REPLACE TABLE nom_table AS SELECT * FROM read_csv_auto('./atelier/data/Bordeaux_agenda.csv',normalize_names=True)")