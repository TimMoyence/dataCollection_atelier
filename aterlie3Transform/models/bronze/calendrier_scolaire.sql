SELECT 
"description",
"start_date",
"end_date",
"location",
"zones",
"annee_scolaire",
 FROM {{ source('raw', 'calendrier_scolaire') }}
 Where "zones" = 'Zone A'