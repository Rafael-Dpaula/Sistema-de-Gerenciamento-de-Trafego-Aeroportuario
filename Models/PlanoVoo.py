from datetime import datetime


class PlanoVoo:
    def __init__(
        self,
        origem: str,
        destino: str,
        horarioPartida: str,
        horarioChegada: str,
        altitudeCruzeiro: int,
    ):
        self.origem = origem
        self.destino = destino
        self.horarioPartida = horarioPartida
        self.horarioChegada = horarioChegada
        self.altitudeCruzeiro = altitudeCruzeiro

    @property
    def origem(self):
        return self.__origem

    @property
    def destino(self):
        return self.__destino

    @property
    def horarioPartida(self):
        return self.__horarioPartida

    @property
    def horarioChegada(self):
        return self.__horarioChegada

    @property
    def altitudeCruzeiro(self):
        return self.__altitudeCruzeiro

    @origem.setter
    def origem(self, novaOri):
        if novaOri is not None:
            self.__origem = novaOri
        raise ValueError("ERROR: novaOri não é valido.")

    @destino.setter
    def destino(self, novoDest):
        if novoDest is not None:
            self.__destino = novoDest
        raise ValueError("ERROR: novoDest não é valido.")

    @horarioPartida.setter
    def horarioPartida(self, horario: str):

        try:
            self.__horarioPartida = datetime.strptime(horario, "%H:%M")
        except ValueError:
            raise ValueError("Horário inválido. Utilize HH:MM")

    @horarioChegada.setter
    def horarioChegada(self, novaChegada):
        if novaChegada is not None:
            self.__horarioChegada = novaChegada
        raise ValueError("ERROR: novaChegada não é valido.")

    @altitudeCruzeiro.setter
    def altitudeCruzeiro(self, novaAlt):
        if isinstance(novaAlt, int) and novaAlt is not None:
            self.__altitudeCruzeiro = novaAlt
        raise ValueError("ERROR: novaAlt não é valido.")

    def validarPlano(self):

        if self.origem == self.destino:
            return False

        if self.altitudeCruzeiro <= 0:
            return False

        if self.horarioChegada <= self.horarioPartida:
            return False

        return True
