import requests
from bs4 import BeautifulSoup
import duckdb

# Remplacer par l'URL de la liste
url = "https://www.bordeaux-tourisme.com/agenda"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire les informations
data = []
for item in soup.find_all('div', class_='ListSit-item'):  
    title = item.find('p', class_='Card-title').text
    date = item.find('p', class_='Card-label').text
    cardUrl = item.find('a')['href']
    responseCard = requests.get(cardUrl)
    soupCard = BeautifulSoup(responseCard.text, 'html.parser')
    
    for item in soupCard.find_all('main', id='Main-wrapper'):
      image_element = item.select_one('figure.Img.FullImg img') 
      if image_element and 'data-src' in image_element.attrs:  
          image = image_element['data-src']
          imageLink = (f'https://www.bordeaux-tourisme.com{image}')  
          data.append((title, date, imageLink))

print(data)

# A voir pour l'envoie des données si il faut pas plutot faire un append des trois 

# Connecter à DuckDB et stocker
with duckdb.connect('datalake.db') as con:
  con.execute("CREATE TABLE IF NOT EXISTS agenda (title VARCHAR, date VARCHAR, imageLink VARCHAR)")
  # Il faut faire un insert global Batch insert : voir pour faire un envoie en masse bulk / batch
  con.execute("INSERT INTO agenda VALUES (?, ?, ?)", data)

