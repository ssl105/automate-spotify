# Automate-Spotify
A simple script that allows a user to add one song to multiple public playlists utilizing Spotify Web api.
This functionality is not present in the desktop client and mobile apps. 

## Troubleshooting
* Spotify Oauth token expires within an hour. If you come across a `KeyError` this could
be caused by an expired token, in which case you would have to generate a new token.
