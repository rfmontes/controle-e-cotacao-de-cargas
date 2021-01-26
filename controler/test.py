from time import sleep

from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome, Firefox


def dolar():
    dolar_float = ''
    while dolar_float == '':
        try:
            nav_gc = Firefox()
            nav_gc.get('https://economia.uol.com.br/cotacoes/')
            html = nav_gc.page_source
            google_page = bs(html, 'html.parser')
            moedas = google_page.find_all(class_='value bra')
            dolar_str = str(moedas[0].text)
            dolar_str = dolar_str.replace('R$ ', '').replace(',', '.')
            dolar_float = float(dolar_str)
            # print(dolar_float)
        except IndexError:
            print('Tentando novamente!')
            nav_gc.close()
            continue
    nav_gc.close()
    print(f'U$$ 1,00 vale R$ {dolar_float:.3f}')
    return dolar_float


dolar()
