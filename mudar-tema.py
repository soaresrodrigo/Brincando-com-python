#!/usr/bin/python
##
#  Esse script serve para configurar o tema de exibição, do shell e do desktop. A lógica é alterar dinamicante entre claro se tiver de manhã e escuro se tiver de noite, assim descansa a visão.
import os
import datetime
import time

# Transforma a prioridade em muito baixa
os.nice(20)

# Configura a hora a ser executada
def configTime():
    hora_atual   = datetime.datetime.now().hour
    if hora_atual >= 6 and hora_atual < 22:
        return True
    return False

# Retorna a mensagem como notificação
def exeChange():
    if configTime() is True:
        theme       = "'McOS-MJV'"
        shell       = 'Sierra-light'
        brightness  = '1'
    else:
        theme       = "'McOS-MJV-Dark-mode'"
        shell       = 'Sierra-dark'
        brightness  = '0.7'

    theme_atual = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
    theme_atual = theme_atual.replace("\n","")
    
    if theme_atual != theme:
        setTheme(theme, shell, brightness)  
        
    #Loop controlado para verificar a cada hora
    verifyTheme()
    
# Calcula os minutos que faltam pra completar alguma hora, depois manda o programa começar a validação
def verifyTheme():
    # Primeiro calcula os minutos restante e transforma em segundos, depois diminue com os segundos passados
    second_left = ((60 - datetime.datetime.now().minute)*60) - (60 - datetime.datetime.now().second)
    time.sleep(second_left)

    return exeChange()

# Aqui é a alteração dos temas
def setTheme(theme, shell, brightness):
    os.system('gsettings set org.gnome.desktop.interface gtk-theme "{0}"'.format(theme)) #Tema
    os.system('gsettings set org.gnome.shell.extensions.user-theme name "{0}"'.format(shell)) #Shell
    os.system('xrandr --output VGA1 --brightness {0}'.format(brightness)) #Brilho tela
    os.system('notify-send -i /home/rodrigo/Imagens/Icones/theme.png "Mudei o tema" "Trabalhe com uma iluminação melhor"') #Mensagem da notificação
    
exeChange()