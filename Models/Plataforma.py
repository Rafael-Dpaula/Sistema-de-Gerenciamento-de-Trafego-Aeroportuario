from Models.Avioes.Aviao import Aviao
class Plataforma:
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
        
    @aviao.setter
    def aviao(self, novoAvi):
        if not novoAvi is None and isinstance(novoAvi, Aviao):
            self._aviao = novoAvi
        else:
            raise ValueError("ERROR: novoAvi não é válido.")

    def __str__(self):
        return (
            f"===== PLATAFORMA =====\n"
            f"Codigo = {self._codigo}\n"
            f"Aviao = {'nenhum' if self._aviao is None else self._aviao._identificador}\n"
            "======================\n"
        )

    def ocupar(self, aviao: Aviao):
        if self._aviao is not None:
            print("ALERT: plataforma ocupada.")
            return
        if not isinstance(aviao, Aviao):
            raise ValueError("ERROR: aviao não é uma instância válida de Aviao.")
        self._aviao = aviao

    def liberar(self):
        if not self._aviao is None:
            self._aviao = None
        else:
            print("ALERT: a plataforma já está disponível.")

    def disponivel(self):
        return self._aviao is None

