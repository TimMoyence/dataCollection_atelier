### 1. **Data Pipeline**
   Processus automatisé permettant de déplacer des données d'une source à une destination, tout en les transformant et les enrichissant en chemin.

### 2. **ETL (Extract, Transform, Load)**
   Méthodologie de gestion de données où les données sont d'abord extraites (extract), puis transformées (transform) et finalement chargées (load) dans un système de stockage.

### 3. **ELT (Extract, Load, Transform)**
   Variante de l'ETL où les données sont extraites et chargées dans un entrepôt de données, puis transformées ultérieurement dans cet entrepôt.

### 4. **Data Warehouse**
   Un grand système de stockage conçu pour regrouper et organiser des données provenant de plusieurs sources, souvent utilisé pour l'analyse et la génération de rapports.

### 5. **Data Lake**
   Un dépôt de données non structurées ou semi-structurées à grande échelle, utilisé pour stocker de vastes quantités de données brutes avant qu'elles ne soient traitées ou analysées.

### 6. **Data Mart**
   Un sous-ensemble d'un data warehouse conçu pour répondre à des besoins spécifiques, souvent par domaine ou par service au sein d'une organisation.

### 7. **Transformation**
   Processus de modification ou d'amélioration des données brutes en vue de leur analyse. Cela inclut le nettoyage, la normalisation, et l'enrichissement des données.

### 8. **Schema**
   Structure ou organisation des données dans une base de données, définissant les tables, les colonnes et leurs types de données.

### 9. **Source**
   L'emplacement ou le système à partir duquel les données sont extraites, comme une base de données, une API, ou un fichier CSV.

### 10. **Target (Cible)**
   L'emplacement où les données sont stockées après avoir été transformées, généralement un entrepôt de données ou un data mart.

### 11. **Model (Modèle)**
   Un ensemble d'instructions ou de règles définissant la manière dont les données doivent être structurées, transformées ou analysées.

### 12. **DBT (Data Build Tool)**
   Outil de transformation de données qui permet de modéliser, transformer et valider des données dans un data warehouse à l'aide de SQL et de bonnes pratiques de développement.

### 13. **Materialization**
   Concept dans DBT et d'autres outils, décrivant comment les données transformées sont stockées, par exemple sous forme de tables ou de vues dans un entrepôt de données.

### 14. **Incremental Load**
   Chargement partiel de données dans une table, généralement utilisé pour ajouter seulement les nouvelles données ou mettre à jour les données existantes sans recharger l'ensemble.

### 15. **Full Refresh**
   Processus de recharge complète d'une table dans l'entrepôt de données, souvent utilisé pour s'assurer que toutes les données sont actuelles.

### 16. **Staging Table**
   Table temporaire utilisée pour stocker des données brutes ou intermédiaires avant qu'elles ne soient transformées ou insérées dans une table de production.

### 17. **Granularity**
   Niveau de détail des données, par exemple, des transactions individuelles par jour ou des totaux mensuels.

### 18. **Fact Table**
   Table dans un entrepôt de données qui stocke les données quantitatives (mesures) sur lesquelles sont effectuées des analyses.

### 19. **Dimension Table**
   Table dans un entrepôt de données contenant des attributs descriptifs ou catégoriels pour compléter les faits.

### 20. **Primary Key (Clé primaire)**
   Identifiant unique pour chaque ligne dans une table, permettant de garantir que chaque enregistrement est distinct.

### 21. **Foreign Key (Clé étrangère)**
   Une colonne ou un ensemble de colonnes dans une table qui fait référence à la clé primaire d'une autre table, créant ainsi une relation entre les deux tables.

### 22. **JOIN**
   Opération SQL permettant de combiner des données provenant de plusieurs tables en une seule table de résultat, en fonction d'une condition donnée (souvent une clé étrangère).

### 23. **Aggregation**
   Processus de regroupement et de synthèse des données à partir de multiples enregistrements, comme la somme, la moyenne, le minimum, ou le maximum.

