# MEDICOS
def ordenar_medicos(lista_medicos, criterio="nome"):
    # Ordena a lista de Médicos usando Insertion Sort.
    n = len(lista_medicos)
    for i in range(1, n):
        medico_atual = lista_medicos[i]
        j = i - 1

        deve_trocar = False
        if j >= 0:  # Garante que lista_medicos[j] é válido
            if criterio == "nome":
                if medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower():
                    deve_trocar = True
            elif criterio == "especialidade":
                if medico_atual.especialidade.lower() < lista_medicos[j].especialidade.lower():
                    deve_trocar = True
                elif medico_atual.especialidade.lower() == lista_medicos[j].especialidade.lower() and \
                        medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower():
                    deve_trocar = True
            else:
                if medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower():
                    deve_trocar = True

        while j >= 0 and deve_trocar:
            lista_medicos[j + 1] = lista_medicos[j]
            j -= 1
            if j >= 0:
                if criterio == "nome":
                    deve_trocar = medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower()
                elif criterio == "especialidade":
                    deve_trocar = (medico_atual.especialidade.lower() < lista_medicos[j].especialidade.lower() or
                                   (medico_atual.especialidade.lower() == lista_medicos[j].especialidade.lower() and
                                    medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower()))
                else:
                    deve_trocar = medico_atual.nome_completo.lower() < lista_medicos[j].nome_completo.lower()
            else:
                deve_trocar = False
        lista_medicos[j + 1] = medico_atual


def buscar_medico_por_id(lista_medicos, id_alvo):
    # Busca linear por um médico com o ID especificado
    for medico in lista_medicos:
        if medico.id_medico == id_alvo:
            return medico
    return None


def buscar_medicos_por_nome(lista_medicos, nome_parcial):
    # Busca linear por médicos cujo nome contenha nome_parcial
    resultados = []
    nome_parcial_lower = nome_parcial.lower()
    for medico in lista_medicos:
        if nome_parcial_lower in medico.nome_completo.lower():
            resultados.append(medico)
    return resultados


def buscar_medicos_por_especialidade(lista_medicos, especialidade_alvo):
    # Busca linear por médicos com a especialidade especificada
    resultados = []
    especialidade_alvo_lower = especialidade_alvo.lower()
    for medico in lista_medicos:
        if medico.especialidade.lower() == especialidade_alvo_lower:
            resultados.append(medico)
    return resultados


def buscar_pacientes_do_medico(lista_pacientes, id_medico_alvo):
    # Busca linear por pacientes atribuídos ao médico com o ID especificado. Deve conter o id em paciente
    resultados = []
    for paciente in lista_pacientes:
        if paciente.id_medico_atribuido == id_medico_alvo:
            resultados.append(paciente)
    return resultados
