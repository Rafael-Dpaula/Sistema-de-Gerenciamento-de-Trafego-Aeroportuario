import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Models.Avioes.Aviao import Aviao
from Models.Factory.FactoryAvioes import FactoryAviao  # criar avioes
from Models.CentroOperacional import CentroOperacional  # classe central
from Models.Pista import Pista  # pistas de pouso e decolagem
from Models.Plataforma import Plataforma  # plataformas(garagens) dos avioes
from Models.PlanoVoo import PlanoVoo  # plano do onde o aviao vai, quando vai, etc
from Models.Aeroporto import Aeroporto  # classe da estrutura fisica do aeroporto
from Models.ControleVoo import (
    ControleVoo,
)  # classe que faz a comunicação entre aviao e o centro de operacao(observer)

aviaoSelecionado = None
aeroportoSelecionado = None
centroSelecionado = None
centros: list[(str, CentroOperacional)] = []
aeroportos: list[Aeroporto._nome, Aeroporto] = []
controles: list[(str, ControleVoo)] = []
avioes: list[(Aviao._identificador, Aviao)] = []
planos: list[(PlanoVoo._destino, PlanoVoo)] = []

# INSTÂNCIAS ESTÁTICAS
# obs = ControleVoo()
# carga = FactoryAviao.criarAviao(
#     tipo="Transporte",
#     identificador="BTR1123",
#     modelo="KC-390 Millennium",
#     tipoCarga="Eletrodomesticos",
#     pesoCarga=72.4,
# )

# aeroporto = Aeroporto("Aeroporto Internacional", "AERP12", "Passo Fundo | RS")
# pista = Pista(0)
# aeroporto.adicionarPista(pista)
# plataforma = Plataforma(0)
# plataforma.ocupar(carga)
# aeroporto.adicionarPlataforma(plataforma)

# controle = ControleVoo()
# plano = PlanoVoo("Passo Fundo|RS", "Curitiba|PR", "13:00", "17:30", 7000)
# centro = CentroOperacional(aeroporto, controle)
# controle.adicionarAeronave(carga)

# aeroportos.append((aeroporto._nome, aeroporto))
# controles.append(("Controle Principal", obs))
# centros.append(("Centro", centro))
# avioes.append((carga._identificador, carga))
# planos.append((plano._destino, plano))


def menuLista(lista, titulo="LISTA"):
    print(f"===== MENU {titulo.upper()} =====")
    if len(lista) == 0:
        print("ALERT: lista vazia.")
        return None
    primeiro = lista[0]  # detecta se é uma lista pura de obj ou uma lista de tuplas
    if isinstance(primeiro, tuple):
        for i, (rotulo, _) in enumerate(lista, start=1):
            print(f"[{i}] {rotulo}")
    elif isinstance(primeiro, Aviao):
        for i, item in enumerate(lista, start=1):
            print(f"[{i}] {item._identificador}")
    else:
        for i, item in enumerate(lista, start=1):
            print(f"[{i}] {item}")
    print("[0] Voltar")
    mn = input("---> ")
    if not mn.isdigit():
        return menuLista(lista, titulo)
    mn = int(mn)
    if mn == 0:
        return None
    if mn < 1 or mn > len(lista):
        return menuLista(lista, titulo)
    if isinstance(lista[mn - 1], tuple):
        return lista[mn - 1][1]
    return lista[mn - 1]


def menu():
    print("====== MENU ======")
    print(
        f"Avião Selecionado: {"Não selecionado" if aviaoSelecionado is None else f"{aviaoSelecionado._modelo} | {aviaoSelecionado._identificador} | {type(aviaoSelecionado).__name__} | {type(aviaoSelecionado._status).__name__}"}"
    )
    print(
        f"Aeroporto Selecionado: {"Não selecionado" if aeroportoSelecionado is None else f"{aeroportoSelecionado.nome} | {aeroportoSelecionado.codigo} | {aeroportoSelecionado.cidade}"}"
    )
    print("[1] Menu Mostrar")
    print("[2] Menu de Criação")
    print("[3] Menu de Manipulação")
    print("[0] Sair")
    mn = input("---> ")
    if mn.isdigit():
        mn = int(mn)
    if mn == 0:
        return
    elif mn == 1:
        menuMostrar()
    elif mn == 2:
        menuCriacao()
    elif mn == 3:
        menuManipulacao()
    else:
        print("ALERT: entrada inválida.")
        menu()


