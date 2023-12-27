def make_album(artist_name, album_title, number_of_songs=None):
    artist = {'name': artist_name.title(), 'album': album_title.title(), 'number_of_songs': number_of_songs}
    return artist


while True:
    album_title = input(f"Album title: ")
    if album_title == 'q':
        break

    artist_name = input(f"Artist name: ")
    if artist_name == 'q':
        break

    number_of_songs = input(f"Number of songs: ")
    if number_of_songs == 'q':
        break
    album_details = make_album(artist_name=artist_name, album_title=album_title, number_of_songs=number_of_songs)
    print(album_details)
