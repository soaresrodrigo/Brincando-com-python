#!/usr/bin/python
##
#  Esse script serve para configurar o tema de exibição, do shell e do desktop. A lógica é alterar dinamicante entre claro se tiver de manhã e escuro se tiver de noite, assim descansa a visão.
import os
import datetime
import time
import sys

# Transforma a prioridade em muito baixa
os.nice(20)

# Configura a hora a ser executada
def configTime():
    hora_atual   = datetime.datetime.now().hour
    if hora_atual >= 6 and hora_atual < 17:
        return True
    return False

# Retorna a mensagem como notificação
def exeChange():
    if configTime() is True:
        theme       = "'Mojave-light'"
        shell       = 'Mojave-light'
        icon        = "'Mojave-CT-light'"
    else:
        theme       = "'Mojave-dark'"
        shell       = 'Mojave-dark'
        icon        = "'Mojave-CT-Night-Mode'"

    theme_actual = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
    
    if theme_actual != theme + "\n":
        setTheme(theme, shell, icon) 
        
    #Loop controlado para verificar a cada hora
    verifyTheme()
    
# Calcula os minutos que faltam pra completar alguma hora, depois manda o programa começar a validação
def verifyTheme():
    # Primeiro calcula os minutos restante e transforma em segundos, depois diminue com os segundos passados
    second_left = ((60 - datetime.datetime.now().minute)*60) - (60 - datetime.datetime.now().second)
    time.sleep(second_left)

    return exeChange()

# Aqui é a alteração dos temas
def setTheme(theme, shell, icon):
    os.system('gsettings set org.gnome.desktop.interface gtk-theme "{0}"'.format(theme)) #Tema
    os.system('gsettings set org.gnome.shell.extensions.user-theme name "{0}"'.format(shell)) #Shell
    os.system('gsettings set org.gnome.desktop.interface icon-theme "{0}"'.format(icon)) #icon
    os.system('notify-send -i /home/rodrigo/Imagens/Ícones/tema.png "Oi, Rodrigo" "Mudei o tema pra você"') #Mensagem da notificação
    
exeChange()

sys.exit(0)
