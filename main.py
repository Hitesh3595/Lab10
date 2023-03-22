from tkinter import *
from tkinter import ttk
import os


from poke_api import get_all_pokemons, download_pokemon_image
from contants import (
    APP_NAME,
    BUTTON_PAD_X,
    BUTTON_PAD_Y,
    BUTTON_ENABLE,
    BUTTON_DISABLE,
    DROPDOWN_PAD_X,
    DROPDOWN_PAD_Y,
    IMG_DIR,
    IMG_PAD_X,
    IMG_PAD_Y,
    DEFAULT_IMG,
)
from utils import  change_desktop_img, create_img_path_for_pokemon


default_img_path = os.path.join(IMG_DIR, DEFAULT_IMG)


def get_selected_pokemon():
    """
    Returns pokemon selected by user.
    """
    pokemon_index = cbox_pokemon_sel.current()
    pokemon_name = pokemon_list[pokemon_index]
    return pokemon_name


def show_pokemon_image(event):
    """
    Show image of selected pokemon on UI and enables "Set as desktop image" button.
    """
    pokemon_name = get_selected_pokemon()
    btn_set_img["state"] = BUTTON_ENABLE
    path = download_pokemon_image(pokemon=pokemon_name)
    img_logo["file"] = path
    return


def set_as_desktop_image():
    """
    Set pokemon image as desktop wallpaper.
    """
    print("setting desktop image...")
    path=img_logo["file"]
    #pokemon = get_selected_pokemon()
    #path = create_img_path_for_pokemon(pokemon)
    change_desktop_img(path)
    return


root = Tk()
root.title(APP_NAME)


# show default image
img_logo = PhotoImage(file=default_img_path)
lbl_logo = ttk.Label(root, image=img_logo)
lbl_logo.grid(padx=IMG_PAD_X, pady=IMG_PAD_Y)


# add dropdown of pokemon
pokemon_list = get_all_pokemons()
cbox_pokemon_sel = ttk.Combobox(root, values=pokemon_list, state='readonly')
cbox_pokemon_sel.set("Select a Pokemon")
cbox_pokemon_sel.bind("<<ComboboxSelected>>", show_pokemon_image)
cbox_pokemon_sel.grid(padx=DROPDOWN_PAD_X, pady=DROPDOWN_PAD_Y)


# "Set as Desktop Image" button
btn_set_img = ttk.Button(
    root,
    text="Set as Desktop Image",
    command=set_as_desktop_image,
    state=BUTTON_DISABLE,
)
btn_set_img.grid(padx=BUTTON_PAD_X, pady=BUTTON_PAD_Y)


root.mainloop()


