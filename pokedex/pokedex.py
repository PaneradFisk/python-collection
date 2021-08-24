# Building a Pokédex using Pokemon API.
# GET https://pokeapi.co/api/v2/pokemon/{id or name}/
# GET https://pokeapi.co/api/v2/generation/{id or name}/


import json
import requests


def check_internet_connection():
    inet_url = "https://www.google.com/"
    inet_timeout = 10
    try:
        check_connect = requests.get(url=inet_url, timeout=inet_timeout)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection, this program needs internet connection to work.")
        exit()


# Verify internet connection required to do API calls.
check_internet_connection()


pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
gen_url = "https://pokeapi.co/api/v2/generation/"

pokemon_input = input("Pokémon name or #: ")
gen_input = input("Select generation #: ")

url = gen_url + gen_input
#url = pokemon_url + pokemon_input

r = requests.get(url)
r.raise_for_status

pkdata = json.loads(r.text)


# Functions to extract data from JSON


def get_index():
    pokemon_index = pkdata["id"]
    print("#" + str(pokemon_index))


def get_name():
    pokemon_name = str(pkdata["name"]).capitalize()
    print(pokemon_name)


def get_type():
    pokemon_type_data = pkdata["types"]
    pokemon_type = []
    for i in range(0, len(pokemon_type_data)):
        pokemon_type.append(pokemon_type_data[i]["type"]["name"])
    for i in pokemon_type:
        print("|Type: " + str(i).capitalize(), end=" |")


def get_base_stat():
    print("Basestats:")
    pokemon_stats_data = pkdata["stats"]
    stats_numbers = []
    stats_names = []
    for i in range(0, len(pokemon_stats_data)):
        stats_numbers.append(pokemon_stats_data[i]["base_stat"])
        stats_names.append(pokemon_stats_data[i]["stat"]["name"])
        print(str(pokemon_stats_data[i]["stat"]["name"]).capitalize(
        )+":", pokemon_stats_data[i]["base_stat"])


# Running everything
print("*" * 30)
get_index()
get_name()
get_type()
print()
get_base_stat()
print("*" * 30)
