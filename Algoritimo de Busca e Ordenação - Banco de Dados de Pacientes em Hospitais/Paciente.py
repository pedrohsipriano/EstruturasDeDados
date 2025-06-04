import datetime


class Paciente:

    # Construtor da classe Paciente
    def __init__(self, nome_completo, prioridade_medica, id_paciente, data_admissao=None, id_medico_atribuido=None):
        self.id_paciente = id_paciente  # Identificador único do paciente
        self.nome_completo = nome_completo  # Nome completo do paciente

        # Valida se a prioridade está entre 1 e 5
        if not 1 <= prioridade_medica <= 5:
            raise ValueError("Prioridade médica deve estar entre 1 e 5.")
        self.prioridade_medica = prioridade_medica  # Nível de prioridade (1 a 5)

        # Se não informada, define a data de admissão como data/hora atual
        self.data_admissao = data_admissao if data_admissao else datetime.datetime.now()

        self.id_medico_atribuido = id_medico_atribuido  # ID do médico atribuído (opcional)

    # Atribui um médico ao paciente
    def atribuir_medico(self, id_medico):
        self.id_medico_atribuido = id_medico

    # Retorna uma string legível com os dados do paciente
    def __str__(self):
        medico_info = f"ID Médico: {self.id_medico_atribuido}" if self.id_medico_atribuido else "Médico: N/A"
        return (f"Paciente: {self.nome_completo}, ID: {self.id_paciente}, Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y %H:%M:%S')}, {medico_info}")

    # Representação oficial do objeto (útil para debug)
    def __repr__(self):
        return (f"Paciente(ID: {self.id_paciente}, Nome: {self.nome_completo}, "
                f"Prioridade: {self.prioridade_medica}, "
                f"Admissão: {self.data_admissao.strftime('%Y-%m-%d %H:%M')})")
