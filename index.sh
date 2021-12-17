#!/bin/bash

## Intalación del emulador ##
##################################

sudo mkdir /etc/FinalGame
sudo apt-get install mednafen -y
sudo cp -r ./roms/ /etc/FinalGame

##################################

## Arranque personalizado ##
##################################################################
sudo cp ./Audio.mp3 /etc/FinalGame/Audio.mp3
sudo apt install sox -y
sudo apt install libsox-fmt-mp3 -y
sudo cp ./grub /etc/default/grub
sudo update-grub
sudo cp ./splash.png /usr/share/plymouth/themes/pix/splash.png
sudo cp ./Fondo.png /etc/FinalGame/Fondo.png
pcmanfm --set-wallpaper /etc/FinalGame/Fondo.png
sudo xrandr -s 1152x864
##################################################################

## Configuración de la consola para el arranque automatico ##
##################################################################

sudo cp ./Background.png /etc/FinalGame/Background.png
sudo cp ./consola.py /etc/FinalGame
sudo cp ./display.desktop /etc/xdg/autostart/display.desktop

##################################################################

## Reinicio de la maquina ##########

sudo reboot

########