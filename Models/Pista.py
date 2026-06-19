from Models.Avioes.Aviao import Aviao
class Pista:
    def __init__(self, codigo: int):
        self.codigo = codigo
        self._aviao: Aviao = None

    @property
    def codigo(self):
        return self._codigo

    @property
    def aviao(self):
        return self._aviao

    @codigo.setter
    def codigo(self, novoCodigo):
        if not novoCodigo is None and isinstance(novoCodigo, int):
            self._codigo = novoCodigo
        else:
            raise ValueError("ERROR: novoCodigo não é válido.")

    def __str__(self):
        return f"===== PISTA =====\nCodigo = {self._codigo}\nAviao = {'nenhum' if self._aviao is None else self._aviao._identificador}\n================="
        
    def ocupar(self, aviao: Aviao):
        if self._aviao is not None:
            print("ALERT: pista ocupada.")
            return
        if not isinstance(aviao, Aviao):
            raise ValueError("ERROR: aviao não é uma instância válida de Aviao.")
        self._aviao = aviao

    def liberar(self):
        if not self._aviao is None:
            self._aviao = None
        else:
            print("ALERT: a pista já está disponível.")

    def disponivel(self):
        return self._aviao is None