### 24. **Partitioning**
   Technique permettant de diviser une table ou une base de données en segments plus petits et plus gérables, souvent basée sur des valeurs spécifiques (par exemple, date, région).

### 25. **Indexing**
   Technique utilisée pour accélérer la recherche et la récupération des données dans une base de données en créant des index sur des colonnes clés.

### 26. **Data Cleansing (Nettoyage de données)**
   Processus de correction ou de suppression de données erronées, incomplètes, ou redondantes pour améliorer la qualité des données.

### 27. **Data Governance**
   Ensemble de règles, de processus et de normes garantissant la gestion sécurisée et l'utilisation appropriée des données au sein d'une organisation.

### 28. **Metadata**
   Données descriptives sur les données elles-mêmes, comme leur source, format, date de création, et toute transformation qui leur a été appliquée.

### 29. **Lagging Indicator**
   Mesure ou indicateur qui reflète des événements passés dans les données, souvent utilisé pour évaluer des performances antérieures.

### 30. **Leading Indicator**
   Mesure ou indicateur qui anticipe ou prédit des événements futurs, utilisé pour prévoir des tendances ou des changements dans les données.

### 31. **BI (Business Intelligence)**
   Ensemble de technologies et de processus utilisés pour collecter, stocker et analyser des données afin de soutenir la prise de décision au sein d'une organisation.

### 32. **Data Visualization**
   Représentation graphique des données, souvent utilisée pour découvrir des tendances ou des insights dans les données analysées.

### 33. **KPI (Key Performance Indicator)**
   Indicateur clé de performance utilisé pour mesurer et suivre l'efficacité ou le succès d'une activité ou d'un processus particulier.

### 34. **SQL (Structured Query Language)**
   Langage utilisé pour interagir avec des bases de données relationnelles, permettant la création, la lecture, la mise à jour et la suppression de données.

### 35. **Data Modeling**
   Processus de création de modèles abstraits pour organiser et structurer les données dans une base de données.

### 36. **Analytics**
   Processus de découverte, d'interprétation et de communication de modèles dans les données pour aider à la prise de décision.

### 37. **Machine Learning**
   Branche de l'intelligence artificielle permettant à des systèmes d'apprendre à partir des données et de prendre des décisions ou des prévisions basées sur ces apprentissages.

### 38. **Overfitting**
   Erreur en apprentissage automatique où un modèle est trop adapté aux données d'entraînement, et échoue à bien généraliser sur de nouvelles données.

### 39. **Underfitting**
   Erreur inverse de l'overfitting où un modèle est trop simple et ne capture pas suffisamment les relations dans les données.

### 40. **Base de Données (Database)**
   Un ensemble organisé de données structurées, généralement stockées et accessibles électroniquement via un système de gestion de base de données (SGBD).

### 41. **SGBD (Système de Gestion de Base de Données)**
   Un logiciel permettant de créer, gérer et manipuler des bases de données. Exemples : MySQL, PostgreSQL, SQL Server, Oracle.

### 42. **Table**
   Structure de base dans une base de données relationnelle, organisée en lignes (enregistrements) et colonnes (champs).

### 43. **Tuple**
   Un enregistrement dans une table de base de données, correspondant à une ligne.

### 44. **Colonne (Attribut)**
   Champ d'une table, représentant une donnée particulière qui sera associée à chaque enregistrement.

### 45. **Index**
   Structure de données permettant d'accélérer la recherche de lignes dans une table de base de données. Un index est généralement créé sur une ou plusieurs colonnes.

### 46. **Query (Requête)**
   Instruction permettant de demander, insérer, mettre à jour ou supprimer des données dans une base de données.

### 47. **Normalisation**
   Processus consistant à organiser les données dans une base de données pour minimiser la redondance et améliorer l'intégrité des données. Les formes normales (1NF, 2NF, 3NF, etc.) sont des étapes de ce processus.

### 48. **Dénormalisation**
   Processus inverse de la normalisation, où des duplications de données sont introduites pour optimiser la vitesse de lecture, souvent utilisée dans les bases de données pour l'analyse.

