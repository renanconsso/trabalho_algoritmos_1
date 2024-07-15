from apartamento import *

class Lista:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, apartamento):
        if self.inicio is None:
            self.inicio = apartamento
            apartamento.vaga = 1
            
        else:
            anterior = None
            atual = self.inicio
            vaga = 1
            
            while atual is not None and atual.vaga == vaga:
                anterior = atual
                atual = atual.proximo
                vaga += 1
            
            apartamento.vaga = vaga
            
            if anterior is None:
                apartamento.proximo = self.inicio
                self.inicio = apartamento
            else:
                apartamento.proximo = anterior.proximo
                anterior.proximo = apartamento
        
        self.tamanho += 1


    def imprimir(self):
        if self.inicio == None:
            print("LISTA VAZIA")
        else:
            auxiliar = self.inicio
            print("--------------------------------------------------------------------")
            print("LISTA DE AP(s) COM VAGAS NA GARAGEM: ")
           
            while auxiliar:
                print(auxiliar)
                auxiliar = auxiliar.proximo
            print(f"TAMANHO DA LISTA: {self.tamanho}")
            print("--------------------------------------------------------------------")

    def excluir(self, vaga):
        if self.inicio == None:
            print("LISTA VAZIA.")
        elif self.tamanho == 1:
            if self.inicio.vaga == vaga:
                self.inicio.vaga = None
                self.inicio.proximo = None
                apExcluido = self.inicio
                self.inicio = None
                self.tamanho -= 1
                return apExcluido
            else:
                print("ID NÃO LOCALIZADO.")
        else:
            if self.inicio.vaga == vaga:
                auxiliar = self.inicio.proximo
                self.inicio.vaga = None
                self.inicio.proximo = None
                apExcluido = self.inicio
                self.inicio = auxiliar
                self.tamanho -= 1
                return apExcluido
            else:
                anterior = self.inicio
                auxiliar = anterior.proximo
                while auxiliar:
                    if auxiliar.vaga == vaga:
                        auxiliar.vaga = None
                        anterior.proximo = auxiliar.proximo
                        auxiliar.proximo = None
                        self.tamanho -= 1
                        return auxiliar
                    else:
                        anterior = auxiliar
                        auxiliar = anterior.proximo

