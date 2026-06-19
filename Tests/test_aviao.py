import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.Factory.FactoryAvioes import FactoryAviao
from Models.Observer.Observer import Observer
from Models.PlanoVoo import PlanoVoo

class DubleObserver(Observer): #classe que simula um observer (necessário para teste unico do Aviao, já que a classe herdada de observer é ControleVoo)
    def __init__(self, rotulo):
        self._chamadas = []  # registro do historico de mensagens
        self._rotulo = rotulo    
    def atualizar(self, origem, mensagem):
        self._chamadas.append((origem, mensagem))
    

privado = FactoryAviao.criarAviao(tipo="Privado", identificador="ACE202", modelo="SkyViper", proprietario="bill gates", numeroPassageiros=12)
carga = FactoryAviao.criarAviao(tipo="Transporte", identificador="BTR1123", modelo="KC-390 Millennium", tipoCarga="Eletrodomesticos", pesoCarga=72.4)
comercial = FactoryAviao.criarAviao(tipo="Comercial", identificador="AZUL2017", modelo="Boeing 747", companhiaAerea="Azul Viagens", numeroPassageiros=300)

plano1 = PlanoVoo("Passo Fundo|RS", "Curitiba|PR", "13:00", "17:30", 7000)
plano2 = PlanoVoo("Porto Alegre|RS", "Rio de Janeiro|RJ", "9:00", "19:30", 7900)
plano3 = PlanoVoo("Joinville|SC", "Goiania|GO", "5:00", "13:30", 6800)

obs1 = DubleObserver("obs1")
obs2 = DubleObserver("obs2")
obs3 = DubleObserver("obs3")

privado.adicionarObserver(obs1)
carga.adicionarObserver(obs2)
comercial.adicionarObserver(obs3)

carga.definirPlano(plano3)

print(privado)
print(carga)
print(comercial)

privado.solicitarPouso()
privado.solicitarDecolagem()
privado.definirPlano(plano1)
privado.solicitarDecolagem()

print(privado)

privado.decolar()
print(privado)

privado.solicitarPouso()
print(privado)

privado.pousar()
print(privado)
privado.pousar()
print(privado)

comercial.definirPlano(plano2)
comercial.solicitarDecolagem()
comercial.decolar()
print(comercial)

comercial.declararEmergencia()
print(comercial)

comercial.solicitarPouso()
print(comercial)

comercial.pousar()
print(comercial)


