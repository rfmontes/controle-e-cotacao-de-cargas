from time import sleep

from controler.arquivos import *
from controler.interface import *


arq = 'Materiais.txt'
arq_retirar = 'Retirar.txt'
arq_caminhao = 'Caminhao.txt'
arq_carga = 'Cargas.txt'

lista_arquivos = [arq_retirar, arq_caminhao, arq_carga]

if arquivoExiste(lista_arquivos):
    criarArquivo(lista_arquivos)

preco_carga_total = 0

while True:
    resposta = menu(['Retiradas', 'Peso do Caminhão', 'Relatório de Eventos', 'Sair'])
    if resposta == 1:
        cabecalho('Quantidade de Retiradas')
        retirar = retiradas()
        cont = 0
        menuLerArquivo(arq)
        while cont != retirar:
            material = escolhaMaterial(cont)
            nome_preco_metal = menuMateriais(material)
            cont += 1
            cadastrar(arq_retirar, nome_preco_metal)

    elif resposta == 2:
        cont = 0
        print(linha())
        print(f'Sera feita {retirar} retiradas!')
        peso = float(input('Peso do caminhão vazio: '))
        CadastraPesoCaminhao(arq_caminhao, peso)
        print(linha())
        while cont != retirar:
            peso = float(input(f'Peso com {cont + 1}° carga: '))
            preco = getPreco(arq_retirar, cont)
            peso_tira = getPesoCarga(arq_caminhao, cont)
            preco_carga = ((peso - peso_tira) / 1000) * preco
            # preco_carga = ((peso - getPesoCarga(arq_caminhao, cont)) / 1000) * preco
            # print(f'- Peso da carga de ??? {peso - peso_tira:.0f} Kg')
            # print(f'- Preço da carga de ??? R$ {preco_carga:.2f}')
            preco_carga_total += preco_carga
            cont += 1
            CadastraPesoCaminhao(arq_caminhao, peso)
            CadastraPrecoCarga(arq_carga, preco_carga, peso=peso-peso_tira)

        print(f'Peso final do caminhão {peso:.0f} Kg')
        print(f'Preço total das cargas R$ {preco_carga_total:.2f}')

    elif resposta == 3:
        cabecalho('RELATÓRIO DE EVENTOS')
        lerCadastro(arq_retirar, 'Materiais selecionados\nPreço da Tonelada com base na LME')
        lerCadastroCaminhao(arq_caminhao, 'Pesagens Realizadas')
        lerCadastroCarga(arq_carga, 'Preço e Peso das Cargas')
        sleep(3)

    elif resposta == 4:
        cabecalho('Saindo do sistema!')
        break
    else:
        print('\033[031mERRO! Digite uma opção válida!\033[m')
    sleep(2)

