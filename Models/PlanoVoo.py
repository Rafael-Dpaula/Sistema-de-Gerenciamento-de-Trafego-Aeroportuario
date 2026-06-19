from datetime import datetime, timedelta


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
        return self._origem

    @property
    def destino(self):
        return self._destino

    @property
    def horarioPartida(self):
        return self._horarioPartida

    @property
    def horarioChegada(self):
        return self._horarioChegada

    @property
    def altitudeCruzeiro(self):
        return self._altitudeCruzeiro

    @origem.setter
    def origem(self, novaOri):
        if novaOri is None:
            raise ValueError("ERROR: novaOri não é valido.")
        self._origem = novaOri

    @destino.setter
    def destino(self, novoDest):
        if novoDest is None:
            raise ValueError("ERROR: novoDest não é valido.")
        self._destino = novoDest

    @horarioPartida.setter
    def horarioPartida(self, novoHorario: str):
        try:
            self._horarioPartida = datetime.strptime(novoHorario, "%H:%M").time()
        except ValueError:
            raise ValueError("Horário inválido. Utilize HH:MM")

    @horarioChegada.setter
    def horarioChegada(self, novoHorario):
        try:
            self._horarioChegada = datetime.strptime(novoHorario, "%H:%M").time()
        except ValueError:
            raise ValueError("Horário inválido. Utilize HH:MM")

    @altitudeCruzeiro.setter
    def altitudeCruzeiro(self, novaAlt):
        if not isinstance(novaAlt, int) or novaAlt is None:
            raise ValueError("ERROR: novaAlt não é valido.")
        self._altitudeCruzeiro = novaAlt

    def __str__(self):
        return (
            "====== PLANO VOO =====\n"
            f"Origem = {self._origem}\n"
            f"Destino = {self._destino}\n"
            f"Horario de partida = {self._horarioPartida}\n"
            f"Horario de chegada = {self._horarioChegada}\n"
            f"Altitude de Cruzeiro = {self._altitudeCruzeiro}\n"
            "======================\n"
        )

    def validarPlano(self):
        if self.origem == self.destino:
            return False

        if self.altitudeCruzeiro <= 0:
            return False

        if self.horarioChegada <= self.horarioPartida:
            return False

        return True
    
    def calcularDuracao(self):
        partida = datetime.combine(datetime.today(), self._horarioPartida)
        chegada = datetime.combine(datetime.today(), self._horarioChegada)
        if chegada < partida:
            chegada += timedelta(days=1)
        return chegada - partida

