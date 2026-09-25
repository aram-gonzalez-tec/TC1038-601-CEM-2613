import requests

url_base = "https://pokeapi.co/api/v2/pokemon"
nombre = input("Introduce el nombre del pokémon que buscas: ").strip().lower()

response = requests.get(f"{url_base}/{nombre}").json()

match response:
    case {"height": height, "weight": weight}:
        print(f"{nombre} - altura: {height} - peso: {weight}")
    case _:
        print("Error")