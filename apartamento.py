from torre import *

numeros_apartamentos = [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33, 40, 41, 42, 43, 50, 51, 52, 53, 60, 61, 62, 63]

class Apartamento:

    idContador = 1

    def __init__(self):
        self.id = Apartamento.idContador
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None        
        Apartamento.idContador += 1

    def _set_numero(self):
        while True:
            try:
                num = int(input("INSIRA O NÚMERO DO AP: "))
                if num in numeros_apartamentos:
                    if num in self.torre.apartamentos:
                        print("ESTA TORRE JÁ POSSUÍ ESSE AP CADASTRADO")
                    else:
                        self.numero = num
                        break
                else:
                    print("NÚMERO INVÁLIDO. POR FAVOR, ESCOLHA UM NÚMERO DE AP EXISTENTE")
            except ValueError:
                print("DIGITE UM NÚMERO VÁLIDO.")

    def _set_torre(self):
        print("---------------------------------------------------------------------")
        print("LISTA DE TORRES CADASTRADAS.")
        print("---------------------------------------------------------------------")
        indice = 1
        for torre in torres:
            print(f"TORRE {indice}: {torre}. \n")
            indice += 1
        while True:
            try:
                idTorre = int(input("DIGITE O ID DA TORRE QUE VAI RECEBER O AP: "))
                if idTorre > 0 and idTorre <= len(torres):
                    self.torre = torres[idTorre - 1]
                    break
                else:
                    print("DIGITE UM ID VÁLIDO DA TORRE.")
            except ValueError:
                print("DIGITE UM NÚMERO VÁLIDO.")

    def cadastrar(self):
        self._set_torre()
        self._set_numero()
        self.torre.apartamentos.append(self.numero)

    def __str__(self):
        return f"AP {self.numero}, VAGA: {self.vaga}, TORRE: {self.torre.nome}. ID: {self.id}"

    def imprimir(self):
        print(self)
