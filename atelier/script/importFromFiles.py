import duckdb


sql_import_Bordeaux_agenda = '''
DROP VIEW IF EXISTS Bordeaux_agenda;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.Bordeaux_agenda AS SELECT * FROM read_csv_auto('./atelier/data/Bordeaux_agenda.csv',normalize_names=True);
'''

sql_import_calendrier_scolaire = '''
DROP VIEW IF EXISTS calendrier_scolaire;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.calendrier_scolaire AS SELECT * FROM read_csv_auto('./atelier/data/calendrier-scolaire.csv',normalize_names=True);
'''

sql_import_chantier = '''
DROP VIEW IF EXISTS chantier;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.chantier AS SELECT * FROM read_csv_auto('./atelier/data/chantier.csv',normalize_names=True);
'''

sql_import_comptage_du_trafic_2023 = '''
DROP VIEW IF EXISTS comptage_du_trafic_2023;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.comptage_du_trafic_2023 AS SELECT * FROM read_csv_auto('./atelier/data/comptage-du-trafic-2023.csv',normalize_names=True);
'''

sql_import_equipement_public = '''
DROP VIEW IF EXISTS equipement_public;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.equipement_public AS SELECT * FROM read_csv_auto('./atelier/data/equipement_public.csv',normalize_names=True);
'''

sql_import_Lieux_parking = '''
DROP VIEW IF EXISTS Lieux_parking;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.Lieux_parking AS SELECT * FROM read_csv_auto('./atelier/data/Lieux_parking.csv',normalize_names=True);
'''

sql_import_offres_de_services_TBM = '''
DROP VIEW IF EXISTS offres_de_services_TBM;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.offres_de_services_TBM AS SELECT * FROM read_csv_auto('./atelier/data/offres-de-services-TBM.csv',normalize_names=True);
'''

sql_import_parkings_donnees_techniques_2024 = '''
DROP VIEW IF EXISTS parkings_donnees_techniques_2024;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.parkings_donnees_techniques_2024 AS SELECT * FROM read_csv_auto('./atelier/data/parkings-donnees-techniques-2024.csv',normalize_names=True);
'''

sql_import_trafic_compteur = '''
DROP VIEW IF EXISTS trafic_compteur;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.trafic_compteur AS SELECT * FROM read_csv_auto('./atelier/data/trafic_compteur.csv',normalize_names=True);
'''

sql_import_trafic_geo_compteur = '''
DROP VIEW IF EXISTS trafic_geo_compteur;
CREATE SCHEMA IF NOT EXISTS raw;
CREATE OR REPLACE TABLE raw.trafic_geo_compteur AS SELECT * FROM read_csv_auto('./atelier/data/trafic_geo_compteur.csv',normalize_names=True);
'''


with duckdb.connect('datalake.db') as con:
  con.sql(sql_import_Bordeaux_agenda)
  # con.table('raw.Bordeaux_agenda').show()
  con.sql(sql_import_calendrier_scolaire)
  # con.table('raw.calendrier_scolaire').show()
  con.sql(sql_import_chantier)
  # con.table('raw.chantier').show()
  con.sql(sql_import_comptage_du_trafic_2023)
  # con.table('raw.comptage_du_trafic_2023').show()
  con.sql(sql_import_equipement_public)
  # con.table('raw.equipement_public').show()
  con.sql(sql_import_Lieux_parking)
  # con.table('raw.Lieux_parking').show()
  con.sql(sql_import_offres_de_services_TBM)
  # con.table('raw.offres_de_services_TBM').show()
  con.sql(sql_import_parkings_donnees_techniques_2024)
  # con.table('raw.parkings_donnees_techniques_2024').show()
  con.sql(sql_import_trafic_compteur)
  # con.table('raw.trafic_compteur').show()
  con.sql(sql_import_trafic_geo_compteur)
  # con.table('raw.trafic_geo_compteur').show()