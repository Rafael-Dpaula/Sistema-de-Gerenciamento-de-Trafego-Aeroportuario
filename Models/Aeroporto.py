from Models.Pista import Pista
from Models.Plataforma import Plataforma
class Aeroporto:
    def __init__(self, nome: str, codigo: str, cidade: str):
        self.nome = nome
        self.codigo = codigo
        self.cidade = cidade
        self._pistas: list[Pista] = []
        self._plataformas: list[Plataforma] = []


    @property
    def nome(self):
        return self._nome


    @property
    def codigo(self):
        return self._codigo


    @property
    def cidade(self):
        return self._cidade


    @property
    def pistas(self):
        return self._pistas


    @property
    def plataformas(self):
        return self._plataformas


    @nome.setter
    def nome(self, novoNome):
        if not novoNome is None:
            self._nome = novoNome

        else:
            raise ValueError("ERROR: novoNome não é válido.")

    @codigo.setter
    def codigo(self, novoCodigo):
        if not novoCodigo is None:
            self._codigo = novoCodigo

        else:
            raise ValueError("ERROR: novoCodigo não é válido.")

    @cidade.setter
    def cidade(self, novaCidade):
        if not novaCidade is None:
            self._cidade = novaCidade

        else:
            raise ValueError("ERROR: novaCidade não é valida.")

    def __str__(self):
        return f"====== AEROPORTO =====\nNome = {self._nome}\nCodigo = {self._codigo}\nCidade = {self._cidade}\nPistas = {[f"{p._codigo} | Vazia" if p._aviao is None else f"{p._codigo}|{p._aviao._identificador}" for p in self._pistas]}\nPlataformas = {[f"{p._codigo} | Vazia" if p._aviao is None else f"{p._codigo}|{p._aviao._identificador}" for p in self._plataformas]}\n======================\n"

    def adicionarPista(self, pista: Pista):
        if pista is None or not isinstance(pista, Pista):
            raise ValueError("ERROR: pista não é uma instancia válida de Pista.")
        if pista not in self._pistas:
            self._pistas.append(pista)


    def adicionarPlataforma(self, plataforma: Plataforma):
        if plataforma is None or not isinstance(plataforma, Plataforma):
            raise ValueError("ERROR: plataforma não é uma instancia válida de Plataforma.")
        if plataforma not in self._plataformas:
            self._plataformas.append(plataforma)


    def removerPista(self, pista: Pista):
        if not pista is None and isinstance(pista, Pista):
            if pista in self._pistas:
                self._pistas.remove(pista)

            else:
                print("ALERT: pista não está em pistas.")
        else:
            raise ValueError("ERROR: pista não é uma instancia válida de Pista.")

    def removerPlataforma(self, plataforma: Plataforma):
        if not plataforma is None and isinstance(plataforma, Plataforma):
            if plataforma in self._plataformas:
                self._plataformas.remove(plataforma)

            else:
                print("ALERT: plataforma não está em plataformas.")
        else:
            raise ValueError("ERROR: plataforma não é uma instancia válida de Plataforma.")
    
    def buscarPistaDisponivel(self):
        for pista in self._pistas:
            if pista.disponivel():
                return pista
        return None
    
    def buscarPlataformaDisponivel(self):
        for plataforma in self._plataformas:
            if plataforma.disponivel():
                return plataforma
        return None