### 49. **ACID (Atomicité, Cohérence, Isolation, Durabilité)**
   Ensemble de propriétés garantissant que les transactions de base de données sont traitées de manière fiable. 
   
   - **Atomicité** : Une transaction est tout ou rien.
   - **Cohérence** : La base de données reste dans un état cohérent avant et après la transaction.
   - **Isolation** : Les transactions sont exécutées de manière isolée les unes des autres.
   - **Durabilité** : Une fois qu'une transaction est validée, elle est permanente, même en cas de panne.

### 50. **Transaction**
   Une unité de travail dans une base de données qui est traitée de manière atomique et ACID, souvent pour garantir la cohérence des données.

### 51. **Locking (Verrouillage)**
   Mécanisme permettant de gérer l'accès concurrent aux données, garantissant que plusieurs transactions ne modifient pas les mêmes données en même temps.

### 52. **Partitionnement Horizontal**
   Technique consistant à diviser une table de base de données en plusieurs sous-ensembles de lignes pour optimiser les performances et la gestion des grandes quantités de données.

### 53. **Partitionnement Vertical**
   Technique consistant à diviser une table en sous-ensembles de colonnes pour optimiser les performances de lecture et réduire la taille des enregistrements individuels.

### 54. **ETL en Temps Réel (Streaming ETL)**
   Variante de l'ETL où les données sont extraites, transformées, et chargées en continu et en temps réel au lieu d'être traitées par lots. Cela permet de traiter des flux de données en continu.

### 55. **Kafka**
   Plateforme de traitement de flux distribuée open source développée par Apache, utilisée pour construire des pipelines de données en temps réel et des applications de streaming. Kafka utilise un modèle producteur-consommateur pour gérer le flux de données.

### 56. **Producteur (Producer)**
   Composant dans un système de messagerie comme Kafka qui génère ou envoie des messages (données) dans des **topics**. Un producteur est responsable de publier des événements ou des données.

### 57. **Consommateur (Consumer)**
   Composant qui lit ou consomme les messages des topics dans Kafka. Un consommateur est responsable de traiter ou d'analyser les événements ou données reçues.

### 58. **Topic**
   Sujet ou catégorie dans Kafka, où les messages sont organisés et publiés par les producteurs. Les consommateurs s'abonnent à ces topics pour recevoir les données.

### 59. **Partition dans Kafka**
   Kafka divise les topics en partitions pour permettre le parallélisme du traitement des données. Chaque partition est une séquence ordonnée de messages qui peuvent être répartis sur plusieurs nœuds pour permettre une mise à l'échelle horizontale.

### 60. **Broker**
   Serveur Kafka responsable du stockage des données et de la gestion des demandes des producteurs et des consommateurs.

### 61. **Cluster Kafka**
   Un groupe de serveurs Kafka (brokers) travaillant ensemble pour distribuer et équilibrer le stockage des données et le traitement des messages. Les clusters Kafka permettent la mise à l'échelle et la tolérance aux pannes.

### 62. **Consumer Group**
   Un ensemble de consommateurs qui travaillent ensemble pour traiter des messages depuis un topic Kafka. Chaque message est traité par un seul consommateur au sein du groupe, ce qui permet de répartir la charge.

### 63. **Offset**
   Position d'un message dans une partition Kafka. Chaque message est identifié par un offset, ce qui permet aux consommateurs de savoir où ils en sont dans la lecture des données.

### 64. **Connecteurs Kafka (Kafka Connect)**
   Framework permettant d'intégrer facilement Kafka avec des systèmes externes (bases de données, systèmes de fichiers, etc.) en configurant des connecteurs pour transférer les données.

### 65. **Stream Processing**
   Technique utilisée pour traiter, analyser et manipuler des données en temps réel. Kafka Streams, par exemple, est une API permettant de construire des applications de traitement de flux en temps réel.

### 66. **Micro-batching**
   Approche intermédiaire entre le traitement par lot et le traitement en temps réel, où les données sont regroupées en petits lots pour être traitées rapidement, souvent utilisé avec des systèmes comme Spark Streaming.

