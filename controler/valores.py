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


def valorMetal(url, coluna=2):
    nav_gc_m = Firefox()
    nav_gc_m.get('https://www.lme.com/Metals/' + url)
    html = nav_gc_m.page_source
    lme_page = bs(html, 'html.parser')
    metal_valor = lme_page.find_all('td')[coluna]
    metal_str = str(metal_valor.text)
    metal_float = float(metal_str)
    nav_gc_m.close()
    dolar_float = dolar()
    metal_float_dolar = metal_float * dolar_float
    print(f'Tonelada em U$$ {metal_float:.2f}')
    # dolar = dolar_float
    print(f'Tonelada em R$ {metal_float_dolar :.2f}')
    return metal_float_dolar


# dolar_float = ''
# while dolar_float == '':
#     try:
#         nav_gc = webdriver.Chrome()
#         nav_gc.get('https://economia.uol.com.br/cotacoes/')
#         html = nav_gc.page_source
#         google_page = bs(html, 'html.parser')
#         moedas = google_page.find_all(class_='value bra')
#         dolar_str = str(moedas[0].text)
#         dolar_str = dolar_str.replace('R$ ', '').replace(',', '.')
#         dolar_float = float(dolar_str)
#         # print(dolar_float)
#     except IndexError:
#         print('Tentando novamente!')
#         nav_gc.close()
#         continue
# nav_gc.close()
# print(f'U$$ 1,00 vale R$ {dolar_float:.3f}')