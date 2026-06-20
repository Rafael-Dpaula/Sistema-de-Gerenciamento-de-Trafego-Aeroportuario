import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.Aeroporto import Aeroporto
from Models.Pista import Pista
from Models.Plataforma import Plataforma
from Models.Factory.FactoryAvioes import FactoryAviao

aeroporto = Aeroporto("Aeroporto internacional", "AERP12", "Passo Fundo | RS")
pista = Pista(0)
plataforma1 = Plataforma(0)
plataforma2 = Plataforma(1)

aviao = FactoryAviao.criarAviao(tipo="Transporte", identificador="BTR1123", modelo="KC-390 Millennium", tipoCarga="Eletrodomesticos", pesoCarga=72.4)

print(aeroporto)

aeroporto.adicionarPista(pista)
aeroporto.adicionarPlataforma(plataforma1)
plataforma1.ocupar(aviao)
print(aeroporto)

aeroporto.adicionarPlataforma(plataforma2)

print(aeroporto)

print("Plataforma disponivel: ", "nenhuma" if aeroporto.buscarPlataformaDisponivel() == None else f"\n{aeroporto.buscarPlataformaDisponivel().__str__()}")

aeroporto.removerPlataforma(plataforma1)

print(aeroporto)

aeroporto.removerPista(pista)

print(aeroporto)

print("Pista disponivel: ", "nenhuma" if aeroporto.buscarPistaDisponivel() == None else f"\n{aeroporto.buscarPistaDisponivel().__str__()}")