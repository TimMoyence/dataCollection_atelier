import requests
from bs4 import BeautifulSoup
import duckdb

# Remplacer par l'URL de la liste
url = "https://www.bordeaux-tourisme.com/agenda"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire les informations
data = []
for item in soup.find_all('div', class_='item-class'):  # Ajustez selon la structure HTML
    title = item.find('h2').text
    date = item.find('span', class_='date-class').text
    data.append((title, date))

# Connecter à DuckDB et stocker
con = duckdb.connect('data/bordeaux_tourisme.db')
con.execute("CREATE TABLE IF NOT EXISTS agenda (title VARCHAR, date VARCHAR)")
con.execute("INSERT INTO agenda VALUES (?, ?)", data)

# Remplacer l'URL
# Conservez l'intégrité des données
