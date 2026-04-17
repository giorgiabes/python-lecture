import sys
import requests


def main():
    print("Search the Art Institute of Chicago!")
    artinst = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artinst, "limit": 3},
        )
        response.raise_for_status()
    except requests.ConnectionError:
        print("Couldn't complete request!")
        sys.exit(-20)

    content = response.json()
    for artwork in content["data"]:
        print(f"[*] {artwork["title"]}")


main()
