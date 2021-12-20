from tkinter import *
import pandas
from random import choice
color1 = "#B1DDC6"
palabra_actual={}
palabras={}

try:
    datos=pandas.read_csv("day 31 flash card/data/aprender.csv")
except FileNotFoundError:
    original=pandas.read_csv("day 31 flash card/data/palabras.csv")
    palabras=original.to_dict(orient="records")
else:
    palabras=datos.to_dict(orient="records")



def siguiente_tarjeta():
    global palabra_actual,espera
    ventana.after_cancel(espera)
    palabra_actual=choice(palabras)
    canva.itemconfig(idioma,text="English",fill="black")
    canva.itemconfig(palabraIdioma,text=palabra_actual["English"],fill="black")
    canva.itemconfig(fondo_tarjeta,image=imagen_inicio)
    espera=ventana.after("3000",func=cambia_tarjeta)

def cambia_tarjeta():
    canva.itemconfig(idioma,text="Spanish",fill="white")
    canva.itemconfig(palabraIdioma,text=palabra_actual["Spanish"],fill="white")
    canva.itemconfig(fondo_tarjeta,image=imagen_atras)

def lo_se():
    palabras.remove(palabra_actual)
    datos=pandas.DataFrame(palabras)
    datos.to_csv("day 31 flash card/data/aprender.csv",index=False)
    siguiente_tarjeta()


ventana=Tk()
ventana.title("Aprende ingles")
ventana.config(padx=20,pady=20,bg=color1)
ventana.resizable(0,0)

espera=ventana.after("3000",func=cambia_tarjeta)

canva=Canvas(width=800,height=526,highlightthickness=0,bg=color1)
imagen_inicio=PhotoImage(file="day 31 flash card/images/card_front.png")
imagen_atras=PhotoImage(file="day 31 flash card/images/card_back.png")
fondo_tarjeta=canva.create_image(400,263,image=imagen_inicio)
idioma=canva.create_text(400,160,font=("Arial",36,"italic"))
palabraIdioma=canva.create_text(400,250,font=("Arial",50,"bold"))
canva.grid(row=0,column=0,columnspan=2)

noImg=PhotoImage(file="day 31 flash card/images/wrong.png")
noBtn=Button(image=noImg,highlightthickness=0,command=siguiente_tarjeta)
noBtn.grid(column=0,row=1)

siIma=PhotoImage(file="day 31 flash card/images/right.png")
siBtn=Button(image=siIma,highlightthickness=0,command=lo_se)
siBtn.grid(column=1,row=1)

siguiente_tarjeta()

ventana.mainloop()