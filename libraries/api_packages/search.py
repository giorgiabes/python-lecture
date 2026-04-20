from museum.artists import get_artists
from museum.artworks import get_artwork


def main():
    artists = input("Artist: ")
    artworks = get_artists(query=artists, limit=3)
    for artwork in artworks:
        print(f"[*] {artwork}")


main()