def menuMostrar():
    print("======= MENU MOSTRAR ======")
    print(
        f"Avião Selecionado: {"Não selecionado" if aviaoSelecionado is None else f"{aviaoSelecionado._modelo} | {aviaoSelecionado._identificador} | {type(aviaoSelecionado).__name__} | {type(aviaoSelecionado._status).__name__}"}"
    )
    print(
        f"Aeroporto Selecionado: {"Não selecionado" if aeroportoSelecionado is None else f"{aeroportoSelecionado.nome} | {aeroportoSelecionado.codigo} | {aeroportoSelecionado.cidade}"}"
    )
    print("[1] Mostrar Aeroporto")
    print("[2] Mostrar Aviao Selecionado")
    print("[3] Mostrar Controle de Voo")
    print("[4] Mostrar Centro de Operações")
    print("[5] Mostrar Pistas")
    print("[6] Mostrar Plataformas")
    print("[7] Mostrar Histórico de Comunicação")
    print("[0] Voltar")
    mn = input("---> ")
    if mn.isdigit():
        mn = int(mn)
    if mn == 0:
        return menu()
    elif mn == 1:
        if aeroportoSelecionado is not None:
            print(aeroportoSelecionado.__str__())
            return menuMostrar()
        else:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
    elif mn == 2:
        if aviaoSelecionado is not None:
            print(aviaoSelecionado.__str__())
        else:
            print("Nenhum avião selecionado.")
            return menuMostrar()
    elif mn == 3:
        if centroSelecionado is not None:
            print(centroSelecionado._controleVoo.__str__())
        else:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
    elif mn == 4:
        if centroSelecionado is not None:
            print(centroSelecionado.__str__())
        else:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
    elif mn == 5:
        if aeroportoSelecionado is None:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
        if len(aeroportoSelecionado._pistas) > 0:
            for pista in aeroportoSelecionado._pistas:
                print(pista.__str__())
        else:
            print("Nenhuma pista cadastrada.")
            return menuMostrar()
    elif mn == 6:
        if aeroportoSelecionado is None:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
        if len(aeroportoSelecionado._plataformas) > 0:
            for plataforma in aeroportoSelecionado._plataformas:
                print(plataforma.__str__())
        else:
            print("Nenhuma plataforma cadastrada.")
            return menuMostrar()
    elif mn == 7:
        if aeroportoSelecionado is None:
            print("Nenhum aeroporto selecionado.")
            return menuMostrar()
        if len(centroSelecionado._controleVoo._historicoContato) > 0:
            for call in centroSelecionado._controleVoo._historicoContato:
                print(call)
        else:
            print("Nenhuma comunicação registrada.")
            return menuMostrar()

    else:
        print("ALERT: entrada inválida.")
        return menuMostrar()
    return menu()


