import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Models.PlanoVoo import PlanoVoo

plano = PlanoVoo("Passo Fundo|RS", "Curitiba|PR", "13:30", "17:00", 7000)
print(plano)
print(f"O plano de voo é valido: {"Sim" if plano.validarPlano() == True else "Não"}\n")