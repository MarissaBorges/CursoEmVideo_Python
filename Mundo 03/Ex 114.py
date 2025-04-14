# -----------------------------------------------
#    EXERCÍCIO 114
# -----------------------------------------------

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('\033[31mO site Pudim NÃO esta acessivel no momento\033[m')
else:
    print('\033[32mO site Pudim esta acessível no momento\033[m')