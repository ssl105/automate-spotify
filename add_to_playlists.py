import requests
import json

from user_info import user_id, token_code

class AddToPlaylists:

    def __init__(self, user = user_id, token = token_code):
        self.spotify_user_id = user
        self.spotify_token = token

    # function to search and return song from spotify web api
    # artist - artist of the song
    # song_name - name of the song
    # 
    # songs[0]["id"] - the first song found from the search 
    def get_song(self, artist, song_name):

        # search query using spotify web api
        query = "https://api.spotify.com/v1/search?q={}+{}&type=track&offset=0&limit=20".format(
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
        song = response_json["tracks"]["items"]

        # return the song on the top of list if it exists
        if song:
            return song[0]["uri"]
        else:
            message = "No song found for {} by {}".format(song_name, artist)
            raise Exception(message)


    # function to search and return a user's playlist
    # playlist - name of the playlist
    # 
    # response[i]["id"] - the playlist with the corresponding name
    def get_playlist(self, playlist_name):
        # search query
        query = "https://api.spotify.com/v1/users/{}/playlists".format(self.spotify_user_id)

        # send http request
        response = requests.get(
            query,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )
        

        # search for the playlist with the correct name
        response_json = response.json()
        playlists = response_json["items"]
        for i in range(len(response_json)):
            if playlists[i]["name"] == playlist_name:
                return playlists[i]["id"]
            
        # no playlist found
        return None


    def add_song_to_playlist(self, playlist_id, song_id):
        songs = [song_id]
        request_data = json.dumps(songs)
        
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            playlist_id)

        response = requests.post(
            query,
            data = request_data,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.spotify_token)
            }
        )

        # check for valid response status
        if response.status_code != 201:
            print("Could not add to playlist")

        response_json = response.json()
        return response_json
        


    def add_song_to_playlists(self, string_list, artist, song_name):
        song_id = self.get_song(artist, song_name) # song id

        # get id list for playlist
        id_list = []
        for i in range(len(string_list)):
            id_list.append(self.get_playlist(string_list[i]))

        # add song to playlists
        for i in range(len(id_list)):
            if id_list is None:
                continue

            self.add_song_to_playlist(id_list[i], song_id)

