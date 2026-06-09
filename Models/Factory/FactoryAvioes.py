from Models.Avioes.Comercial import Comercial
from Models.Avioes.Privado import Privado
from Models.Avioes.Transporte import Transporte
class FactoryAviao:
    @staticmethod
    def criarAviao(tipo: str, **kwargs):
        tipo = tipo.strip().lower()
        if tipo == "comercial":
            obrigatorios = [
                "identificador",
                "modelo",
                "companhiaAerea",
                "numeroPassageiros"
            ]
            for campo in obrigatorios:
                if campo not in kwargs:
                    raise ValueError(f"ERROR: campo obrigatório ausente: {campo}.")
            return Comercial(**kwargs)
        
        if tipo == "privado":
            obrigatorios = [
                "identificador",
                "modelo",
                "proprietario",
                "numeroPassageiros"
            ]
            for campo in obrigatorios:
                if campo not in kwargs:
                    raise ValueError(f"ERROR: campo obrigatório ausente: {campo}.")
            return Privado(**kwargs)
        
        if tipo == "transporte":
            obrigatorios = [
                "identificador",
                "modelo",
                "tipoCarga",
                "pesoCarga"
            ]
            for campo in obrigatorios:
                if campo not in kwargs:
                    raise ValueError(f"ERROR: campo obrigatório ausente: {campo}.")
            return Transporte(**kwargs)
        
        raise ValueError("ERROR: tipo de aeronave inválida.")
