import datetime
from Paciente import Paciente
from Medico import Medico
import gerenciador_pacientes as gp
import gerenciador_medicos as gm
import os

#Menu functions
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def exibir_menu_principal():
    print("\nSistema de Gerenciamento Hospitalar ")
    print("==========================================")
    print("1. Gerenciar Pacientes")
    print("2. Gerenciar Médicos")
    print("3. Iniciar Simulação de Atendimento de Emergência")
    print("0. Sair do Sistema")
    print("==========================================")
    return input("Escolha uma opção: ")


def exibir_menu_pacientes():
    print("\n--- Gerenciar Pacientes ---")
    print("1. Adicionar Novo Paciente à Fila")
    print("2. Listar Todos os Pacientes (na ordem atual)")
    print("3. Ordenar Pacientes por Prioridade (para atendimento/busca)")
    print("4. Buscar Pacientes por Prioridade (e Data de Admissão opcional)")
    print("5. Atribuir Médico a Paciente")
    print("9. Voltar ao Menu Principal")
    return input("Escolha uma opção: ")


def exibir_menu_medicos():
    print("\n--- Gerenciar Médicos ---")
    print("1. Adicionar Novo Médico")
    print("2. Listar Todos os Médicos (na ordem atual)")
    print("3. Ordenar Médicos por Nome")
    print("4. Ordenar Médicos por Especialidade")
    print("5. Buscar Médico por ID")
    print("6. Buscar Médicos por Nome Parcial")
    print("7. Buscar Médicos por Especialidade")
    print("8. Listar Pacientes Atribuídos a um Médico")
    print("9. Voltar ao Menu Principal")
    return input("Escolha uma opção: ")


def adicionar_novo_paciente(lista_pacientes):
    limpar_tela()
    print("--- Adicionar Novo Paciente ---")
    nome = input("Nome completo do paciente: ")
    while True:
        try:
            prioridade_str = input("Prioridade Médica (1-Emergência a 5-Não Urgente): ")
            prioridade = int(prioridade_str)
            if not 1 <= prioridade <= 5:
                raise ValueError("Prioridade fora do intervalo.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número entre 1 e 5.")

    # Function that adds a simple sequential ID
    id_paciente_novo = (max(p.id_paciente for p in lista_pacientes if isinstance(p.id_paciente, int)) + 1) \
        if any(isinstance(p.id_paciente, int) for p in lista_pacientes) else 101

    novo_paciente = Paciente(nome, prioridade, id_paciente=id_paciente_novo)
    lista_pacientes.append(novo_paciente)
    print(f"\nPaciente '{novo_paciente.nome_completo}' adicionado com ID {id_paciente_novo}.")
    print(f"Detalhes: {novo_paciente}")
    input("\nPressione Enter para continuar...")
    return novo_paciente


def adicionar_novo_medico(lista_medicos):
    limpar_tela()
    print("--- Adicionar Novo Médico ---")
    nome = input("Nome completo do médico: ")
    especialidade = input("Especialidade: ")
    # ID simples para exemplo
    id_medico_novo = f"MED-{(max(int(m.id_medico.split('-')[1]) for m in lista_medicos if m.id_medico.startswith('MED-') and m.id_medico.split('-')[1].isdigit()) + 1) if any(m.id_medico.startswith('MED-') for m in lista_medicos) else 101}"

    novo_medico = Medico(nome, especialidade, id_medico=id_medico_novo)
    lista_medicos.append(novo_medico)
    print(f"\nMédico '{novo_medico.nome_completo}' adicionado com ID {id_medico_novo}.")
    print(f"Detalhes: {novo_medico}")
    input("\nPressione Enter para continuar...")
    return novo_medico


def listar_entidades_formatado(lista_entidades, titulo="Lista de Entidades"):
    limpar_tela()
    print(f"--- {titulo} ---")
    if not lista_entidades:
        print("Nenhuma entidade encontrada.")
    else:
        for y, entidade in enumerate(lista_entidades):
            print(f"{y + 1}. {entidade}")
    print("-" * (len(titulo) + 6))
    input("\nPressione Enter para continuar...")


