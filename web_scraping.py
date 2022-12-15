import requests
import pandas as pd
from bs4 import BeautifulSoup

url=requests.get('https://www.imdb.com/chart/top')
url.raise_for_status()
soup = BeautifulSoup(url.text,'html.parser')
movies = soup.find('tbody',class_="lister-list").find_all('tr')
xyz = []
for abc in movies:
    name=abc.find('td',class_="titleColumn").a.text
    rank= abc.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
    year=abc.find('td',class_="titleColumn").span.text.strip('()')
    rating = abc.find('td',class_="ratingColumn imdbRating").strong.text
    
    xyz.append([rank,name,year,rating])

df = pd.DataFrame(xyz, columns=['Rank','Name','Year','Rating'],ignore_Index=True)
df.to_csv('Top_rated_movies')

    
