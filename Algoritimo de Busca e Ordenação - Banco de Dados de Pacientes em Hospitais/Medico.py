class Medico:

    # Construtor da classe Medico
    def __init__(self, nome_completo, especialidade, id_medico):
        self.id_medico: str = id_medico  # Identificador único do médico
        self.nome_completo: str = nome_completo  # Nome completo do médico
        self.especialidade: str = especialidade  # Especialidade médica

    # Retorna uma string legível com os dados do médico
    def __str__(self):
        return (f"Médico: {self.nome_completo}, ID: {self.id_medico}, Especialidade: {self.especialidade}")

    # Representação oficial do objeto (útil para debug)
    def __repr__(self):
        return (f"Medico(ID: {self.id_medico}, Nome: {self.nome_completo}, "
                f"Especialidade: {self.especialidade})")
