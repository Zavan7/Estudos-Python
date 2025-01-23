import contas
import pessoas


class Banco:
    def __init__ (
        self,
        agencias: list[int] | None =  None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []