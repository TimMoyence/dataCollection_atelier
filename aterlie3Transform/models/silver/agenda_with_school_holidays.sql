WITH agenda AS (
    SELECT
        "titre" AS event_title,
        "description" AS event_description,
        "ville" AS event_city,
        "premiere_date_debut" AS first_start_date,
        "premiere_date_fin" AS first_end_date,
        "derniere_date_debut" AS last_start_date,
        "derniere_date_fin" AS last_end_date,
        "nom_du_lieu" AS location_name,
        "adresse" AS location_address,
        "arrondissement" AS location_arrondissement,
        "code_insee" AS location_insee,
        "code_postal" AS location_postal_code,
        "telephone_du_lieu" AS location_phone,
        "site_web_du_lieu" AS location_website,
        "liens_du_lieu" AS location_links,
        "evenement_physique_ou_en_ligne" AS event_type,
        "lien_dacces_en_ligne" AS online_event_link,
        "etat_de_levenement" AS event_status,
        "age_minimum" AS min_age,
        "age_maximum" AS max_age
    FROM {{ source('raw', 'Bordeaux_agenda') }}
),
holidays AS (
    SELECT
        "description" AS holiday_description,
        "start_date" AS holiday_start_date,
        "end_date" AS holiday_end_date,
        "location" AS holiday_location,
        "zones" AS holiday_zones,
        "annee_scolaire" AS school_year
    FROM {{ source('raw', 'calendrier_scolaire') }}
)
SELECT
    COALESCE(agenda.event_title, 'Unknown Event') AS event_title,
    agenda.event_description,
    agenda.event_city,
    agenda.first_start_date,
    agenda.first_end_date,
    holidays.holiday_start_date,
    holidays.holiday_end_date,
    holidays.holiday_description,
    holidays.holiday_zones,
    holidays.school_year
FROM agenda
LEFT JOIN holidays
    ON agenda.first_start_date BETWEEN holidays.holiday_start_date AND holidays.holiday_end_date
    OR agenda.last_start_date BETWEEN holidays.holiday_start_date AND holidays.holiday_end_date
