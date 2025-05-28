import datetime
from Paciente import Paciente
from Medico import Medico
import gerenciador_pacientes as gp
import gerenciador_medicos as gm


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

    gp.ordenar_pacientes(lista_de_pacientes)

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

    gm.ordenar_medicos(lista_de_medicos, "especialidade")
    print("\nLista de Médicos Ordenada por Especialidade (e Nome):")
    for m in lista_de_medicos:
        print(m)

    gm.ordenar_medicos(lista_de_medicos, "nome")
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

    # FILA DE ATENDIMENTO / SAIDA ORDENAÇÃO
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

        proximo_a_atender = gp.selecionar_proximo(lista_para_atendimento, contadores_fila)

        if proximo_a_atender:
            pacientes_atendidos_ordem.append(proximo_a_atender)
            # Tenta buscar o nome do médico para exibição
            nome_medico_responsavel = "N/A"
            if proximo_a_atender.id_medico_atribuido:
                medico_obj = gm.buscar_medico_por_id(lista_de_medicos, proximo_a_atender.id_medico_atribuido)
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
    resultados_p1 = gp.buscar_pacientes_binaria(lista_de_pacientes, 1)
    if resultados_p1:
        for p_res in resultados_p1:
            print(f"- {p_res.nome_completo} (Prioridade: {p_res.prioridade_medica}, Admissão: {p_res.data_admissao.strftime('%d/%m/%Y %H:%M')})")
    else:
        print("Nenhum paciente encontrado com Prioridade 1.")

    data_especifica_busca = datetime.datetime(2023, 10, 20, 9, 30, 0)
    print(f"\nBuscando Pacientes com Prioridade 3 e Admissão em {data_especifica_busca.strftime('%d/%m/%Y %H:%M:%S')}:")
    resultados_p3_data = gp.buscar_pacientes_binaria(lista_de_pacientes, 3, data_especifica_busca)
    if resultados_p3_data:
        for p_res in resultados_p3_data:
            print(f"- {p_res.nome_completo} (Prioridade: {p_res.prioridade_medica}, Admissão: {p_res.data_admissao.strftime('%d/%m/%Y %H:%M')})")
    else:
        print("Nenhum paciente encontrado com estes critérios.")

    print(f"\nBuscando médico por ID ('{medico1.id_medico}'):")
    medico_encontrado = gm.buscar_medico_por_id(lista_de_medicos, medico1.id_medico)
    if medico_encontrado:
        print(f"- Encontrado: {medico_encontrado}") 
    else:
        print(f"Médico com ID '{medico1.id_medico}' não encontrado.")

    print("\nBuscando médicos por nome parcial 'Grey':")
    medicos_encontrados_nome = gm.buscar_medicos_por_nome(lista_de_medicos, "Grey")
    if medicos_encontrados_nome:
        for m_res in medicos_encontrados_nome:
            print(f"- {m_res}")
    else:
        print("Nenhum médico encontrado com 'Grey' no nome.")

    print("\nBuscando médicos por especialidade 'Diagnóstico':")
    medicos_encontrados_esp = gm.buscar_medicos_por_especialidade(lista_de_medicos, "Diagnóstico")
    if medicos_encontrados_esp:
        for m_res in medicos_encontrados_esp:
            print(f"- {m_res}")
    else:
        print("Nenhum médico encontrado com a especialidade 'Diagnóstico'.")
    
    print(f"\nBuscando pacientes do {medico1.nome_completo} (ID: {medico1.id_medico}):")
    pacientes_do_medico = gm.buscar_pacientes_do_medico(lista_de_pacientes, medico1.id_medico)
    if pacientes_do_medico:
        for p_res in pacientes_do_medico:
            print(f"- {p_res.nome_completo} (ID Paciente: {p_res.id_paciente}, Prioridade: {p_res.prioridade_medica})")
    else:
        print(f"Nenhum paciente encontrado para o médico {medico1.nome_completo}.")
        
    print("\n\nSimulação e demonstração de busca concluídas.")