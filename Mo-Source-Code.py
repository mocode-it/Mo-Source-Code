#------------------------------#
#Devolper : Mokhtar Abdelkreem
#------------------------------#
# You In Right Place ...
#--------------------------#
import os
import time
import requests
import webbrowser
import json
#-----------------------#
print('\033[1;31mWait ...')
time.sleep(1)
os.system('clear')
os.system('xdg-open https://cutt.us/mocode')
webbrowser.open('https://cutt.us/mocode')
os.system('python3 -m pip install --upgrade pip')
os.system('pip install requests')
os.system('pip2 install requests')
os.system('clear')
print('''\033[1;36m
┏━┓┏━┓━━━━━━━━━━┓━━━━━━━━━━━━━━━━━━━━━┓━━━━┏┓━━━
┃┃┗┛┃┃━━━━━━━┏━┓┃━━━━━━━━━━━━━━━━━━┏━┓┃━━━━┃┃━━━
┃┏┓┏┓┃━━┓━━━━┗━━┓━━┓┓┏┓━┓━━┓━━┓━━━━┃━┗┛━━┓━┛┃━━┓
┃┃┃┃┃┃┏┓┃━━━┓━━┓┃┏┓┃┃┃┃┏┛┏━┛┏┓┃━━━┓┃━┏┓┏┓┃┏┓┃┏┓┃
┃┃┃┃┃┃┗┛┃━━━┛┗━┛┃┗┛┃┗┛┃┃━┗━┓┃━┫━━━┛┗━┛┃┗┛┃┗┛┃┃━┫
┗┛┗┛┗┛━━┛━━━━━━━┛━━┛━━┛┛━━━┛━━┛━━━━━━━┛━━┛━━┛━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

        Devolper : Mokhtar Abdelkreem

	Try By Your Self Be The Best .

	No Thing is Named Impossible .

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')
url = input('\033[1;35mWeb Target : ')
print('')
source = requests.get(url)
#out = print(source.text)
path_file = str(input('Your File Path : '))
file = open(path_file,"w")
file.write(source.text)
file.close()

#-------- Finished Code ---------#


