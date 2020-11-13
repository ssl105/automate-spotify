import requests

class AddToPlaylists:

    def __init__(self, user, token):
        self.spotify_user_id = user
        self.spotify_token = token

    # function to search and return song from spotify web api
    # artist - artist of the song
    # song_name - name of the song
    # 
    # songs[0]["id"] - the first song found from the search 
    def get_song(self, artist, song_name):

        # search query using spotify web api
        query = "https://api.spotify.com/v1/search?q=track:{}+artist:{}&type=track&offset=0&limit=20".format(
            song_name,
            artist
        )

        # send http request to spotify web api
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )

        # get the list of songs returned
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # return the song on the top of list if it exists
        if songs:
            return songs[0]["id"]
        else:
            raise Exception("No song found for {} by {}".format(song_name, artist))

    def get_playlist(self, playlist_name):
        pass

    def add_song_to_playlists(self):
        pass

