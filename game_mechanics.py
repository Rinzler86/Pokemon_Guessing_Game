import requests
import urllib.request
import base64
from PIL import Image as Imag
from PIL import  ImageTk
from tkinter import *
import io
import numpy as np


#API call
import numberz
import secrets


def pokemon_call(name_or_num):
    return requests.get(url=f'https://pokeapi.co/api/v2/pokemon/{name_or_num}/').json()

# class for displaying url photos
class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        self.image = PhotoImage(data=base64.encodebytes(raw_data))
        image = Imag.open(io.BytesIO(raw_data))
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image

def display_image(link):
    img = WebImage(link).get()
    imagelab = Label(image=img, bg='yellow', borderwidth=5 )
    imagelab.image = img
    imagelab.place(x=205, y=100)


def check_selector(var_1, var_2, var_3):
    if (var_1.get() == 1) & (var_2.get() == 1) & (var_3.get() == 1):
        rand_range_151 = secrets.SystemRandom().randrange(0, 386)
        return numberz.all[rand_range_151]
    elif (var_1.get() == 1) & (var_2.get() == 1) & (var_3.get() == 0):
        rand_range_151 = secrets.SystemRandom().randrange(0, 252)
        return numberz.all[rand_range_151]
    elif (var_2.get() == 1) & (var_3.get() == 1) & (var_1.get() == 0):
        rand_range_151 = secrets.SystemRandom().randrange(152, 386)
        return numberz.all[rand_range_151]
    elif (var_1.get() == 1) & (var_3.get() == 1) & (var_2.get() == 0) :
        print("i dont know how to combine these 2 yet!")
    elif (var_1.get() == 1):
        rand_range_151 = secrets.SystemRandom().randrange(0, 152)
        return numberz.all[rand_range_151]
    elif (var_2.get() == 1):
        rand_range_151 = secrets.SystemRandom().randrange(152, 252)
        return numberz.all[rand_range_151]
    elif (var_3.get() == 1):
        rand_range_151 = secrets.SystemRandom().randrange(252, 386)
        return numberz.all[rand_range_151]
