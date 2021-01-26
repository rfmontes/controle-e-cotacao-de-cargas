from controler.interface import cabecalho


def arquivoExiste(nome):
    for n in nome:
        try:
            a = open(n, 'rt')
            a.close()
        except FileNotFoundError:
            return False
    else:
        return True

# def arquivoExiste(nome):
#     try:
#         a = open(nome, 'rt')
#         a.close()
#     except FileNotFoundError:
#         return False
#     else:
#         return True


def criarArquivo(nome):
    for n in nome:
        try:
            a = open(n, 'wt+')
            a.close()
        except:
            print('Houve um ERRO na criação do arquivo')

# def criarArquivo(nome):
#     try:
#         a = open(nome, 'wt+')
#         a.close()
#     except:
#         print('Houve um ERRO na criação do arquivo')


def lerArquivo(nome, msgCabecalho):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabecalho(msgCabecalho)
        c = 1
        for linha in a:
            linha = linha.replace('\n', '')
            print(f'{c} - {linha}')
            c += 1
    finally:
        a.close()


def cadastrar(arq_retirar, nome_metal):
    try:
        a = open(arq_retirar, 'at', encoding='UTF-8')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome_metal}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            # print(f'Novo registro realizado com sucesso!')
            a.close()


def lerCadastro(nome, msgCabecalho):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabecalho(msgCabecalho)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<25} R$ {dado[1]}')
    finally:
        a.close()


def CadastraPesoCaminhao(arq_caminhao, peso):
    try:
        a = open(arq_caminhao, 'at', encoding='UTF-8')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{peso:.0f}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            # print(f'Novo registro realizado com sucesso!')
            a.close()


def lerCadastroCaminhao(nome, msgCabecalho, msg=None):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabecalho(msgCabecalho)
        msg = f'Peso do caminhão vazio:'
        cont = 0
        for linha in a:
            linha = linha.replace('\n', '')
            print(f'{msg:<25}  {linha:>10} Kg')
            msg = f'Peso com {cont + 1}° carga: '
            cont += 1
    finally:
        a.close()


def getPreco(nome, cont=0):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        linhas = a.readlines()
        dado = linhas[cont].split(';')[1].replace('\n', '').replace(' ', '')
        preco = dado
        preco = float(preco)
        a.close()
    finally:
        a.close()
    return preco


def getPesoCarga(nome, cont=0):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        linhas = a.readlines()
        dado = linhas[cont].replace('\n', '').replace(' ', '')
        peso = dado
        peso = float(peso)
        a.close()
    finally:
        a.close()
    return peso


def CadastraPrecoCarga(arq_carga, preco_carga, peso):
    try:
        a = open(arq_carga, 'at', encoding='UTF-8')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{peso:.0f}; {preco_carga:.2f}\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            # print(f'Novo registro realizado com sucesso!')
            a.close()


def lerCadastroCarga(nome, msgCabecalho):
    try:
        a = open(nome, 'rt', encoding='UTF-8')
    except:
        print('ERRO ao ler arquivo')
    else:
        cabecalho(msgCabecalho)
        cont = 0
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            msg = f'{cont + 1}° carga: '
            print(f'{msg} {dado[0]} Kg    -   R$ {dado[1]}')
            cont += 1
    finally:
        a.close()
