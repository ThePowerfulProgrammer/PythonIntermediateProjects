import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

movieTitles = soup.find_all(name="h3", class_="title")
 

for i in movieTitles[::-1]:
    
    
    with open("./MovieSoup/movies.txt", mode="a", encoding="utf-8") as wFile:
        wFile.write(f"{i.getText()}\n")       
        
    
