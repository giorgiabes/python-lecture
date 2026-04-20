import requests


def get_artists(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            {
                "q": query,
                "limit": limit,
            },
        )
    except requests.HTTPError:
        return []

    content = response.json()
    return [artists["title"] for artists in content["data"]]