def carregar_dados_iniciais():

    pacientes = [
        Paciente("Carlos Silva", 2, 1, data_admissao=datetime.datetime(2023, 10, 20, 10, 0, 0)),
        Paciente("Ana Pereira", 1, 2, data_admissao=datetime.datetime(2023, 10, 20, 10, 5, 0)),
        Paciente("João Costa", 3, 3, data_admissao=datetime.datetime(2023, 10, 20, 9, 30, 0)),
        Paciente("Maria Oliveira", 2, 4, data_admissao=datetime.datetime(2023, 10, 20, 10, 2, 0)),
        Paciente("Lucas Martins", 4, 5, data_admissao=datetime.datetime(2023, 10, 20, 8, 0, 0)),
        Paciente("Beatriz Almeida", 2, 6, data_admissao=datetime.datetime(2023, 10, 20, 10, 1, 0)),
        Paciente("Mario Souza", 3, 7, data_admissao=datetime.datetime(2023, 10, 20, 9, 35, 0)),
        Paciente("Fernanda Lima", 2, 8, data_admissao=datetime.datetime(2023, 10, 20, 10, 3, 0)),
        Paciente("Roberto Dias", 5, 9, data_admissao=datetime.datetime(2023, 10, 20, 11, 0, 0)),
        Paciente("Ana Silva", 1, 10, data_admissao=datetime.datetime(2023, 10, 20, 10, 4, 0))

    ]
    medicos = [
        Medico("Dr. Gregory House", "Diagnóstico", "MED-001"),
        Medico("Dra. Meredith Grey", "Cirurgia Geral", "MED-002"),
        Medico("Dr. Derek Shepherd", "Neurocirurgia", "MED-003"),
        Medico("Dra. Cristina Yang", "Cardiologia", "MED-004"),
        Medico("Dr. James Wilson", "Oncologia", "MED-005")
    ]

    pacientes[0].atribuir_medico("MED-002")  # Carlos Silva com Dra. Meredith Grey
    pacientes[5].atribuir_medico("MED-001")  # Beatriz Almeida com Dr. Gregory House
    pacientes[9].atribuir_medico("MED-004")  # Ana Clara Silva com Dra. Cristina Yang
    pacientes[2].atribuir_medico("MED-001")  # João Costa com Dr. Gregory House

    return pacientes, medicos


