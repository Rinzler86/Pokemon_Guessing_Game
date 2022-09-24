import os
import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import numberz
from game_mechanics import WebImage, pokemon_call, display_image, check_selector
import pygame

#Create window and attributes for sizing and title name
root = tk.Tk()
root.geometry('500x500+400+200')
root.resizable(False, False)
root.title("Pokemon Guessing Game!")
root.config(bg='white')
ico = Image.open("C:\\Users\\Zeb Duffey\\Downloads\\pikachu_face.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

pygame.mixer.init()

def play_sound():
   pygame.mixer.music.load("C:\\Users\\Zeb Duffey\\Downloads\\right-answer-ding-ding-sound-effect\\Right-answer-ding-ding-sound-effect.mp3")
   pygame.mixer.music.play()


def play_wrong():
   pygame.mixer.music.load("C:\\Users\\Zeb Duffey\\Downloads\\mixkit-basketball-buzzer-1647.wav")
   pygame.mixer.music.play()

#function for deleting textbox hint when mouse button is clicked
def click(event):
   textbox.configure(state=NORMAL)
   textbox.delete(0, END)
   textbox.unbind('<Button-1>', clicked)

#creating and placing pokemon logo
pokemon_logo = Image.open("C:\\Users\\Zeb Duffey\\Downloads\\pokemon-logo-png-0.png")
resize_tuple = (140, 100)
resize_logo = pokemon_logo.resize(resize_tuple)
test = ImageTk.PhotoImage(resize_logo)

label1 = tkinter.Label(image=test, bg='white')
label1.image = test

# Position for pokemon logo
label1.place(x=180, y=0)

#creation and placement of grass graphic in bottom of application
pokemon_grass = Image.open("C:\\Users\\Zeb Duffey\\Downloads\\long_grass.jpg")
resize_tuple_2 = (500, 200)
resize_logo_2 = pokemon_grass.resize(resize_tuple_2)
test2 = ImageTk.PhotoImage(resize_logo_2)

label2 = tkinter.Label(image=test2, bg='white')
label2.image = test2

# Position for grass graphic
label2.place(x=0, y=340)

#creating and placing pokemon background
pokemon_logo_3 = Image.open("C:\\Users\\Zeb Duffey\\Downloads\\pokemon-backgrouund_cropped.jpg")
resize_tuple_3 = (270, 200)
resize_logo_3 = pokemon_logo_3.resize(resize_tuple_3)
test_3 = ImageTk.PhotoImage(resize_logo_3)

label3 = tkinter.Label(image=test_3, bg='white')
label3.image = test_3

# Position for pokemon logo
label3.place(x=230, y=250)


current_pokemon = ''
current_name = []
numberss = numberz.all


def start_press():
   global current_pokemon
   global indexP
   pokemon = check_selector(var_1=var_1, var_2=var_2, var_3=var_3)
   current_pokemon = pokemon
   name = pokemon_call(name_or_num=pokemon)['name']
   current_name.append(name)
   #weight = pokemon_call(name_or_num=retrieve_name)['weight']
   pokemon_sprite = pokemon_call(name_or_num=pokemon)['sprites']['front_default']
   put_in_quatations = f'{pokemon_sprite}'
   display_image(link=put_in_quatations)
   start_button["state"] = DISABLED
   checkbox_1["state"] = DISABLED
   checkbox_2["state"] = DISABLED
   checkbox_3["state"] = DISABLED


textbox = Entry(width=20, font=('Segoe Print', 14), justify='center', fg='#2a75bb')
textbox.place(x=110, y=390)

score = 0


def get_pokemon(*args):
   global score
   global numberss
   global current_pokemon
   entered = textbox.get().lower()
   if entered == current_name[0]:
      play_sound()
      current_name.pop()
      numberss.remove(current_pokemon)
      current_pokemon = ''
      #numberss.pop(current_pokemon)
      score += 1
      score_label.config(text=f'Score: {score}')
      textbox.delete(0, END)
      start_press()
      print(current_name)
   else:
      play_wrong()
      current_name.pop()
      start_press()
      textbox.delete(0, END)
      print(current_name)


# Restarts the Whole Window
# def restart():
#    global root
#    root.destroy()
#    root = Tk()
#    root.mainloop()


enter_button = Button(text="Enter", font=('Segoe Print', 15), command=get_pokemon)
enter_button.place(x=210, y=430)

start_button = Button(text="Start", font=('Segoe Print', 15), command=start_press)
start_button.place(x=380, y=190)

#restart_button = Button(text="Reset", font=('Segoe Print', 15), command=restart)
#restart_button.place(x=80, y=190)

score_label = Label(text=f'Score: {score}', font=('Segoe Print', 15), bg='white')
score_label.place(x=360, y=20)

var_1 = tk.IntVar()
var_2 = tk.IntVar()
var_3 = tk.IntVar()

checkbox_1 = tk.Checkbutton(root, text='Generation 1',variable=var_1, onvalue=1, offvalue=0, bg='white',font=('Segoe Print', 11) )
checkbox_1.place(x=350, y=100)

checkbox_2 = tk.Checkbutton(root, text='Generation 2',variable=var_2, onvalue=1, offvalue=0, bg='white',font=('Segoe Print', 11) )
checkbox_2.place(x=350, y=130)

checkbox_3 = tk.Checkbutton(root, text='Generation 3',variable=var_3, onvalue=1, offvalue=0, bg='white',font=('Segoe Print', 11) )
checkbox_3.place(x=350, y=160)

#bind return to button_press as alternative to pushing enter button
root.bind('<Return>', get_pokemon)

root.mainloop()