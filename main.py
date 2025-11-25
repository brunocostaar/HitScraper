from bs4 import BeautifulSoup # biblioteca de webscraping
import requests # biblioteca para fazer requisições HTTP
import spotipy # biblioteca para acessar a API do Spotify
from spotipy.oauth2 import SpotifyOAuth
import os
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_agent = os.getenv("USER_AGENT")

scope = "playlist-modify-public" # escopo do que spotipy pode fazer

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri="http://127.0.0.1:8888/callback",
    scope=scope
))

url = "https://www.billboard.com/charts/hot-100/" # url do site usado para pegar as músicas mais ouvidas no determinado dia
headers = {
    "User-Agent": user_agent # header necessário para acessar a página
}

date = input("Input a date (YYYY-MM-DD): ") # pega a data desejada
url = url + date # adiciona ao url

response = requests.get(url=url, headers=headers) # pega a pagina
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser') # faz o webscraping

song_items = soup.select("li.o-chart-results-list__item") # pega cada item da lista de 100 músicas

song_names = []
for item in song_items:
    # o seletor h3 dentro do item é o nome da música
    title_element = item.select_one("h3")
    # o seletor span logo após o h3 geralmente é o artista
    artist_element = item.select_one("h3 + span")

    if title_element and artist_element:
        title = title_element.get_text().strip()
        artist = artist_element.get_text().strip()
        song_names.append(f"{title} {artist}")

user_id = sp.current_user()["id"] # pega seu user ID do spotify

track_uris = []

for song_name in song_names:
    # busca pela música (limite de 1 resultado para pegar o top hit)
    result = sp.search(q=song_name, limit=1, type='track')

    tracks = result['tracks']['items']

    if tracks:
        # pega o URI da primeira música encontrada
        uri = tracks[0]['uri']
        track_name = tracks[0]['name']
        artist_name = tracks[0]['artists'][0]['name']

        track_uris.append(uri)
        print(f"✅ Encontrada: {track_name} - {artist_name}")
    else:
        print(f"❌ Não encontrada: {song_name}")

if track_uris:
    playlist_name = f"Músicas mais populares no dia {date}"

    # cria a playlist vazia
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)

    # adiciona as músicas encontradas
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

    print(f"\n✅ Playlist '{playlist_name}' criada com sucesso com {len(track_uris)} músicas!")
else:
    print("\nNenhuma música válida foi encontrada para criar a playlist.")