# Main Loop
if __name__ == "__main__":
    lista_de_pacientes, lista_de_medicos = carregar_dados_iniciais()

    pacientes_ordenados_para_busca_prioridade = False
    while True:
        limpar_tela()
        escolha_principal = exibir_menu_principal()

        # --- MANAGE PATIENTS---
        if escolha_principal == '1':
            while True:
                limpar_tela()
                escolha_pacientes = exibir_menu_pacientes()
                if escolha_pacientes == '1':
                    adicionar_novo_paciente(lista_de_pacientes)
                    pacientes_ordenados_para_busca_prioridade = False
                elif escolha_pacientes == '2':
                    listar_entidades_formatado(lista_de_pacientes, "Lista de Todos os Pacientes (Ordem Atual)")
                elif escolha_pacientes == '3':
                    gp.ordenar_pacientes(lista_de_pacientes)
                    pacientes_ordenados_para_busca_prioridade = True
                    listar_entidades_formatado(lista_de_pacientes, "Pacientes Ordenados por Prioridade e Admissão")
                elif escolha_pacientes == '4':
                    if not pacientes_ordenados_para_busca_prioridade:
                        print(
                            "\nAlerta: A lista de pacientes precisa ser ordenada por prioridade primeiro (Opção 3 do menu de pacientes).")
                        print("Ordenando agora para otimizar a busca...")
                        gp.ordenar_pacientes(lista_de_pacientes)
                        pacientes_ordenados_para_busca_prioridade = True
                        input("Lista ordenada. Pressione Enter para continuar com a busca...")

                    limpar_tela()
                    print("--- Buscar Pacientes por Prioridade ---")
                    while True:
                        try:
                            prioridade_busca_str = input("Digite a prioridade para busca (1-5): ")
                            prioridade_busca = int(prioridade_busca_str)
                            if not 1 <= prioridade_busca <= 5:
                                raise ValueError("Prioridade fora do intervalo.")
                            break
                        except ValueError:
                            print("Entrada inválida para prioridade.")
                    data_adm_busca_str = input(
                        "Digite a data de admissão (AAAA-MM-DD HH:MM) ou deixe em branco para buscar apenas por prioridade: ")

                    resultados_busca_p = gp.buscar_pacientes_binaria(
                        lista_de_pacientes, prioridade_busca, data_adm_busca_str if data_adm_busca_str else None
                    )
                    listar_entidades_formatado(resultados_busca_p,
                                               f"Resultado da Busca (Prioridade: {prioridade_busca})")

                elif escolha_pacientes == '5':
                    limpar_tela()
                    print("--- Atribuir Médico a Paciente ---")
                    listar_entidades_formatado(lista_de_pacientes, "Pacientes Disponíveis")
                    id_pac_str = input("Digite o ID do Paciente para atribuir médico: ")
                    try:
                        id_pac_int = int(id_pac_str)
                        pac_encontrado = next((p for p in lista_de_pacientes if p.id_paciente == id_pac_int), None)
                    except ValueError:
                        pac_encontrado = None

                    if pac_encontrado:
                        limpar_tela()
                        listar_entidades_formatado(lista_de_medicos, "Médicos Disponíveis")
                        id_med_str = input(f"Digite o ID do Médico para atribuir a {pac_encontrado.nome_completo}: ")
                        med_encontrado = gm.buscar_medico_por_id(lista_de_medicos, id_med_str)
                        if med_encontrado:
                            pac_encontrado.atribuir_medico(med_encontrado.id_medico)
                            print(
                                f"\n{pac_encontrado.nome_completo} atribuído a {med_encontrado.nome_completo} com sucesso!")
                        else:
                            print(f"\nMédico com ID '{id_med_str}' não encontrado.")
                    else:
                        print(f"\nPaciente com ID '{id_pac_str}' não encontrado.")
                    input("\nPressione Enter para continuar...")

                elif escolha_pacientes == '9':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")


        # --- MANAGE DOCTORS---

        elif escolha_principal == '2':
            while True:
                limpar_tela()
                escolha_medicos = exibir_menu_medicos()
                if escolha_medicos == '1':
                    adicionar_novo_medico(lista_de_medicos)
                elif escolha_medicos == '2':
                    listar_entidades_formatado(lista_de_medicos, "Lista de Todos os Médicos (Ordem Atual)")
                elif escolha_medicos == '3':
                    gm.ordenar_medicos(lista_de_medicos, "nome")
                    listar_entidades_formatado(lista_de_medicos, "Médicos Ordenados por Nome")
                elif escolha_medicos == '4':
                    gm.ordenar_medicos(lista_de_medicos, "especialidade")
                    listar_entidades_formatado(lista_de_medicos, "Médicos Ordenados por Especialidade (e Nome)")
                elif escolha_medicos == '5':
                    limpar_tela()
                    id_busca_m = input("Digite o ID do médico para busca (ex: MED-001): ")
                    medico_res_id = gm.buscar_medico_por_id(lista_de_medicos, id_busca_m)
                    if medico_res_id:
                        listar_entidades_formatado([medico_res_id], f"Resultado da Busca por ID: {id_busca_m}")
                    else:
                        print(f"Médico com ID '{id_busca_m}' não encontrado.")
                        input("Pressione Enter para continuar...")
                elif escolha_medicos == '6':
                    limpar_tela()
                    nome_busca_m = input("Digite o nome parcial do médico para busca: ")
                    medicos_res_nome = gm.buscar_medicos_por_nome(lista_de_medicos, nome_busca_m)
                    listar_entidades_formatado(medicos_res_nome, f"Resultado da Busca por Nome: '{nome_busca_m}'")
                elif escolha_medicos == '7':
                    limpar_tela()
                    esp_busca_m = input("Digite a especialidade do médico para busca: ")
                    medicos_res_esp = gm.buscar_medicos_por_especialidade(lista_de_medicos, esp_busca_m)
                    listar_entidades_formatado(medicos_res_esp,
                                               f"Resultado da Busca por Especialidade: '{esp_busca_m}'")
                elif escolha_medicos == '8':
                    limpar_tela()
                    id_med_para_pac = input("Digite o ID do médico para listar seus pacientes: ")
                    medico_obj = gm.buscar_medico_por_id(lista_de_medicos, id_med_para_pac)
                    if medico_obj:
                        pacientes_do_med = gm.buscar_pacientes_do_medico(lista_de_pacientes,
                                                                                    medico_obj.id_medico)
                        listar_entidades_formatado(pacientes_do_med, f"Pacientes do {medico_obj.nome_completo}")
                    else:
                        print(f"Médico com ID '{id_med_para_pac}' não encontrado.")
                        input("Pressione Enter para continuar...")
                elif escolha_medicos == '9':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar...")


        # --- SERVICE SIMULATION ---

        elif escolha_principal == '3':
            limpar_tela()
            print("--- Iniciando Simulação de Atendimento de Emergência ---")

            if not lista_de_pacientes:
                print("Não há pacientes cadastrados para iniciar a simulação.")
                input("\nPressione Enter para voltar ao menu principal...")
                continue

            gp.ordenar_pacientes(lista_de_pacientes)
            pacientes_ordenados_para_busca_prioridade = True

            lista_para_atendimento_simulacao = list(lista_de_pacientes)

            print("\nFila inicial para atendimento (ordenada):")
            listar_entidades_formatado(lista_para_atendimento_simulacao, "Fila para Simulação")  # Mostra e pausa

            contadores_fila = {'atendidos_nivel2_desde_ultimo_nivel3_ou_4': 0}
            pacientes_atendidos_na_simulacao = []

            print("\nIniciando simulação passo a passo...")
            input("Pressione Enter para o primeiro atendimento...")

            while lista_para_atendimento_simulacao:
                limpar_tela()
                print("--- Simulação em Andamento ---")
                print("Fila atual antes da seleção:")
                for i, p_fila in enumerate(lista_para_atendimento_simulacao):
                    print(f"  {i + 1}. {p_fila}")
                print("-" * 30)

                proximo_a_atender = gp.selecionar_proximo(
                    lista_para_atendimento_simulacao, contadores_fila
                )

                if proximo_a_atender:
                    pacientes_atendidos_na_simulacao.append(proximo_a_atender)
                    nome_medico_resp = "N/A"
                    if proximo_a_atender.id_medico_atribuido:
                        med_obj_sim = gm.buscar_medico_por_id(lista_de_medicos, proximo_a_atender.id_medico_atribuido)
                        if med_obj_sim:
                            nome_medico_resp = med_obj_sim.nome_completo

                    print(
                        f"\n--> ATENDENDO: {proximo_a_atender.nome_completo} (P: {proximo_a_atender.prioridade_medica}) "
                        f"\n    Médico Responsável: {nome_medico_resp} "
                        f"\n    (Contador Nível 2: {contadores_fila.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0)})"
                    )
                    if lista_para_atendimento_simulacao:
                        input("\nPressione Enter para o próximo atendimento...")
                    else:
                        print("\nTodos os pacientes da fila foram atendidos.")
                        input("Pressione Enter para ver o resumo...")
                else:
                    print("\nFila de atendimento esvaziou (condição inesperada).")
                    break

            limpar_tela()
            print("--- Simulação Concluída ---")
            listar_entidades_formatado(pacientes_atendidos_na_simulacao, "Ordem Final de Atendimento na Simulação")
            input("Pressione Enter para voltar ao menu principal...")

        # --- EXIT ---
        elif escolha_principal == '0':
            limpar_tela()
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
            input("Pressione Enter para continuar...")