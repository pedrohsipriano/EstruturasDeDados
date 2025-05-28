import datetime

def ordenar_pacientes(lista_pacientes):
    for i in range(1, len(lista_pacientes)):
        paciente_atual = lista_pacientes[i]
        j = i - 1

        while j >= 0 and \
              (paciente_atual.prioridade_medica < lista_pacientes[j].prioridade_medica or \
               (paciente_atual.prioridade_medica == lista_pacientes[j].prioridade_medica and \
                paciente_atual.data_admissao < lista_pacientes[j].data_admissao)):
            lista_pacientes[j + 1] = lista_pacientes[j]
            j -= 1
        lista_pacientes[j + 1] = paciente_atual

def selecionar_proximo(lista_aguardando, contadores_atendimento):
    if not lista_aguardando:
        return None

    if lista_aguardando[0].prioridade_medica == 1:
        return lista_aguardando.pop(0)

    idx_proximo_nivel_2 = -1
    idx_proximo_nivel_3 = -1
    idx_proximo_nivel_4 = -1

    for i, p in enumerate(lista_aguardando):
        if p.prioridade_medica == 2 and idx_proximo_nivel_2 == -1:
            idx_proximo_nivel_2 = i
        elif p.prioridade_medica == 3 and idx_proximo_nivel_3 == -1:
            idx_proximo_nivel_3 = i
        elif p.prioridade_medica == 4 and idx_proximo_nivel_4 == -1:
            idx_proximo_nivel_4 = i

        if idx_proximo_nivel_2 != -1 and idx_proximo_nivel_3 != -1 and idx_proximo_nivel_4 != -1:
            break

    if contadores_atendimento.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0) >= 2:
        paciente_selecionado = None
        if idx_proximo_nivel_3 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_3)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0
            return paciente_selecionado
        elif idx_proximo_nivel_4 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_4)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0
            return paciente_selecionado
        elif idx_proximo_nivel_2 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_2)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] += 1
            return paciente_selecionado
    else:
        if idx_proximo_nivel_2 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_2)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = \
                contadores_atendimento.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0) + 1
            return paciente_selecionado
        elif idx_proximo_nivel_3 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_3)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0
            return paciente_selecionado
        elif idx_proximo_nivel_4 != -1:
            paciente_selecionado = lista_aguardando.pop(idx_proximo_nivel_4)
            contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0
            return paciente_selecionado

    if lista_aguardando:
        return lista_aguardando.pop(0)

    return None

def buscar_pacientes_binaria(lista_pacientes, prioridade_alvo, data_admissao_alvo=None):

    resultados = []
    esquerda = 0
    direita = len(lista_pacientes) - 1
    primeiro_encontrado_idx = -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        paciente_meio = lista_pacientes[meio]

        if paciente_meio.prioridade_medica < prioridade_alvo:
            esquerda = meio + 1
        elif paciente_meio.prioridade_medica > prioridade_alvo:
            direita = meio - 1
        else:
            if data_admissao_alvo is not None:
                if paciente_meio.data_admissao < data_admissao_alvo:
                    esquerda = meio + 1
                elif paciente_meio.data_admissao > data_admissao_alvo:
                    direita = meio - 1
                else:
                    primeiro_encontrado_idx = meio
                    direita = meio - 1
            else:
                primeiro_encontrado_idx = meio
                direita = meio - 1

    if primeiro_encontrado_idx != -1:
        idx = primeiro_encontrado_idx
        temp_resultados_esquerda = []
        while idx >= 0 and \
              lista_pacientes[idx].prioridade_medica == prioridade_alvo and \
              (data_admissao_alvo is None or lista_pacientes[idx].data_admissao == data_admissao_alvo):
            temp_resultados_esquerda.append(lista_pacientes[idx])
            idx -= 1
        resultados.extend(reversed(temp_resultados_esquerda))

        idx = primeiro_encontrado_idx + 1
        while idx < len(lista_pacientes) and \
              lista_pacientes[idx].prioridade_medica == prioridade_alvo and \
              (data_admissao_alvo is None or lista_pacientes[idx].data_admissao == data_admissao_alvo):
            resultados.append(lista_pacientes[idx])
            idx += 1
    return resultados
