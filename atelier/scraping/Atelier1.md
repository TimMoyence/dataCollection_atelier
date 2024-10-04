### Étape 1 - Périmètre d'analyse : Facteurs influençant le trafic routier de la rocade bordelaise

1. **Accidents ou incidents routiers**
   - Les accidents, incidents, ou pannes peuvent créer des ralentissements importants.

2. **Travaux ou fermetures de routes**
   - Les travaux routiers et fermetures temporaires ont un impact direct sur le trafic.

3. **Jours de la semaine (télétravail)**
   - Les tendances du télétravail, notamment les jours de milieu de semaine, influencent la circulation.

4. **Horaires (historique des bouchons)**
   - Les embouteillages se forment souvent à des heures spécifiques (heures de pointe).

5. **Conditions météorologiques**
   - Les intempéries, comme la pluie ou la neige, modifient les comportements routiers.

6. **Événements locaux**
   - Les festivals, événements sportifs ou culturels peuvent augmenter le trafic dans certaines zones.

7. **Périodes de vacances scolaires**
   - Pendant les vacances, les habitudes de conduite changent, impactant la circulation.

8. **Présence et nombre de places de parking relais**
   - Les parkings relais peuvent diminuer le nombre de véhicules entrant dans la ville.

9. **Usage des vélos**
   - L'adoption des vélos pour les déplacements quotidiens peut réduire le trafic.

10. **Réseaux de transport en commun**
    - L'efficacité et la fréquence des transports en commun influencent la réduction du trafic automobile.


### Étape 2 - Sources de données pour chaque facteur

1. **Accidents ou incidents routiers**
   - Source : [ONISR - Indicateurs labellisés](https://www.onisr.securite-routiere.gouv.fr/outils-statistiques/indicateurs-labellises), [Data Gouv - Bases de données annuelles des accidents](https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2022/)
   - Travail : Analyse des données historiques sur les accidents, recoupement avec les horaires de pointe et les conditions météorologiques.

2. **Travaux ou fermetures de routes**
   - Source : [Chantiers sur la ville de Bordeaux](https://shorturl.at/ZN0Qv), [Arrêtés temporaires de circulation (ATC) actifs sur Bordeaux](https://shorturl.at/dprMj)
   - Travail : Suivi en temps réel des fermetures de routes et des chantiers pour prédire les impacts sur le trafic.

3. **Jours de la semaine (télétravail)**
   - Source : A trouver
   - Travail : Analyse des tendances en télétravail sur certains jours de la semaine et leurs impacts sur la réduction du trafic.

4. **Horaires (historique des bouchons)**
   - Source : [Comptage du trafic 2023 Bordeaux Métropole](https://opendata.bordeaux-metropole.fr/explore/dataset/comptage-du-trafic-2023-bordeaux-metropole/information/)
   - Travail : Analyse des données horaires pour comprendre les heures de pointe et les pics de trafic.

5. **Conditions météorologiques**
   - Source : [OpenWeatherMap API](https://openweathermap.org/api), [Météo France](https://www.meteofrance.com/)
   - Travail : Intégration des données météorologiques en temps réel pour corréler avec les variations de trafic.

6. **Événements locaux**
   - Source : [Agenda Bordeaux Métropole](https://shorturl.at/1Ta1U)
   - Travail : Collecte des événements locaux qui pourraient provoquer des pics de trafic ponctuels.

7. **Périodes de vacances scolaires**
   - Source : [Calendrier des vacances scolaires](https://explore.data.gouv.fr/fr/datasets/5889d03ea3a72974cbf0d5b0/#/resources/9957d723-346e-4317-8cb3-293c94e19b2d)
   - Travail : Recoupement avec les périodes de baisse ou de hausse du trafic pour modéliser les comportements pendant les vacances.

8. **Présence et nombre de places de parking relais**
   - Source : [Géolocalisation des parkings](https://opendata.bordeaux-metropole.fr/explore/dataset/st_park_p/information/), [Données techniques des parkings](https://opendata.bordeaux-metropole.fr/explore/dataset/parkings-donnees-techniques-2024/information/)
   - Travail : Modélisation de l'impact des parkings relais sur la réduction du trafic urbain.

9. **Usage des vélos**
   - Source : [Emplacement de freefloating bordelais](https://opendata.bordeaux-metropole.fr/explore/dataset/st_freefloating_s/information/?disjunctive.nom_commune)
   - Travail : Analyse des données d'utilisation des vélos en libre-service pour modéliser l'impact sur le trafic.

10. **Réseaux de transport en commun**
    - Source : [Offre de transport TBM en temps réel](https://shorturl.at/0Ipb4)
    - Travail : Corrélation entre l'efficacité des transports en commun et la réduction du trafic automobile.

---

### Étape 3 - Ingestion dans un Datalake

Vous pouvez maintenant installer **DuckDB** et commencer l'ingestion de données dans un datalake avec les principales sources identifiées.

Exemple d’ingestion d’une source de données :

```bash
pip install duckdb
```

Ouvrir une connexion persistente avec DuckDB :

```python
import duckdb

# Ouvrir une connexion persistente
con = duckdb.connect(database='datalake.db', read_only=False)
```

Charger un fichier CSV contenant les données de trafic historique, par exemple :

```sql
CREATE OR REPLACE TABLE trafic_historique AS
SELECT * FROM read_csv_auto(
    'trafic_historique.csv',
    normalize_names=True
)
```