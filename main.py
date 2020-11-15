from add_to_playlists import AddToPlaylists

def run():
    artist = input("Enter name of the artist: ")
    song_name = input("Enter name of the song: ")
    playlists = []


    while 1:
        curr_input = input("Enter name of the playlist: ")

        if curr_input == "":
            break

        playlists.append(curr_input)
        
    ap = AddToPlaylists()
    ap.add_song_to_playlists(playlists, artist, song_name)
    
if __name__ == "__main__":
    run()