### 67. **Backpressure**
   Mécanisme dans un pipeline de streaming qui régule le flux de données lorsqu'un composant aval est surchargé et ne peut pas traiter les données aussi rapidement qu'elles arrivent.

### 68. **Pub/Sub (Publication-Subscription)**
   Modèle de messagerie dans lequel les producteurs publient des messages sans se soucier des consommateurs, et les consommateurs s'abonnent aux topics pour recevoir ces messages. Kafka utilise ce modèle.

### 69. **Durabilité des messages**
   Caractéristique des systèmes de messagerie comme Kafka qui garantit que les messages sont stockés de manière persistante et qu'ils peuvent être récupérés même en cas de défaillance système.

### 70. **Data Warehouse (Entrepôt de Données)**
   Un système de stockage centralisé conçu pour permettre l'analyse et la génération de rapports à partir de données provenant de sources multiples. Les données y sont organisées de manière structurée, optimisées pour les requêtes analytiques.

### 71. **Data Lake**
   Un dépôt de données massives (big data) où les données peuvent être stockées dans leur format brut ou transformé. Contrairement à un data warehouse, un data lake peut contenir des données structurées, semi-structurées (JSON, XML), ou non structurées (texte, images, vidéos).

### 72. **Data Lakehouse**
   Fusion des concepts de **data lake** et de **data warehouse**, offrant la flexibilité du stockage brut d'un data lake tout en appliquant certaines structures et capacités analytiques d'un data warehouse.

### 73. **OLTP (Online Transaction Processing)**
   Type de système conçu pour gérer des transactions courantes dans les bases de données opérationnelles. Il est utilisé pour capturer, stocker et traiter des transactions en temps réel.

### 74. **OLAP (Online Analytical Processing)**
   Type de système conçu pour l'analyse multidimensionnelle des données dans des data warehouses, facilitant les requêtes complexes, comme l'analyse de tendances, les tableaux croisés et la segmentation de données.

### 75. **Dimensions**
   Attributs utilisés dans les **systèmes OLAP** pour organiser les données. Elles représentent les différents aspects sous lesquels une organisation souhaite analyser ses données (ex. : temps, produits, régions).

### 76. **Faits (Facts)**
   Données mesurables ou numériques dans un entrepôt de données, stockées dans des **fact tables** et généralement associées à des dimensions. Exemples : ventes, revenus, quantités.

### 77. **Modèle Étoile (Star Schema)**
   Architecture simple d'un data warehouse où les **fact tables** (tables de faits) sont reliées à plusieurs **dimension tables** (tables de dimensions), formant un schéma en étoile.

### 78. **Modèle Flocon de Neige (Snowflake Schema)**
   Variante du modèle étoile où les tables de dimensions sont normalisées, c'est-à-dire que les attributs des dimensions sont subdivisés en sous-tables, formant ainsi un schéma plus complexe.

### 79. **Cubes OLAP (Cubes de Données)**
   Structures de données multidimensionnelles utilisées dans les systèmes OLAP pour représenter les données et permettre une analyse rapide. Chaque dimension du cube représente une perspective différente sous laquelle les données peuvent être interrogées.

### 80. **Ingestion de Données**
   Processus consistant à collecter et à importer des données provenant de sources externes ou internes dans un système de stockage (data warehouse ou data lake) pour traitement ou analyse.

### 81. **Data Governance (Gouvernance des Données)**
   Ensemble de règles, de processus et de normes qui régissent la gestion des données dans une organisation. La gouvernance des données veille à ce que les données soient accessibles, fiables, sécurisées et utilisées conformément aux politiques organisationnelles.

### 82. **Data Quality (Qualité des Données)**
   Mesure de la précision, de l'exhaustivité, de la fiabilité et de la pertinence des données. La qualité des données est cruciale pour s'assurer que les décisions basées sur les données sont valides.

### 83. **Data Steward**
   Personne ou équipe responsable de la gestion de la qualité des données et de leur gouvernance. Les data stewards veillent à ce que les données soient bien documentées, disponibles et de haute qualité.

