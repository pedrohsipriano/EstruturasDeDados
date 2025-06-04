# Função para ordenar lista de médicos usando Insertion Sort
def ordenar_medicos(lista_medicos, criterio="nome"):
    n = len(lista_medicos)
    for i in range(1, n):
        medico_atual = lista_medicos[i]
        j = i - 1

        deve_trocar = False

        # Verifica se precisa trocar com base no critério escolhido
        if j >= 0:
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

        # Desloca os elementos enquanto a ordem não está correta
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


# Busca linear de médico pelo ID
def buscar_medico_por_id(lista_medicos, id_alvo):
    for medico in lista_medicos:
        if medico.id_medico == id_alvo:
            return medico
    return None


# Busca linear de médicos pelo nome (parcial)
def buscar_medicos_por_nome(lista_medicos, nome_parcial):
    resultados = []
    nome_parcial_lower = nome_parcial.lower()
    for medico in lista_medicos:
        if nome_parcial_lower in medico.nome_completo.lower():
            resultados.append(medico)
    return resultados


# Busca linear de médicos pela especialidade
def buscar_medicos_por_especialidade(lista_medicos, especialidade_alvo):
    resultados = []
    especialidade_alvo_lower = especialidade_alvo.lower()
    for medico in lista_medicos:
        if medico.especialidade.lower() == especialidade_alvo_lower:
            resultados.append(medico)
    return resultados


# Busca linear de pacientes atribuídos a um médico específico
def buscar_pacientes_do_medico(lista_pacientes, id_medico_alvo):
    resultados = []
    for paciente in lista_pacientes:
        if paciente.id_medico_atribuido == id_medico_alvo:
            resultados.append(paciente)
    return resultados