def menuManipulacao():
    global aeroportoSelecionado, centroSelecionado, aviaoSelecionado, planos, avioes
    centroSelecionado = next(
        (obj for rotulo, obj in centros if obj._aeroporto == aeroportoSelecionado), None
    )
    print("===== MENU DE MANIPULAÇÃO =====")
    print(
        f"Avião Selecionado: {"Não selecionado" if aviaoSelecionado is None else f"{aviaoSelecionado._modelo} | {aviaoSelecionado._identificador} | {type(aviaoSelecionado).__name__} | {type(aviaoSelecionado._status).__name__}"}"
    )
    print(
        f"Aeroporto Selecionado: {"Não selecionado" if aeroportoSelecionado is None else f"{aeroportoSelecionado.nome} | {aeroportoSelecionado.codigo} | {aeroportoSelecionado.cidade}"}"
    )
    if aeroportoSelecionado is not None and len(
        aeroportoSelecionado._plataformas
    ) >= len(aeroportoSelecionado._pistas):
        print(
            f"AVISO: a quantidade de pistas e plataformas podem gerar conflitos. recomenda-se pelo menos {len(aeroportoSelecionado._plataformas)+1} pistas para evitar problemas de tráfego."
        )
    print("[1] Selecionar Aeroporto")
    print("[2] Adicionar Avião ao Aeroporto")
    print("[3] Remover Avião do Aeroporto")
    print("[4] Selecionar Avião")
    print("[5] Definir Plano de Voo")
    print("[6] Mudar Estado do Aviao")
    print("[7] Adicionar Observador")
    print("[8] Remover Observador")
    print("[0] Voltar")
    mn = input("---> ")
    if mn.isdigit():
        mn = int(mn)
    if mn == 0:
        return menu()
    elif mn == 1:
        resultado = menuLista(aeroportos, "aeroportos")
        if resultado is not None:
            aeroportoSelecionado = resultado
        return menuManipulacao()
    elif mn == 2:
        if centroSelecionado is None or aeroportoSelecionado is None:
            print("ALERT: selecione aeroporto válido.")
            return menuManipulacao()
        vaga = aeroportoSelecionado.buscarPlataformaDisponivel()
        if vaga is None:
            print(
                "ALERT: capacidade máxima do aeroporto atingida. "
                "adicione mais plataformas para comportar mais aeronaves."
            )
            return menuManipulacao()
        aviao = menuLista(avioes, "aeronaves")
        if aviao is None:
            return menuManipulacao()
        centroSelecionado._controleVoo.adicionarAeronave(aviao)
        vaga.ocupar(aviao)
        return menuManipulacao()
    elif mn == 3:
        if centroSelecionado is None:
            print("ALERT: primeiro selecione um aeroporto.")
            return menuManipulacao()
        aviao = menuLista(avioes, "aeronaves")
        if aviao is None:
            return menuManipulacao()
        platUtilizada = None
        for plat in aeroportoSelecionado._plataformas:
            if plat._aviao is aviao:
                platUtilizada = plat
                break
        platUtilizada.liberar()
        centroSelecionado._controleVoo.removerAeronave(aviao)
        return menuManipulacao()
    elif mn == 4:
        if centroSelecionado is None:
            print("ALERT: primeiro selecione um aeroporto.")
            return menuManipulacao()
        aviao = menuLista(centroSelecionado._controleVoo.aeronaves, "aviões")
        if aviao is not None:
            aviaoSelecionado = aviao
        return menuManipulacao()
    elif mn == 5:
        if aviaoSelecionado is None:
            print("ALERT: primeiro selecione um avião.")
            return menuManipulacao()
        plano = menuLista(planos, "planos de voo")
        if plano is None:
            return menuManipulacao()
        aviaoSelecionado.definirPlano(plano)
        return menuManipulacao()
    elif mn == 6:
        if aviaoSelecionado is None:
            print("ALERT: primeiro selecione um avião.")
            return menuManipulacao()
        menuEstados()
        return menuManipulacao
    elif mn == 7:
        if aviaoSelecionado is None:
            print("ALERT: primeiro selecione um avião.")
            return menuManipulacao()
        aviaoSelecionado.adicionarObserver(menuLista(controles, "observadores"))
        return menuManipulacao()
    elif mn == 8:
        if aviaoSelecionado is None:
            print("ALERT: primeiro selecione um avião.")
            return menuManipulacao()
        aviaoSelecionado.removerObserver(menuLista(controles, "observadores"))
        return menuManipulacao()
    else:
        print("ALERT: entrada inválida.")
        return menuManipulacao()


