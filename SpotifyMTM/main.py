import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from secret import CLIENT_ID,CLIENT_SECRET



# date = input("Which uear do you want to travel to? Type the date in this format YYYY-MM-DD: ").upper()
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
# soup = BeautifulSoup(markup=response.text)


# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri="http://example.com"))

# results = sp.current_user_saved_tracks()
# for index, item in enumerate(results['items']):
#     track = item['track']
#     print(index, track['artists'][0]['name'], " - ", track['name'])
    
    
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri="http://example.com"))

sp.user_playlist_create(user="qljdlbk9slxdci2wcp6t8qths", name="Test", public=False)


