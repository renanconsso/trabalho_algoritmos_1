from lista_vagas import *
from fila_espera import *

listaVagasGaragem = Lista()
filaEspera = Fila()

def cadastrar_torres():
    novaTorre = Torre()
    novaTorre.cadastrar()
    print("TORRE CADASTRADA.")
    novaTorre.imprimir()

def cadastrar_apartamentos():
    if len(torres) == 0:
        print("ERRO!")
        print("NÃO PODE CADASTRAR APARTAMENTOS ENQUANTO NÃO HOUVER TORRES CADASTRADAS.")
        return
    else:
        novoAp = Apartamento()
        novoAp.cadastrar()
        if listaVagasGaragem.tamanho < 10:
            listaVagasGaragem.adicionar(novoAp)
        else:
            filaEspera.adicionar(novoAp)
        print("APARTAMENTO CADASTRADO")
        novoAp.imprimir()
        return

def liberar_vaga():
    if listaVagasGaragem.tamanho == 0:
        print("NÃO EXISTEM VAGAS PARA SEREM LIBERADAS.")
        return
    while True:
        try:
            vagaExcluida = int(input("INFORME O NÚMERO DA VAGA QUE DESEJA LIBERAR: "))
            if 1 <= vagaExcluida <= 10:
                vagaOcupada = False
                auxiliar = listaVagasGaragem.inicio
                while auxiliar:
                    if auxiliar.vaga == vagaExcluida:
                        vagaOcupada = True
                        break
                    auxiliar = auxiliar.proximo 
                if vagaOcupada:
                    break
                else:
                    print("VAGA NÃO EXISTE.")
                    return
            else:
                print("DIGITE UM NÚMERO DE 1 A 10.")
        except:
            print("DIGITE UM NÚMERO VÁLIDO")
    apExcluido = listaVagasGaragem.excluir(vagaExcluida)
    if filaEspera.tamanho > 0:
        apParaReceberVaga = filaEspera.inicio
        filaEspera.remover()
        listaVagasGaragem.adicionar(apParaReceberVaga)
    filaEspera.adicionar(apExcluido)

def ver_fila():
    filaEspera.imprimir()

def ver_lista():
    listaVagasGaragem.imprimir()

def menu():
    opcoes = {
        1: cadastrar_torres,
        2: cadastrar_apartamentos,
        3: liberar_vaga,
        4: ver_fila,
        5: ver_lista,
        6: lambda: print("FIM.")
    }

    while True:
        print("---------------------------------------------------------")
        print("MENU DO CONDOMÍNIO")
        print("---------------------------------------------------------")
        print("SELECIONE: ")
        print("1 CADASTRAR TORRE")
        print("2 CADASTRAR APARTAMENTO")
        print("3 LIBERAR VAGA DA GARAGEM")
        print("4 VER FILA DE ESPERA")
        print("5 VISUALIZAR LISTA DA GARAGEM")
        print("6 SAIR")
        print("---------------------------------------------------------")

        try:
            escolha_usuario = int(input("QUAL OPÇÃO VOCÊ QUER? "))
            if escolha_usuario < 1 or escolha_usuario > 6:
                print("ESCOLHA UM NÚMERO QUE CONTENHA NO MENU")
            else:
                opcoes[escolha_usuario]()
                if escolha_usuario == 6:
                    break
        except ValueError:
            print("DIGITE UM NÚMERO VÁLIDO")