def menuEstados():
    print("===== SELECIONE A SOLICITAÇÃO ======")
    print(
        f"Avião Selecionado: {"Não selecionado" if aviaoSelecionado is None else f"{aviaoSelecionado._modelo} | {aviaoSelecionado._identificador} | {type(aviaoSelecionado).__name__} | {type(aviaoSelecionado._status).__name__}"}"
    )
    print("[1] Solicitar Decolagem")
    print("[2] Informar Decolagem")
    print("[3] Solicitar Pouso")
    print("[4] Informar Pouso")
    print("[5] Declarar Emergência")
    print("[0] Voltar")
    mn = input("---> ")
    if mn.isdigit():
        mn = int(mn)
    if mn == 0:
        return menuManipulacao()
    elif mn == 1:
        aviaoSelecionado.solicitarDecolagem()
        centroSelecionado._controleVoo.solicitarDecolagem(aviaoSelecionado)
        centroSelecionado.autorizarDecolagem(aviaoSelecionado)
        return menuEstados()
    elif mn == 2:
        centroSelecionado.processarDecolagem(aviaoSelecionado)
        return menuEstados()
    elif mn == 3:
        aviaoSelecionado.solicitarPouso()
        centroSelecionado._controleVoo.solicitarPouso(aviaoSelecionado)
        centroSelecionado.autorizarPouso(aviaoSelecionado)
        return menuEstados()
    elif mn == 4:
        centroSelecionado.processarPouso(aviaoSelecionado)
        return menuEstados()
    elif mn == 5:
        centroSelecionado.processarEmergencia(aviaoSelecionado)
        return menuEstados()
    else:
        print("ALERT: entrada inválida.")
        return menuEstados()


