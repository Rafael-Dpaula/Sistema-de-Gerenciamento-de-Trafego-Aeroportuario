import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.CentroOperacional import CentroOperacional
from Models.ControleVoo import ControleVoo
from Models.Aeroporto import Aeroporto
from Models.Factory.FactoryAvioes import FactoryAviao
from Models.PlanoVoo import PlanoVoo
from Models.Pista import Pista
from Models.Plataforma import Plataforma

obs = ControleVoo()
carga = FactoryAviao.criarAviao(tipo="Transporte", identificador="BTR1123", modelo="KC-390 Millennium", tipoCarga="Eletrodomesticos", pesoCarga=72.4)
carga.adicionarObserver(obs)

aeroporto = Aeroporto("Aeroporto Internacional", "AERP12", "Passo Fundo | RS")
pista = Pista(0)
aeroporto.adicionarPista(pista)
plataforma = Plataforma(0)
plataforma.ocupar(carga)
aeroporto.adicionarPlataforma(plataforma)

controle = ControleVoo()
plano = PlanoVoo("Passo Fundo|RS", "Curitiba|PR", "13:00", "17:30", 7000)
centro = CentroOperacional(aeroporto, controle)

# print(centro)
controle.adicionarAeronave(carga)
carga.definirPlano(plano)

# aviao solicita -> controle solicita -> centro autoriza ->
carga.solicitarDecolagem()
# print(type(carga._status).__name__)
controle.solicitarDecolagem(carga)
# print(type(carga._status).__name__)
centro.autorizarDecolagem(carga)
# print(type(carga._status).__name__)
centro.processarDecolagem(carga)
print(carga)
# print(centro)

# carga.solicitarPouso()
# controle