### 84. **Data Catalog (Catalogue de Données)**
   Outil ou système qui permet de documenter et d'organiser les métadonnées des données disponibles dans une organisation. Il aide à découvrir, comprendre et gérer les ensembles de données.

### 85. **ETL (Extract, Transform, Load)**
   Processus par lequel les données sont extraites de différentes sources, transformées pour correspondre aux besoins du système cible, puis chargées dans un entrepôt de données ou un autre système de stockage. Ce processus est souvent utilisé dans les data warehouses.

### 86. **ELT (Extract, Load, Transform)**
   Variante de l'ETL où les données sont d'abord chargées dans un entrepôt de données avant d'être transformées. Cette méthode est couramment utilisée dans des systèmes massifs comme les data lakes.

### 87. **Data Mart**
   Sous-ensemble d'un data warehouse, contenant des données spécifiques à un département ou à un domaine particulier d'une organisation (ex. : ventes, marketing). Les data marts sont conçus pour répondre à des besoins analytiques précis.

### 88. **Lac de Données Brutes (Raw Data Lake)**
   Une partie d'un data lake où les données sont stockées dans leur format brut, tel qu'elles ont été ingérées, sans transformation. Ce type de stockage est utile pour conserver l'historique complet des données.

### 89. **Delta Lake**
   Technologie de stockage qui ajoute des fonctionnalités transactionnelles à un data lake, permettant la gestion des transactions ACID, des versions historiques et des métadonnées sur les fichiers dans un data lake. Delta Lake est couramment utilisé avec Spark.

### 90. **Data Tiering**
   Technique qui consiste à organiser et stocker les données en fonction de leur fréquence d'utilisation, de leur importance ou de leur sensibilité. Les données les plus critiques sont stockées sur des disques plus rapides (tiers élevé), tandis que les données moins importantes sont stockées sur des supports plus lents (tiers faible).

### 91. **Time-to-Live (TTL)**
   Durée de vie pendant laquelle les données sont considérées comme valides ou pertinentes dans un système. Après cette période, les données peuvent être supprimées ou archivées.

### 92. **Data Lake Governance**
   Ensemble de règles et de processus mis en place pour garantir l'organisation, la gestion, la sécurité, et la conformité des données dans un data lake.

### 93. **Data Wrangling**
   Processus de transformation et de nettoyage des données brutes pour les rendre prêtes à l'analyse. Cela inclut la déduplication, le formatage, et la gestion des valeurs manquantes.

### 94. **Data Mesh**
   Nouveau paradigme dans la gestion des données où l'architecture du data lake ou du data warehouse est distribuée entre des équipes décentralisées, chaque équipe gérant ses propres ensembles de données comme des "produits de données" au lieu d'une gestion centralisée.

### 95. **Federated Data Access**
   Méthode permettant d'interroger des données provenant de plusieurs bases de données ou systèmes sans les déplacer ni les consolider dans un seul entrepôt de données. Les données restent dans leurs systèmes d'origine, mais sont accessibles de manière unifiée.

### 96. **Scalabilité Horizontale**
   Capacité d'un système, comme un data warehouse ou un data lake, à gérer des volumes croissants de données en ajoutant de nouveaux nœuds de stockage ou de calcul sans modifier l'infrastructure principale.

### 97. **Scalabilité Verticale**
   Processus consistant à améliorer les performances d'un système en augmentant les ressources disponibles, comme ajouter de la mémoire ou de la puissance CPU à un serveur existant.

### 98. **Data Retention Policy**
   Politique qui définit combien de temps les données doivent être conservées dans un système de stockage avant d'être archivées ou supprimées, souvent pour répondre à des exigences réglementaires ou de gestion.

### 99. **Data Archiving**
   Processus de déplacement des données non utilisées vers un emplacement de stockage à long terme, généralement moins coûteux, tout en conservant leur accessibilité pour des besoins futurs ou des audits.

### 100. **Snapshot**
   Copie figée des données à un moment précis, souvent utilisée pour des sauvegardes ou des audits dans un data warehouse ou un système OLAP.
