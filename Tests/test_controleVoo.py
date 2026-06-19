import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.Factory.FactoryAvioes import FactoryAviao
from Models.ControleVoo import ControleVoo
from Models.PlanoVoo import PlanoVoo

carga = FactoryAviao.criarAviao(tipo="Transporte", identificador="BTR1123", modelo="KC-390 Millennium", tipoCarga="Eletrodomesticos", pesoCarga=72.4)
controle = ControleVoo()
controle2 = ControleVoo()
plano = PlanoVoo("Passo Fundo|RS", "Curitiba|PR", "13:30", "17:00", 7000)

carga.adicionarObserver(controle)
carga.definirPlano(plano)
print(carga)

carga.solicitarDecolagem()
carga.decolar()

print(carga)

print("As instâncias são identicas? ","Sim" if controle.__eq__(controle2) else "Não")