def menuCriacao():
    print("===== MENU CRIAÇÃO =====")
    print("[1] Criar Aeroporto")
    print("[2] Criar Controle de Voo")
    print("[3] Criar Centro de Operações")
    print("[4] Criar Pista")
    print("[5] Criar Plataforma")
    print("[6] Criar Plano de Voo")
    print("[7] Criar Aviao")
    print("[8] Remover Pista")
    print("[9] Remover Plataforma")
    print("[0] Voltar")
    mn = input("---> ")
    if mn.isdigit():
        mn = int(mn)
    if mn == 0:
        return menu()
    elif mn == 1:
        nome = input("[INFO] NOME: ")
        codigo = input("[INFO] CODIGO: ")
        cidade = input("[INFO] CIDADE: ")
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            aeroportos.append((nome, Aeroporto(nome, codigo, cidade)))
        return menuCriacao()
    elif mn == 2:
        nome = input("[INFO] NOME: ")
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            controles.append((nome, ControleVoo()))
        return menuCriacao()
    elif mn == 3:
        nome = input("[INFO] NOME: ")
        print("[INFO] SELECIONE O AEROPORTO: ")
        aeroporto = menuLista(aeroportos, "aeroportos")
        if aeroporto is None:
            return menuCriacao()
        print("[INFO] SELECIONE O CONTROLE DE VOO: ")
        controle = menuLista(controles, "controles de voo")
        if controle is None:
            return menuCriacao()
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            centros.append((nome, CentroOperacional(aeroporto, controle)))
        return menuCriacao()
    elif mn == 4:
        print("[INFO] SELECIONE O AEROPORTO: ")
        aeroporto = menuLista(aeroportos, "aeroportos")
        if aeroporto is None:
            return menuCriacao()
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            aeroporto.adicionarPista(Pista(len(aeroporto._pistas)))
        return menuCriacao()
    elif mn == 5:
        print("[INFO] SELECIONE O AEROPORTO: ")
        aeroporto = menuLista(aeroportos, "aeroportos")
        if aeroporto is None:
            return menuCriacao()
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            aeroporto.adicionarPlataforma(Plataforma(len(aeroporto._plataformas)))
        return menuCriacao()
    elif mn == 6:
        origem = input("[INFO] ORIGEM: ")
        destino = input("[INFO] DESTINO: ")
        horarioPartida = input("[INFO] HORÁRIO DA PARTIDA(MM:HH): ")
        horarioChegada = input("[INFO] HORÁRIO DA CHEGADA(MM:HH): ")
        altitude = int(input("[INFO] ALTITUDE DE CRUZEIRO: "))
        criar = input("[CRIAR] S/N: ")
        if criar.lower() == "s":
            planos.append(
                (
                    destino,
                    PlanoVoo(origem, destino, horarioPartida, horarioChegada, altitude),
                )
            )
        return menuCriacao()
    elif mn == 7:
        tipo = input("[INFO] TIPO DO AVIAO(COMERCIAL, PRIVADO, TRANSPORTE): ")
        identificador = input("[INFO] IDENTIFICADOR: ")
        modelo = input("[INFO] MODELO: ")
        if tipo.upper() == "COMERCIAL":
            companhia = input("[INFO] COMPANHIA AÉREA: ")
            nroPassageiro = int(input("[INFO] NÚMERO DE PASSAGEIROS: "))
            criar = input("[CRIAR] S/N: ")
            if criar.lower() == "s":
                avioes.append(
                    (
                        identificador,
                        FactoryAviao.criarAviao(
                            tipo,
                            identificador=identificador,
                            modelo=modelo,
                            companhiaAerea=companhia,
                            numeroPassageiros=nroPassageiro,
                        ),
                    )
                )
            return menuCriacao()
        if tipo.upper() == "PRIVADO":
            proprietario = input("[INFO] PROPRIETÁRIO: ")
            nroPassageiro = int(input("[INFO] NÚMERO DE PASSAGEIROS: "))
            criar = input("[CRIAR] S/N: ")
            if criar.lower() == "s":
                avioes.append(
                    (
                        identificador,
                        FactoryAviao.criarAviao(
                            tipo,
                            identificador=identificador,
                            modelo=modelo,
                            proprietario=proprietario,
                            numeroPassageiros=nroPassageiro,
                        ),
                    )
                )
            return menuCriacao()
        if tipo.upper() == "TRANSPORTE":
            tipoCarga = input("[INFO] TIPO DA CARGA: ")
            pesoCarga = float(input("[INFO] PESO DA CARGA: "))
            criar = input("[CRIAR] S/N: ")
            if criar.lower() == "s":
                avioes.append(
                    (
                        identificador,
                        FactoryAviao.criarAviao(
                            tipo,
                            identificador=identificador,
                            modelo=modelo,
                            tipoCarga=tipoCarga,
                            pesoCarga=pesoCarga,
                        ),
                    )
                )
        return menuCriacao()
    elif mn == 8:
        print("[INFO] SELECIONE O AEROPORTO: ")
        aeroporto = menuLista(aeroportos, "aeroportos")
        if aeroporto is None:
            return menuCriacao()
        pista = menuLista(aeroporto._pistas, "pistas")
        if pista is None:
            return menuCriacao()
        remover = input("[REMOVER] S/N: ")
        if remover.lower() == "s":
            aeroporto.removerPista(pista)
        return menuCriacao()
    elif mn == 9:
        print("[INFO] SELECIONE O AEROPORTO: ")
        aeroporto = menuLista(aeroportos, "aeroportos")
        if aeroporto is None:
            return menuCriacao()
        plataforma = menuLista(aeroporto._plataformas, "plataformas")
        if plataforma is None:
            return menuCriacao()
        remover = input("[REMOVER] S/N: ")
        if remover.lower() == "s":
            aeroporto.removerPlataforma(plataforma)
        return menuCriacao()
    else:
        print("ALERT: entrada inválida.")
        return menuCriacao()


def main():
    print("Carregando sistema de gerenciamento de tráfego aeroportuário...")
    menu()
    print("Encerrando sistema de gerenciamento de tráfego aeroportuário...")


main()
