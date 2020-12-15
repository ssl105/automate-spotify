# Automate-Spotify
A simple script that allows a user to search and add a song to multiple public playlists utilizing Spotify Web api.
This functionality is not present in the desktop client and mobile application for Spotify. 

## Running the Program
### Getting User Id
- Sign in to your account on https://open.spotify.com/. 
- Go to your profile page by accessing the drop down button on the upper right of the page.
- URL should be formatted open.spotify.com/user/"userID"

### Getting Token
- Access the Spotify Web API webpage https://developer.spotify.com/console/post-playlist-tracks/.
- Find Oauth Token and generate token with the required scopes along with play-read-private and playlist-read-collaborative scopes.
- Make sure you have signup for a spotify developer account

### Run the file
- Input the information into the user info file.
- Run the file using python main.py
- The command prompt will ask for the name of the artist and song.
- After inputing the song information, the prompt will ask for the name of your playlists to add to. 
- Press enter twice to stop input. 
- If playlist names were correctly inputted, the playlist should be modified with the corresponding song.

## Troubleshooting
* Spotify Oauth token expires within an hour. If you come across a `KeyError` this could
be caused by an expired token, in which case you would have to generate a new token.
