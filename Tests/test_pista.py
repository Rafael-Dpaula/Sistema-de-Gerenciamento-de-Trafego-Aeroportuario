import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.Factory.FactoryAvioes import FactoryAviao
from Models.Pista import Pista

aviao = FactoryAviao.criarAviao(tipo="Privado", identificador="Falcoa", modelo="A277", proprietario="Melon Musk", numeroPassageiros=8)
pista = Pista(3)

print(pista)
pista.ocupar(aviao)
print(pista)
print("Disponível? ","Sim" if pista.disponivel() else "Não")
pista.liberar()
print(pista)
print("Disponível? ","Sim" if pista.disponivel() else "Não")