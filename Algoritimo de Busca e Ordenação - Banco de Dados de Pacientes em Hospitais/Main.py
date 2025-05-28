import datetime
from Paciente import Paciente
from Medico import Medico

# PACIENTES
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

# MEDICOS
def ordenar_medicos(lista_medicos, criterio="nome"):
    # Ordena a lista de Médicos usando Insertion Sort.
    n = len(lista_medicos)
    for i in range(1, n):
        medico_atual = lista_medicos[i]
        j = i - 1

        deve_trocar = False
        if j >= 0: # Garante que lista_medicos[j] é válido
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

# EXECUÇÃO E SAÍDA
if __name__ == "__main__":
    paciente1 = Paciente("Carlos Silva", 2, 1, data_admissao=datetime.datetime(2023, 10, 20, 10, 0, 0))
    paciente2 = Paciente("Ana Pereira", 1, 2, data_admissao=datetime.datetime(2023, 10, 20, 10, 5, 0))
    paciente3 = Paciente("João Costa", 3, 3, data_admissao=datetime.datetime(2023, 10, 20, 9, 30, 0))
    paciente4 = Paciente("Maria Oliveira", 2, 4, data_admissao=datetime.datetime(2023, 10, 20, 10, 2, 0))
    paciente5 = Paciente("Lucas Martins", 4, 5, data_admissao=datetime.datetime(2023, 10, 20, 8, 0, 0))
    paciente6 = Paciente("Beatriz Almeida", 2, 6, data_admissao=datetime.datetime(2023, 10, 20, 10, 1, 0))
    paciente7 = Paciente("Mario Souza", 3, 7, data_admissao=datetime.datetime(2023, 10, 20, 9, 35, 0))
    paciente8 = Paciente("Fernanda Lima", 2, 8, data_admissao=datetime.datetime(2023, 10, 20, 10, 3, 0))
    paciente9 = Paciente("Roberto Dias", 5, 9, data_admissao=datetime.datetime(2023, 10, 20, 11, 0, 0))
    paciente10 = Paciente("Ana Silva", 1, 10, data_admissao=datetime.datetime(2023, 10, 20, 10, 4, 0))

    lista_de_pacientes = [
        paciente1, paciente2, paciente3, paciente4,
        paciente5, paciente6, paciente7, paciente8, paciente9, paciente10
    ]

    print("--- Lista Original de Pacientes (Desordenada) ---")
    for p in lista_de_pacientes:
        print(p)

    ordenar_pacientes(lista_de_pacientes)

    print("\n--- Lista de Pacientes Ordenada por Prioridade (Insertion Sort) ---\n")
    for p in lista_de_pacientes:
        print(p)
    print()
    
    # SAÍDA MEDICOS
    print("\n\n--- Cadastro e Demonstração de Médicos ---")
    medico1 = Medico("Dr. Gregory House","Diagnóstico","MED-001")
    medico2 = Medico( "Dra. Meredith Grey", "Cirurgia Geral","MED-002")
    medico3 = Medico("Dr. Derek Shepherd", "Neurocirurgia","MED-003")
    medico4 = Medico( "Dra. Cristina Yang", "Cardiologia","MED-004")
    medico5 = Medico( "Dr. James Wilson", "Oncologia","MED-005")

    lista_de_medicos = [medico1, medico2, medico3, medico4, medico5]
    print("Lista Original de Médicos:")
    for m in lista_de_medicos:
        print(m)

    ordenar_medicos(lista_de_medicos, "especialidade")
    print("\nLista de Médicos Ordenada por Especialidade (e Nome):")
    for m in lista_de_medicos:
        print(m)

    ordenar_medicos(lista_de_medicos, "nome")
    print("\nLista de Médicos Ordenada por Nome:")
    for m in lista_de_medicos:
        print(m)

    # Atribuir medico a paciente
    if hasattr(paciente1, 'atribuir_medico'): 
        paciente1.atribuir_medico(medico2.id_medico)
        paciente6.atribuir_medico(medico1.id_medico)
        paciente10.atribuir_medico(medico4.id_medico)
        paciente3.atribuir_medico(medico1.id_medico) 
    
    print("\n--- Pacientes com Médicos Atribuídos (após ordenação de pacientes) ---")
    for p in lista_de_pacientes:
        print(p) 

    # FILA DE ATENDIMENTO / SAIDA ORDENACAO
    print("\n\n--- Simulação da Fila de Atendimento () ---\n")
    lista_para_atendimento = list(lista_de_pacientes)

    print("Fila inicial para atendimento (já ordenada, com médicos):")
    for p in lista_para_atendimento:
        print(p)
    print("-" * 20)
    print()
    
    contadores_fila = {'atendidos_nivel2_desde_ultimo_nivel3_ou_4': 0}
    print("Ordem de atendimento simulada:")

    pacientes_atendidos_ordem = []
    while lista_para_atendimento:
        print("\nFila atual:")
        for p_fila in lista_para_atendimento:
            print(f"  {p_fila}")

        proximo_a_atender = selecionar_proximo(lista_para_atendimento, contadores_fila)

        if proximo_a_atender:
            pacientes_atendidos_ordem.append(proximo_a_atender)
            # Tenta buscar o nome do médico para exibição, se houver ID
            nome_medico_responsavel = "N/A"
            if proximo_a_atender.id_medico_atribuido:
                medico_obj = buscar_medico_por_id(lista_de_medicos, proximo_a_atender.id_medico_atribuido)
                if medico_obj:
                    nome_medico_responsavel = medico_obj.nome_completo
            
            print(
                f"--> ATENDENDO: {proximo_a_atender.nome_completo} (ID: {proximo_a_atender.id_paciente}, P: {proximo_a_atender.prioridade_medica}) "
                f"| Médico: {nome_medico_responsavel} "
                f"(Contador N2: {contadores_fila.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0)})")
        else:
            print("Fila de atendimento vazia.") 
            break

    print("\n--- Todos os pacientes foram atendidos ---\n")
    print("Ordem final de atendimento:\n")
    for i, p_atendido in enumerate(pacientes_atendidos_ordem):
        print(f"{i + 1}. {p_atendido.nome_completo} (Prioridade: {p_atendido.prioridade_medica})")


    # SAIDA BUSCA MEDICOS E PACIENTES
    print("\n\n--- Demonstração de Funções de Busca ---")
    
    print("\nBuscando Pacientes com Prioridade 1 (Busca Binária):")
    resultados_p1 = buscar_pacientes_binaria(lista_de_pacientes, 1)
    if resultados_p1:
        for p_res in resultados_p1:
            print(f"- {p_res.nome_completo} (Prioridade: {p_res.prioridade_medica}, Admissão: {p_res.data_admissao.strftime('%d/%m/%Y %H:%M')})")
    else:
        print("Nenhum paciente encontrado com Prioridade 1.")

    data_especifica_busca = datetime.datetime(2023, 10, 20, 9, 30, 0)
    print(f"\nBuscando Pacientes com Prioridade 3 e Admissão em {data_especifica_busca.strftime('%d/%m/%Y %H:%M:%S')}:")
    resultados_p3_data = buscar_pacientes_binaria(lista_de_pacientes, 3, data_especifica_busca)
    if resultados_p3_data:
        for p_res in resultados_p3_data:
            print(f"- {p_res.nome_completo} (Prioridade: {p_res.prioridade_medica}, Admissão: {p_res.data_admissao.strftime('%d/%m/%Y %H:%M')})")
    else:
        print("Nenhum paciente encontrado com estes critérios.")

    print(f"\nBuscando médico por ID ('{medico1.id_medico}'):")
    medico_encontrado = buscar_medico_por_id(lista_de_medicos, medico1.id_medico)
    if medico_encontrado:
        print(f"- Encontrado: {medico_encontrado}") 
    else:
        print(f"Médico com ID '{medico1.id_medico}' não encontrado.")

    print("\nBuscando médicos por nome parcial 'Grey':")
    medicos_encontrados_nome = buscar_medicos_por_nome(lista_de_medicos, "Grey")
    if medicos_encontrados_nome:
        for m_res in medicos_encontrados_nome:
            print(f"- {m_res}")
    else:
        print("Nenhum médico encontrado com 'Grey' no nome.")

    print("\nBuscando médicos por especialidade 'Diagnóstico':")
    medicos_encontrados_esp = buscar_medicos_por_especialidade(lista_de_medicos, "Diagnóstico")
    if medicos_encontrados_esp:
        for m_res in medicos_encontrados_esp:
            print(f"- {m_res}")
    else:
        print("Nenhum médico encontrado com a especialidade 'Diagnóstico'.")
    
    print(f"\nBuscando pacientes do {medico1.nome_completo} (ID: {medico1.id_medico}):")
    pacientes_do_medico = buscar_pacientes_do_medico(lista_de_pacientes, medico1.id_medico)
    if pacientes_do_medico:
        for p_res in pacientes_do_medico:
            print(f"- {p_res.nome_completo} (ID Paciente: {p_res.id_paciente}, Prioridade: {p_res.prioridade_medica})")
    else:
        print(f"Nenhum paciente encontrado para o médico {medico1.nome_completo}.")
        
    print("\n\nSimulação e demonstração de busca concluídas.")