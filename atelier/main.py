import duckdb

with duckdb.connect("datalake.db") as con:
  con.sql("CREATE OR REPLACE TABLE Bordeaux_agenda AS SELECT * FROM read_csv_auto('./atelier/data/Bordeaux_agenda.csv',normalize_names=True)")
  con.table('Bordeaux_agenda').show()
  con.sql("CREATE OR REPLACE TABLE calendrier_scolaire AS SELECT * FROM read_csv_auto('./atelier/data/calendrier-scolaire.csv',normalize_names=True)")
  con.table('calendrier_scolaire').show()
  con.sql("CREATE OR REPLACE TABLE Lieux_parking AS SELECT * FROM read_csv_auto('./atelier/data/Lieux_parking.csv',normalize_names=True)")
  con.table('Lieux_parking').show()


# import duckdb

# with duckdb.connect("datalake.db") as db:
#     db.sql('''
#         CREATE OR REPLACE TABLE calendrier AS
#         SELECT * FROM read_csv_auto(
#         'calendrier.csv',
#         normalize_names=True
#         )
#     ''')
#     db.table('calendrier').show()