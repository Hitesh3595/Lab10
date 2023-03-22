import os
import ctypes

from contants import IMG_DIR


def create_img_path_for_pokemon(pokemon, ext):
    """
    Generates path of where pokemon image is present or will be downloaded.
    """
    file_name = f"{pokemon}.{ext}"
    file_path = os.path.join(IMG_DIR, file_name)
    return file_path


def change_desktop_img(path):
    """
    Set image present at given path as desktop image.

    Args:
        path (str): path of image
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
    return