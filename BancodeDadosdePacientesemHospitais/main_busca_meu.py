import datetime # datas e horas.
import uuid     # ID's únicos

# --- Classe: Paciente ---
class Paciente:
    # Dados de um paciente: ID, nome, prioridade (1 a 5) e hora de entrada.
    def __init__(self, nome_completo: str, prioridade_medica: int, id_paciente: str, data_admissao: datetime.datetime = None):
        # Cria um paciente. Prioridade obrigatório entre 1-5; data de entrada é a atual.
        self.id_paciente = id_paciente
        self.nome_completo = nome_completo
        if not 1 <= prioridade_medica <= 5: raise ValueError("Prioridade médica deve estar entre 1 e 5.")
        self.prioridade_medica = prioridade_medica
        self.data_admissao = data_admissao if data_admissao else datetime.datetime.now()
    def __str__(self): return (f"Paciente: {self.nome_completo:<20} | Prioridade: {self.prioridade_medica} | Admissão: {self.data_admissao.strftime('%d/%m/%Y %H:%M:%S')} | ID: {self.id_paciente}")
    def __repr__(self): return (f"Paciente(ID: '{self.id_paciente}', Nome: '{self.nome_completo}', Prioridade: {self.prioridade_medica}, Admissão: '{self.data_admissao.isoformat()}')")

# --- Função ordenar_pacientes ---
def ordenar_pacientes(lista_pacientes: list[Paciente]):
    # Ordena a lista de pacientes por prioridade (menor primeiro) e, se empatar, por data de admissão (mais antiga primeiro).
    n = len(lista_pacientes)
    for i in range(1, n):
        paciente_atual, j = lista_pacientes[i], i - 1
        while j >= 0 and (paciente_atual.prioridade_medica < lista_pacientes[j].prioridade_medica or (paciente_atual.prioridade_medica == lista_pacientes[j].prioridade_medica and paciente_atual.data_admissao < lista_pacientes[j].data_admissao)):
            lista_pacientes[j + 1] = lista_pacientes[j]; j -= 1
        lista_pacientes[j + 1] = paciente_atual

# --- Função selecionar_proximo ---
def selecionar_proximo(lista_aguardando: list[Paciente], contadores_atendimento: dict) -> Paciente | None:
    # Seleciona o próximo paciente para atendimento. Prioridade 1 primeiro. Outras prioridades revezam (2 Nível 2 para 1 Nível 3/4).
    # Remove o paciente da lista.    
    if not lista_aguardando: return None
    if lista_aguardando[0].prioridade_medica == 1: return lista_aguardando.pop(0)

    idx2, idx3, idx4 = -1, -1, -1 # Índices dos primeiros de cada prioridade
    for i, p in enumerate(lista_aguardando):
        if p.prioridade_medica == 2 and idx2 == -1: idx2 = i
        elif p.prioridade_medica == 3 and idx3 == -1: idx3 = i
        elif p.prioridade_medica == 4 and idx4 == -1: idx4 = i
        if idx2 != -1 and idx3 != -1 and idx4 != -1: break

    # Lógica de revezamento e seleção
    if contadores_atendimento.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0) >= 2:
        if idx3 != -1: paciente = lista_aguardando.pop(idx3); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0; return paciente
        elif idx4 != -1: paciente = lista_aguardando.pop(idx4); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0; return paciente
        elif idx2 != -1: paciente = lista_aguardando.pop(idx2); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] += 1; return paciente
    else:
        if idx2 != -1: paciente = lista_aguardando.pop(idx2); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = contadores_atendimento.get('atendidos_nivel2_desde_ultimo_nivel3_ou_4', 0) + 1; return paciente
        elif idx3 != -1: paciente = lista_aguardando.pop(idx3); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0; return paciente
        elif idx4 != -1: paciente = lista_aguardando.pop(idx4); contadores_atendimento['atendidos_nivel2_desde_ultimo_nivel3_ou_4'] = 0; return paciente

    if lista_aguardando: return lista_aguardando.pop(0)
    return None

