from Models.Aeroporto import Aeroporto
from Models.ControleVoo import ControleVoo
from Models.Avioes.Aviao import Aviao


class CentroOperacional:
    def __init__(self, aeroporto: Aeroporto, controleVoo: ControleVoo):
        self.aeroporto = aeroporto
        self.controleVoo = controleVoo

    @property
    def aeroporto(self):
        return self.__aeroporto

    @property
    def controleVoo(self):
        return self.__controleVoo

    @aeroporto.setter
    def aeroporto(self, novoAero):
        if not isinstance(novoAero, Aeroporto):
            raise ValueError(
                "ERROR: novoAero não é uma instância válida de Aeroporto."
            )
        self.__aeroporto = novoAero

    @controleVoo.setter
    def controleVoo(self, novoControle):
        if not isinstance(novoControle, ControleVoo):
            raise ValueError(
                "ERROR: novoControle não é uma instância válida de ControleVoo."
            )
        self.__controleVoo = novoControle

    def autorizarPouso(self, aviao: Aviao):
        if aviao not in self.__controleVoo.filaPouso:
            print(f"ALERT: a aeronave {aviao.identificador} não está na fila de pouso.")
            return
        pista = self.__aeroporto.buscarPistaDisponivel()
        if pista is None:
            print("ALERT: não existem pistas disponíveis.")
            return
        pista.ocupar(aviao)
        self.__controleVoo.autorizarPouso(aviao)
        print(aviao.pousar())
        return pista

    def autorizarDecolagem(self, aviao: Aviao):
        if aviao not in self.__controleVoo.filaDecolagem:
            print(
                f"ALERT: a aeronave {aviao.identificador} não está na fila de decolagem."
            )
            return
        pista = self.__aeroporto.buscarPistaDisponivel()
        if pista is None:
            print("ALERT: não existem pistas disponíveis.")
            return
        plataformaUtilizada = None
        for plataforma in self.__aeroporto.plataformas:
            if plataforma.aviao == aviao:
                plataformaUtilizada = plataforma
                break
        if plataformaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma plataforma.")
            return
        plataformaUtilizada.liberar()
        pista.ocupar(aviao)
        self.__controleVoo.autorizarDecolagem(aviao)
        print(aviao.decolar())
        return pista
    
    def processarPouso(self, aviao: Aviao):
        plataforma = self.__aeroporto.buscarPlataformaDisponivel()
        if plataforma is None:
            print("ALERT: não existem plataformas disponíveis.")
            return
        pistaUtilizada = None
        for pista in self.__aeroporto.pistas:
            if pista.aviao == aviao:
                pistaUtilizada = pista
                break
        if pistaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma pista.")
            return
        print(aviao.pousar())
        plataforma.ocupar(aviao)
        pistaUtilizada.liberar()
        
    def processarDecolagem(self, aviao: Aviao):
        if aviao is None or not isinstance(aviao, Aviao):
            raise ValueError(
                "ERROR: aviao não é uma instância válida de Aviao."
            )
        pistaUtilizada = None
        for pista in self.__aeroporto.pistas:
            if pista.aviao == aviao:
                pistaUtilizada = pista
                break
        if pistaUtilizada is None:
            print("ALERT: aeronave não está ocupando nenhuma pista.")
            return
        print(aviao.decolar())
        pistaUtilizada.liberar()
