import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.Factory.FactoryAvioes import FactoryAviao
from Models.Plataforma import Plataforma

plataforma = Plataforma(12)
aviao = FactoryAviao.criarAviao(tipo="Privado", identificador="Falcoa", modelo="A277", proprietario="Melon Musk", numeroPassageiros=8)

print(plataforma)
plataforma.ocupar(aviao)
print(plataforma)
print("Disponível? ","Sim" if plataforma.disponivel() else "Não")
plataforma.liberar()
print(plataforma)
print("Disponível? ","Sim" if plataforma.disponivel() else "Não")
