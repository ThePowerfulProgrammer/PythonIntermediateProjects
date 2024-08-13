from bs4 import BeautifulSoup
import requests




# date = input("Which uear do you want to travel to? Type the date in this format YYYY-MM-DD: ").upper()
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
# soup = BeautifulSoup(markup=response.text)


def createSongList(date) -> list: 
    
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
    soup = BeautifulSoup(response.text,'html.parser')
    
    allSongTitles = soup.find_all(name="li ul h3", id="title-of-a-story")
    for title in allSongTitles:
        print(title.getText())
    
    return []
    

    
year = "2010-01-20"
print(createSongList(year))
    
    


