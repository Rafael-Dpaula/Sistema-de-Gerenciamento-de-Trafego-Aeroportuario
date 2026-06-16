from Models.ControleVoo import ControleVoo
from Models.Pista import Pista
from Models.Plataforma import Plataforma
class Aeroporto:
    def __init__(self, nome: str, codigo: str, cidade: str):
        self.nome = nome
        self.codigo = codigo
        self.cidade = cidade
        self.__controleVoo: ControleVoo = ControleVoo()
        self.__pistas: list[Pista] = []
        self.__plataformas: list[Plataforma] = []

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cidade(self):
        return self.__cidade

    @property
    def controleVoo(self):
        return self.__controleVoo

    @property
    def pistas(self):
        return self.__pistas

    @property
    def plataformas(self):
        return self.__plataformas

    @nome.setter
    def nome(self, novoNome):
        if not novoNome is None:
            self.__nome = novoNome
        else:
            raise ValueError("ERROR: novoNome não é válido.")

    @codigo.setter
    def codigo(self, novoCodigo):
        if not novoCodigo is None:
            self.__codigo = novoCodigo
        else:
            raise ValueError("ERROR: novoCodigo não é válido.")

    @cidade.setter
    def cidade(self, novaCidade):
        if not novaCidade is None:
            self.__cidade = novaCidade
        else:
            raise ValueError("ERROR: novaCidade não é valida.")

    def adicionarPista(self, pista: Pista):
        if pista is None or not isinstance(pista, Pista):
            raise ValueError("ERROR: pista não é uma instancia válida de Pista.")
        if pista not in self.__pistas:
            self.__pistas.append(pista)

    def adicionarPlataforma(self, plataforma: Plataforma):
        if plataforma is None or not isinstance(plataforma, Plataforma):
            raise ValueError("ERROR: plataforma não é uma instancia válida de Plataforma.")
        if plataforma not in self.__plataformas:
            self.__plataformas.append(plataforma)

    def removerPista(self, pista: Pista):
        if not pista is None and isinstance(pista, Pista):
            if pista in self.__pistas:
                self.__pistas.remove(pista)
            else:
                print("ALERT: pista não está em pistas.")
        else:
            raise ValueError("ERROR: pista não é uma instancia válida de Pista.")

    def removerPlataforma(self, plataforma: Plataforma):
        if not plataforma is None and isinstance(plataforma, Plataforma):
            if plataforma in self.__plataformas:
                self.__plataformas.remove(plataforma)
            else:
                print("ALERT: plataforma não está em plataformas.")
        else:
            raise ValueError("ERROR: plataforma não é uma instancia válida de Plataforma.")
    
    def buscarPistaDisponivel(self):
        for pista in self.__pistas:
            if pista.disponivel():
                return pista
        return None
    
    def buscarPlataformaDisponivel(self):
        for plataforma in self.__plataformas:
            if plataforma.disponivel():
                return plataforma
        return None