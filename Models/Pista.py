from Models.Avioes import Aviao
class Pista:
    def __init__(self, codigo: int):
        self.codigo = codigo
        self.__aviao: Aviao = None

    @property
    def codigo(self):
        return self.__codigo

    @property
    def aviao(self):
        return self.__aviao

    @codigo.setter
    def codigo(self, novoCodigo):
        if not novoCodigo is None and isinstance(novoCodigo, int):
            self.__codigo = novoCodigo
        else:
            raise ValueError("ERROR: novoCodigo não é válido.")

    def ocupar(self, aviao: Aviao):
        if self.__aviao is not None:
            print("ALERT: pista ocupada.")
            return
        if aviao is None or not isinstance(aviao, Aviao):
            raise ValueError("ERROR: aviao não é uma instância válida de Aviao.")
        self.__aviao = aviao

    def liberar(self):
        if not self.__aviao is None:
            self.__aviao = None
        else:
            print("ALERT: a pista já está disponível.")

    def disponivel(self):
        return self.__aviao is None
