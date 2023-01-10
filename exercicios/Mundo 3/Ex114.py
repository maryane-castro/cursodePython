'''Crie um codigo em python que teste se o site pudim está 
acessivel pelo computador usado.'''

import urllib3

url = 'http://www.pudim.com.br/'
http = urllib3.PoolManager()
try:
    urlcode = http.request('GET', url)
except:
    print('\033[1;31mFoi impossivel conectar ao site pudim!\033[m')
else:
    print('\033[1;32mO site pudim ta funcionando!\033[m')
