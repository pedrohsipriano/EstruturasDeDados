
class Medico:

    def __init__(self, nome_completo, especialidade, id_medico): # Sem type hints na assinatura
        self.id_medico: str = id_medico
        self.nome_completo: str = nome_completo
        self.especialidade: str = especialidade

    # Visualização Médico
    def __str__(self):
        return (f"Médico: {self.nome_completo}, ID: {self.id_medico}, Especialidade: {self.especialidade}")

    def __repr__(self):
        return (f"Medico(ID: {self.id_medico}, Nome: {self.nome_completo}, "
                f"Especialidade: {self.especialidade})")