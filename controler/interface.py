from valores import valorMetal


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mERRO: por favor, digite um número válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar um número.')
            return 0
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[033m{c}\033[m - \033[034m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[032mDigite a opção: \033[m')
    return opc


def retiradas():
    retirar = leiaInt('Quantidade de Retiradas: ')
    if retirar == 1:
        print('Selecione 1 material')
    elif retirar == 2:
        print('Selecione 2 materiais')
    elif retirar == 3:
        print('Selecione 3 materiais')
    elif retirar == 4:
        print('Selecione 4 materiais')
    else:
        print('Quantidade excedida!')
    print(linha())
    return retirar


def menuLerArquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('ERRO ao abrir Menu')
    else:
        c = 1
        for linha_arq in a:
            linha_arq = linha_arq.replace('\n', '')
            print(f'{c} - {linha_arq}')
            c += 1
        # print(linha())
        # material = leiaInt(f'Escolha {cont+1}° Material: ')
        # return material


def escolhaMaterial(cont):
    print(linha())
    c = 1
    material = leiaInt(f'Escolha {cont + 1}° Material: ')
    c += 1
    return material


def menuMateriais(material=None):
    global nome_metal, metal_float_dolar
    print(linha())
    if material == 1:
        nome_metal = 'Alumínio'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Aluminium#tabIndex=0')
    elif material == 2:
        nome_metal = 'Cobre'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Copper#tabIndex=0')
    elif material == 3:
        nome_metal = 'Chumbo'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Lead#tabIndex=0')
    elif material == 4:
        nome_metal = 'Níquel'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Nickel#tabIndex=0')
    elif material == 5:
        nome_metal = 'Estanho'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Tin#tabIndex=0')
    elif material == 6:
        nome_metal = 'Zinco'
        print(nome_metal)
        metal_float_dolar = valorMetal('Non-ferrous/Zinc#tabIndex=0')
    elif material == 7:
        nome_metal = 'Vergalhões de aço'
        print(nome_metal)
        metal_float_dolar = valorMetal('Ferrous/Steel-Rebar#tabIndex=0', 1)
    elif material == 8:
        nome_metal = 'Sucata de aço'
        print(nome_metal)
        metal_float_dolar = valorMetal('Ferrous/Steel-Scrap#tabIndex=0', 1)
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
    return f'{nome_metal}; {metal_float_dolar:.2f}'
