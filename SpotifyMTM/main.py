from bs4 import BeautifulSoup
import requests
from spotifyAccess import createSpoitfySongsURI, addSongsToPlaylist




# date = input("Which uear do you want to travel to? Type the date in this format YYYY-MM-DD: ").upper()
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
# soup = BeautifulSoup(markup=response.text)


def createSongList(date) -> list: 
    response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
    soup = BeautifulSoup(response.text,'html.parser')
    allSongTitles = soup.select(selector="li h3")
    top100 = [allSongTitles[i].getText().strip() for i in range(100)]    
    return top100
        
year = "2010-01-20"

songs = createSongList(year)

uris = createSpoitfySongsURI(songs)

addSongsToPlaylist(uris)



    
    


