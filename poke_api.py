import requests

from contants import GET_POKEMON_URL
from utils import create_img_path_for_pokemon


def get_all_pokemons():
    """
    Gets all pokemon names.

    Return:
        list[str]: list of pokemon names
    """
    response = requests.get(GET_POKEMON_URL)
    if response.status_code != 200:
        print("failure")
        print(f"Response code: {response.status_code} ({response.reason})")
        return []

    json_response = response.json()
    all_pokemons_info = json_response["results"]
    all_pokemon_names = [pokemon_info["name"] for pokemon_info in all_pokemons_info]
    return all_pokemon_names


def get_pokemon(pokemon):
    """
    Gets the pokemon

    Args:
        pokemon (str): name of pokemon
    
    Returns:
        pokemon_info (dict): a dictionary of pokemon info
    """
    response = requests.get(GET_POKEMON_URL + pokemon)
    if response.status_code != 200:
        raise Exception("Pokemon not found.")
    
    pokemon_info = response.json()
    return pokemon_info


def download_pokemon_image(pokemon):
    """
    Downloads the given pokemon image.

    Args:
        pokemon (str): name of pokemon

    Returns:
        img_path (str): path where image is stored
    """
    try:
        pokemon_info = get_pokemon(pokemon)
    except Exception:
        return ""

    try:
        img_url = pokemon_info["sprites"]["other"]["official-artwork"]["front_default"]
    except KeyError:
        return ""

    # get image extension
    ext = img_url.split(".")[-1]

    # get actual image
    response = requests.get(img_url)
    if response.status_code != 200:
        return

    file_path = create_img_path_for_pokemon(pokemon, ext)

    # save image in disk
    with open(file_path, "wb") as file:
        file.write(response.content)

    return file_path