# --- Função buscar_pacientes ---
def buscar_pacientes_binaria(lista_pacientes: list[Paciente], prioridade_alvo: int, data_admissao_alvo: datetime.datetime = None) -> list[Paciente]:
    # Busca por pacientes em uma lista ordenada por prioridade e data admissão. Encontra os pacientes com `prioridade_alvo` e caso for, `data_admissao_alvo`.
    # Retorna uma lista de resultados.
    resultados, esquerda, direita, primeiro_encontrado_idx = [], 0, len(lista_pacientes) - 1, -1
    while esquerda <= direita: # Fase 1: Acha o primeiro item.
        meio = (esquerda + direita) // 2; paciente_meio = lista_pacientes[meio]
        if paciente_meio.prioridade_medica < prioridade_alvo: esquerda = meio + 1
        elif paciente_meio.prioridade_medica > prioridade_alvo: direita = meio - 1
        else: # Prioridade OK
            if data_admissao_alvo is not None:
                if paciente_meio.data_admissao < data_admissao_alvo: esquerda = meio + 1
                elif paciente_meio.data_admissao > data_admissao_alvo: direita = meio - 1
                else: primeiro_encontrado_idx = meio; direita = meio - 1 
            else: primeiro_encontrado_idx = meio; direita = meio - 1 

    if primeiro_encontrado_idx != -1: # Fase 2: busca todos os itens encontrados.
        idx = primeiro_encontrado_idx
        while idx >= 0 and lista_pacientes[idx].prioridade_medica == prioridade_alvo and (data_admissao_alvo is None or lista_pacientes[idx].data_admissao == data_admissao_alvo):
            resultados.append(lista_pacientes[idx]); idx -= 1
        resultados.reverse(); idx = primeiro_encontrado_idx + 1
        while idx < len(lista_pacientes) and lista_pacientes[idx].prioridade_medica == prioridade_alvo and (data_admissao_alvo is None or lista_pacientes[idx].data_admissao == data_admissao_alvo):
            resultados.append(lista_pacientes[idx]); idx += 1
    return resultados

# --- Bloco Principal ---
if __name__ == "__main__":
    print("Simulando sistema de pacientes.")
    # Cria e mostra pacientes.
    pacientes = [Paciente("Carlos Silva", 2, "EMG-001", datetime.datetime(2023, 10, 20, 10, 0, 0)), 
                 Paciente("Ana Pereira", 1, "EMG-002", datetime.datetime(2023, 10, 20, 10, 5, 0)),
                 Paciente("João Costa", 3, "EMG-003", datetime.datetime(2023, 10, 20, 9, 30, 0)), 
                 Paciente("Maria Oliveira", 2, "EMG-004", datetime.datetime(2023, 10, 20, 10, 2, 0)), 
                 Paciente("Lucas Martins", 4, "EMG-005", datetime.datetime(2023, 10, 20, 8, 0, 0)), 
                 Paciente("Beatriz Almeida", 2, "EMG-006", datetime.datetime(2023, 10, 20, 10, 1, 0)),
                 Paciente("Mario Souza", 3, "EMG-007", datetime.datetime(2023, 10, 20, 9, 35, 0)),
                 Paciente("Fernanda Lima", 2, "EMG-008", datetime.datetime(2023, 10, 20, 10, 3, 0)),
                 Paciente("Roberto Dias", 5, "EMG-009", datetime.datetime(2023, 10, 20, 11, 0, 0)),
                 Paciente("Ana Silva", 1, "EMG-010", datetime.datetime(2023, 10, 20, 10, 4, 0))]
    print("\n--- Lista Original ---"); [print(p) for p in pacientes]

    # Ordena e mostra ordenado.
    ordenar_pacientes(pacientes)
    print("\n--- Lista Ordenada ---"); [print(p) for p in pacientes]

    # Simulação de atendimento.
    print("\n--- Simulação de Atendimento ---")
    fila_atendimento = list(pacientes); atendidos = []; contadores = {'atendidos_nivel2_desde_ultimo_nivel3_ou_4': 0}
    while fila_atendimento:
        proximo = selecionar_proximo(fila_atendimento, contadores)
        if proximo: atendidos.append(proximo); print(f"--> ATENDENDO: {proximo.nome_completo} (Prio: {proximo.prioridade_medica})")
        else: print("Fila vazia."); break
    print("\n--- Ordem de Atendimento ---"); [print(f"{i+1}. {p.nome_completo} (Prio: {p.prioridade_medica})") for i,p in enumerate(atendidos)]

    # Demonstração de busca.
    print("\n--- Demonstração de Busca Binária ---")
    print("\nBuscando Prioridade 1:"); res = buscar_pacientes_binaria(pacientes, 1); [print(f"- {p.nome_completo}") for p in res] if res else print("Nenhum.")
    print("\nBuscando Prioridade 3, 09:30:00:"); res = buscar_pacientes_binaria(pacientes, 3, datetime.datetime(2023, 10, 20, 9, 30, 0)); [print(f"- {p.nome_completo}") for p in res] if res else print("Nenhum.")
    print("\nSimulação concluída.")