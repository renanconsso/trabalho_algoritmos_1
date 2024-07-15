torres = []

class Torre:

    idContador = 1

    def __init__(self):
        self.id = Torre.idContador
        self.nome = None
        self.endereco = None
        self.apartamentos = []
        Torre.idContador += 1

    def _set_nome(self):
        while True:
            nome = input("QUAL NOME DA TORRE QUE IRÁ CADASTRAR? ").strip()
            if nome:
                self.nome = nome
                break
            else:
                print("DIGITE UM NOME VÁLIDO")

    def _set_endereco(self):
        while True:
            end = input("QUAL ENDEREÇO DA TORRE QUE IRÁ CADASTRAR? ").strip()
            if end:
                self.endereco = end
                break
            else:
                print("DIGITE UM ENDEREÇO VÁLIDO")

    def cadastrar(self):
        self._set_nome()
        self._set_endereco()
        torres.append(self)

    def __str__(self):
        return f"TORRE {self.nome}, LOCALIZADA NO ENDEREÇO: {self.endereco}. ID DA TORRE: {self.id}"

    def imprimir(self):
        print(self)
