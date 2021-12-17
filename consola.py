#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ###########################################################################
# consola.py
#
# Author: Alejandro Alpizar Lizbeth Viridiana
# Author: Mendoza Rodriguez Luis Alberto
# Author: Montoya Pérez Héctor
#
# Lincence: MIT
#
# Este progra es la interfas grafica de la consola asi como el contralador
# de muchos procesos de la consola.
#
# ###########################################################################

from tkinter import *
from tkinter import ttk
import os
import threading

# función para ejecutar el emulador con el juego seleccionado

def games(juego):
    os.system("mednafen /etc/FinalGame/roms/" + juego)

# función para reproducir sonido
def sonido():
    os.system("play /etc/FinalGame/Audio.mp3")

threading.Thread(target=sonido).start()

os.system("xrandr -s 1152x864")

# función para salir
def salir():
    os.system("sudo shutdown now")

# Creación de la interfaz
###############################################
raiz = Tk()
raiz.title("Consola")
raiz.attributes("-fullscreen",True)
raiz.resizable(1,1)
raiz.config(bg="White")
###############################################

imagen = PhotoImage(file="/etc/FinalGame/Background.png")
Label(raiz, image=imagen, bd=0).pack()

# Boton de ejecución del juego
########################################################################

Button(raiz,text="Batman"           ,bg='gold',command=lambda:games("Batman.gbc")                                       ,width=15).place(x=600,y=50,anchor="center")
Button(raiz,text="Bubble Bobble"    ,bg='gold',command=lambda:games("BubbleBobble.gbc")                                 ,width=15).place(x=600,y=100,anchor="center")
Button(raiz,text="Tarzan"           ,bg='gold',command=lambda:games("Disney_Tarzan.gbc")                                ,width=15).place(x=600,y=150,anchor="center")
Button(raiz,text="Galaga"           ,bg='gold',command=lambda:games("Galaga.gbc")                                       ,width=15).place(x=600,y=200,anchor="center")
Button(raiz,text="Kirby"            ,bg='gold',command=lambda:games("KoroKoroKirby.gbc")                                ,width=15).place(x=600,y=250,anchor="center")
Button(raiz,text="Mega Man"         ,bg='gold',command=lambda:games("MegaManXtreme.gbc")                                ,width=15).place(x=600,y=300,anchor="center")
Button(raiz,text="Monopoly"         ,bg='gold',command=lambda:games("Monopoly.gbc")                                     ,width=15).place(x=600,y=350,anchor="center")
Button(raiz,text="Pokemon Red"      ,bg='gold',command=lambda:games("PokemonRed.gb")                                    ,width=15).place(x=600,y=400,anchor="center")
Button(raiz,text="Pokemon Yellow"   ,bg='gold',command=lambda:games("PokemonYellowVersion.gbc")                         ,width=15).place(x=600,y=450,anchor="center")
Button(raiz,text="Resident Evil"    ,bg='gold',command=lambda:games("ResidentEvilGaiden.gbc")                           ,width=15).place(x=600,y=500,anchor="center")
Button(raiz,text="Shantae"          ,bg='gold',command=lambda:games("Shantae.gbc")                                      ,width=15).place(x=600,y=550,anchor="center")
Button(raiz,text="Simpsons"         ,bg='gold',command=lambda:games("SimpsonsThe-NightoftheLivingTreehouseofHorror.gbc"),width=15).place(x=600,y=600,anchor="center")
Button(raiz,text="Super Mario World",bg='gold',command=lambda:games("Super_Mario_World.smc")                            ,width=15).place(x=600,y=650,anchor="center")
Button(raiz,text="Tetris"           ,bg='gold',command=lambda:games("Tetris.gb")                                        ,width=15).place(x=600,y=700,anchor="center")
Button(raiz,text="Tomb Raider"      ,bg='gold',command=lambda:games("TombRaiderCurseoftheSword.gbc")                    ,width=15).place(x=600,y=750,anchor="center")

# Boton Apagar consolaa
########################################################################
Button(raiz,text="Apagar",bg='red',command=salir,width=15).place(x=600,y=800,anchor="center")
########################################################################

# Ejecución de la interfas grafica
###################################
raiz.mainloop()
###################################