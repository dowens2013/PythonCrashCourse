
def make_album(artist_name, album_title, number_of_songs=None):
    artist = {'name': artist_name.title(), 'album': album_title.title(), 'number_of_songs': number_of_songs}
    return artist


album_details = make_album('lil wayne', 'right above it', 3)
print(album_details)